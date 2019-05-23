# MIT License
#
# Copyright (c) 2016 David Sandberg
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# pylint: disable=missing-docstring
import os
import tensorflow as tf
import numpy as np
from PIL import Image

from facial_recognition import detect_face, facenet


def get_alignment_mtcnn():
    with tf.Graph().as_default():
        gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=1.0)
        sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options, log_device_placement=False))
        with sess.as_default():
            pnet, rnet, onet = detect_face.create_mtcnn(sess, None)
    return pnet, rnet, onet


def get_bounding_boxes(img, mtcnn):
    minsize = 20  # minimum size of face
    threshold = [0.6, 0.7, 0.7]  # three steps's threshold
    factor = 0.709  # scale factor
    img_size = np.asarray(img.shape)[0:2]
    bounding_boxes, _ = detect_face.detect_face(img, minsize, mtcnn[0], mtcnn[1], mtcnn[2], threshold, factor)
    return bounding_boxes, img_size


def single_image_bounding_boxes(img):
    mtcnn = get_alignment_mtcnn()
    return get_bounding_boxes(img, mtcnn)


def crop_image(img, bounding_boxes, img_size):
    margin = 44
    image_size = 160
    det = np.squeeze(bounding_boxes[0, 0:4])
    bb = np.zeros(4, dtype=np.int32)
    bb[0] = np.maximum(det[0] - margin / 2, 0)
    bb[1] = np.maximum(det[1] - margin / 2, 0)
    bb[2] = np.minimum(det[2] + margin / 2, img_size[1])
    bb[3] = np.minimum(det[3] + margin / 2, img_size[0])
    cropped = img[bb[1]:bb[3], bb[0]:bb[2], :]
    aligned = np.array(Image.fromarray(cropped).resize((image_size, image_size)))
    prewhitened = facenet.prewhiten(aligned)
    return prewhitened


def get_embeddings(images):
    batch_size = 100
    batches = []
    for i in range(0, len(images), batch_size):
        batches.append(images[i:i + batch_size])
    embeddings = []
    if not images:
        return embeddings
    with tf.Graph().as_default():
        with tf.Session() as sess:
            # Load the model
            facenet.load_model(os.path.join("facial_recognition", "model.pb"))
            # Get input and output tensors
            images_placeholder = tf.get_default_graph().get_tensor_by_name("input:0")
            embeddings_tensor = tf.get_default_graph().get_tensor_by_name("embeddings:0")
            phase_train_placeholder = tf.get_default_graph().get_tensor_by_name("phase_train:0")
            images_done = 0
            for batch in batches:
                # Run forward pass to calculate embeddings
                feed_dict = {images_placeholder: np.stack(batch), phase_train_placeholder: False}
                emb = sess.run(embeddings_tensor, feed_dict=feed_dict)
                for e in emb:
                    embeddings.append(e)
                images_done += len(batch)
                print("images embedded:", images_done)
    return embeddings
