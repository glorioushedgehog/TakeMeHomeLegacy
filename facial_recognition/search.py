import io
import os
import re
import sys
import time
from threading import Thread
import numpy as np
from PIL import Image
import tensorflow as tf


from facial_recognition import detect_face, facenet
from tmh.models import InferenceTask

distance_threshold = 1.0


# this is needed to avoid reliance on the client requesting
# the search results in order to delete the inference task
def delete_old_inference_tasks():
    tasks = InferenceTask.objects.all()
    num_seconds_in_day = 24 * 60 * 60
    for a_task in tasks:
        task_age = time.time() - a_task.date_created.timestamp()
        if task_age > num_seconds_in_day:
            a_task.delete()


def search_image(task, image_bytes):
    delete_old_inference_tasks()
    img = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    img = np.array(img)

    minsize = 20  # minimum size of face
    threshold = [0.6, 0.7, 0.7]  # three steps's threshold
    factor = 0.709  # scale factor
    margin = 44
    image_size = 160

    print('Creating networks and loading parameters')
    with tf.Graph().as_default():
        gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=1.0)
        sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options, log_device_placement=False))
        with sess.as_default():
            pnet, rnet, onet = detect_face.create_mtcnn(sess, None)

    img_size = np.asarray(img.shape)[0:2]
    bounding_boxes, _ = detect_face.detect_face(img, minsize, pnet, rnet, onet, threshold, factor)
    if len(bounding_boxes) < 1:
        print("can't detect face")
        task.state = task.ERROR
        task.save()
        return
    task.state = task.ANALYZING_FACE
    task.save()
    det = np.squeeze(bounding_boxes[0, 0:4])
    bb = np.zeros(4, dtype=np.int32)
    bb[0] = np.maximum(det[0] - margin / 2, 0)
    bb[1] = np.maximum(det[1] - margin / 2, 0)
    bb[2] = np.minimum(det[2] + margin / 2, img_size[1])
    bb[3] = np.minimum(det[3] + margin / 2, img_size[0])
    cropped = img[bb[1]:bb[3], bb[0]:bb[2], :]
    aligned = np.array(Image.fromarray(cropped).resize((image_size, image_size)))
    prewhitened = facenet.prewhiten(aligned)
    images = [prewhitened]

    with tf.Graph().as_default():
        with tf.Session() as sess:
            # Load the model
            facenet.load_model(os.path.join("facial_recognition", "model.pb"))
            # Get input and output tensors
            images_placeholder = tf.get_default_graph().get_tensor_by_name("input:0")
            embeddings = tf.get_default_graph().get_tensor_by_name("embeddings:0")
            phase_train_placeholder = tf.get_default_graph().get_tensor_by_name("phase_train:0")
            # Run forward pass to calculate embeddings
            feed_dict = {images_placeholder: images, phase_train_placeholder: False}
            emb = sess.run(embeddings, feed_dict=feed_dict)
    task.state = task.SUCCESS
    embedding_string = str(list(emb[0]))
    embedding_string = re.sub(r"\s", "", embedding_string)
    embedding_string = re.sub(r"\[", "", embedding_string)
    embedding_string = re.sub(r"\]", "", embedding_string)
    task.embedding = embedding_string
    task.save()


def init_inference_task(image):
    task = InferenceTask.objects.create()
    image_bytes = bytearray(0)
    for a_chunk in image.chunks():
        image_bytes += a_chunk
    thread = Thread(target=search_image, args=(task, image_bytes,))
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
    except Exception:
        return sys.maxsize
    dist = np.sum(np.square(diff))
    return dist


def get_matching_persons(embedding_string, image_datas):
    embedding = embedding_from_string(embedding_string)
    keys = []
    for image_data in image_datas:
        a_distance = distance(embedding, image_data.embedding)
        print(a_distance)
        if a_distance < distance_threshold:
            keys.append(image_data.primarykey)
    return keys
