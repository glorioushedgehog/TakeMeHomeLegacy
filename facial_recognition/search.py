import io
import os
import re
import sys
import time
from threading import Thread

import imageio
import numpy as np
from PIL import Image
from django.core.files.images import ImageFile

from facial_recognition import infer
from tmh.models import InferenceTask, ImageData

distance_threshold = 1.0


# this is needed to avoid reliance on the client requesting
# the search results in order to delete the inference task
def delete_old_inference_tasks():
    tasks = InferenceTask.objects.all()
    num_seconds_in_day = 24 * 60 * 60
    now = time.time()
    for a_task in tasks:
        task_age = now - a_task.date_created.timestamp()
        if task_age > num_seconds_in_day:
            a_task.delete()


def image_to_byte_array(image):
    image_bytes = bytearray(0)
    for a_chunk in image.chunks():
        image_bytes += a_chunk
    return image_bytes


def embedding_to_string(embedding):
    embedding_string = str(list(embedding))
    embedding_string = re.sub(r"\s", "", embedding_string)
    embedding_string = re.sub(r"\[", "", embedding_string)
    embedding_string = re.sub(r"\]", "", embedding_string)
    return embedding_string


def search_image(task, image):
    image_bytes = image_to_byte_array(image)
    image_as_array = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    image_as_array = np.array(image_as_array)
    bounding_boxes, image_size = infer.single_image_bounding_boxes(image_as_array)
    if len(bounding_boxes) < 1:
        print("can't detect face")
        task.state = task.ERROR
        task.save()
        return
    task.state = task.ANALYZING_FACE
    task.save()
    cropped_image = [infer.crop_image(image_as_array, bounding_boxes, image_size)]
    embeddings = infer.get_embeddings(cropped_image)
    task.state = task.SUCCESS
    string_embedding = embedding_to_string(embeddings[0])
    task.embedding = string_embedding
    task.save()


def init_inference_task(image):
    delete_old_inference_tasks()
    task = InferenceTask.objects.create()
    thread = Thread(target=search_image, args=(task, image,))
    thread.start()
    return task.id


def embedding_from_string(embedding_string):
    nums = embedding_string.strip().split(',')
    embedding = np.asarray(list(map(float, nums)))
    return embedding


def distance(embedding, string_embedding):
    try:
        nums = string_embedding.strip().split(',')
        other_embedding = np.asarray(list(map(float, nums)))
        diff = np.subtract(embedding, other_embedding)
    except ValueError:
        return sys.maxsize
    dist = np.sum(np.square(diff))
    return dist


def get_matching_persons(embedding_string, image_datas):
    embedding = embedding_from_string(embedding_string)
    keys = []
    for image_data in image_datas:
        if not image_data.embedding:
            continue
        a_distance = distance(embedding, image_data.embedding)
        if a_distance == sys.maxsize:
            print("invalid embedding for person:")
            print("person:")
            print(image_data.person)
            print("embedding:")
            print(image_data.embedding)
        if a_distance < distance_threshold:
            keys.append(image_data.person.primarykey)
    return keys


def image_datas_without_embeddings():
    image_datas = []
    all_image_datas = ImageData.objects.all()
    for image_data in all_image_datas:
        if not image_data.embedding:
            image_datas.append(image_data)
    return image_datas


def create_image_datas(persons):
    for person in persons:
        if hasattr(person, 'imagedata'):
            continue
        image_bytes = person.picture
        try:
            image = Image.open(io.BytesIO(image_bytes))
            path = person.primarykey + ".BMP"
            image.save(path)
            new_image_data = ImageData(person=person, picture=ImageFile(open(path, "rb")))
            new_image_data.save()
            os.remove(path)
        except OSError:
            print("could not parse image for person", person.primarykey)
            pass
    embed_image_datas(image_datas_without_embeddings())


def embed_image_datas(image_datas):
    image_datas_with_detectable_faces = []
    aligned_images = []
    mtcnn = infer.get_alignment_mtcnn()
    for image_data in image_datas:
        img = imageio.imread(os.path.expanduser(image_data.picture.url), pilmode='RGB')
        bounding_boxes, image_size = infer.get_bounding_boxes(img, mtcnn)
        # ensure a face was detected
        if len(bounding_boxes) < 1:
            print("no face detected for person", image_data.person.primarykey)
            continue
        cropped_image = infer.crop_image(img, bounding_boxes, image_size)
        aligned_images.append(cropped_image)
        image_datas_with_detectable_faces.append(image_data)
        print(image_data.person.primarykey + " image aligned")
    embeddings = infer.get_embeddings(aligned_images)
    if len(embeddings) != len(image_datas_with_detectable_faces):
        print("could not embed all images. exiting.")
        print("please report this error to takemehomesoftware@outlook.com")
        return
    i = 0
    for image_data in image_datas_with_detectable_faces:
        the_embedding = embeddings[i]
        image_data.embedding = embedding_to_string(the_embedding)
        image_data.save()
        i += 1
    print("SUCCESS! facial recognition search preparation complete!")
    print("reload /manage_facial_recognition to see new coverage stats")


def prepare_for_facial_recognition(persons):
    thread = Thread(target=create_image_datas, args=(persons,))
    thread.start()
