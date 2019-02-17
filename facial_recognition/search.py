import numpy as np
from PIL import Image
from io import BytesIO
import base64

#from facial_recognition import detect_face, facenet


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

    # img = imageio.imread(os.path.expanduser(image), pilmode='RGB')
    img_size = np.asarray(image.shape)[0:2]
    bounding_boxes, _ = detect_face.detect_face(image, minsize, pnet, rnet, onet, threshold, factor)
    if len(bounding_boxes) < 1:
        print("can't detect face, remove ", image)
        return None
    det = np.squeeze(bounding_boxes[0, 0:4])
    bb = np.zeros(4, dtype=np.int32)
    bb[0] = np.maximum(det[0] - margin / 2, 0)
    bb[1] = np.maximum(det[1] - margin / 2, 0)
    bb[2] = np.minimum(det[2] + margin / 2, img_size[1])
    bb[3] = np.minimum(det[3] + margin / 2, img_size[0])
    cropped = image[bb[1]:bb[3], bb[0]:bb[2], :]
    # aligned = misc.imresize(cropped, (image_size, image_size), interp='bilinear')

    aligned = np.array(Image.fromarray(cropped).resize((image_size, image_size)))
    prewhitened = facenet.prewhiten(aligned)

    return []


def search(base64_image):
    print(base64_image)
    image = Image.open(BytesIO(base64.b64decode(base64_image)))
    image.save("test.jpg")
    #embedding = infer(image)
