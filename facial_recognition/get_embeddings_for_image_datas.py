from facial_recognition.get_multiple_embeddings import get_embeddings
from tmh.models import ImageData


def generate_embeddings():
    paths = []
    image_datas = ImageData.objects.all()
    for image_data in image_datas:
        paths.append(image_data.picture.url)
    embeddings = get_embeddings(paths)
    i = 0
    for image_data in image_datas:
        string_embedding = ''
        for e in embeddings[i]:
            string_embedding += str(e) + ','
        string_embedding = string_embedding[:-1]
        image_data.embedding = string_embedding
        image_data.save()
        i += 1
