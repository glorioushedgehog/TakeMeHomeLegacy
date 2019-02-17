import os

import imageio
import numpy as np
from PIL import Image
from io import BytesIO
import base64
import tensorflow as tf


from facial_recognition import detect_face, facenet


def infer(image):
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

    img = imageio.imread(os.path.expanduser(image), pilmode='RGB')
    img_size = np.asarray(img.shape)[0:2]
    bounding_boxes, _ = detect_face.detect_face(img, minsize, pnet, rnet, onet, threshold, factor)
    if len(bounding_boxes) < 1:
        print("can't detect face")
        return None
    det = np.squeeze(bounding_boxes[0, 0:4])
    bb = np.zeros(4, dtype=np.int32)
    bb[0] = np.maximum(det[0] - margin / 2, 0)
    bb[1] = np.maximum(det[1] - margin / 2, 0)
    bb[2] = np.minimum(det[2] + margin / 2, img_size[1])
    bb[3] = np.minimum(det[3] + margin / 2, img_size[0])
    cropped = img[bb[1]:bb[3], bb[0]:bb[2], :]

    # aligned = misc.imresize(cropped, (image_size, image_size), interp='bilinear')
    aligned = np.array(Image.fromarray(cropped).resize((image_size, image_size)))

    prewhitened = facenet.prewhiten(aligned)
    images = [prewhitened]

    with tf.Graph().as_default():
        with tf.Session() as sess:
            # Load the model
            facenet.load_model("C:\\Users\\Paul\\PycharmProjects\\TakeMeHomeDjango\\facial_recognition\\model.pb")
            # Get input and output tensors
            images_placeholder = tf.get_default_graph().get_tensor_by_name("input:0")
            embeddings = tf.get_default_graph().get_tensor_by_name("embeddings:0")
            phase_train_placeholder = tf.get_default_graph().get_tensor_by_name("phase_train:0")
            # Run forward pass to calculate embeddings
            feed_dict = {images_placeholder: images, phase_train_placeholder: False}
            emb = sess.run(embeddings, feed_dict=feed_dict)
            print(emb[0])
    return []


def search(base64_image):
    base64_image = str(base64_image)
    strings_to_remove = ['b\'data:image/png;base64,', 'b\'data:image/jpg;base64,', 'b\'data:image/jpeg;base64,']
    for string in strings_to_remove:
        if base64_image.startswith(string):
            base64_image = base64_image[len(string):]
    image = Image.open(BytesIO(base64.b64decode(base64_image)))
    image_url = "image.jpg"
    image.save(image_url)
    embedding = infer(image_url)
