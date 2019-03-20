from math import ceil

from tmh.models import ImageData


def context_from_person_list(persons):
    persons = persons * 5
    large_row_size = 4
    medium_row_size = 2

    persons_by_large_col = []
    for _ in range(large_row_size):
        persons_by_large_col.append([])
    for i in range(ceil(len(persons) / large_row_size)):
        for j in range(large_row_size):
            an_index = i * large_row_size + j
            if an_index >= len(persons):
                break
            persons_by_large_col[j].append(persons[an_index])

    persons_by_medium_col = []
    for _ in range(medium_row_size):
        persons_by_medium_col.append([])
    for i in range(ceil(len(persons) / medium_row_size)):
        for j in range(medium_row_size):
            an_index = i * medium_row_size + j
            if an_index >= len(persons):
                break
            persons_by_medium_col[j].append(persons[an_index])

    for individual in persons:
        an_id = individual.primarykey
        if ImageData.objects.filter(pk=an_id).exists():
            an_image_data = ImageData.objects.get(pk=an_id)
            if an_image_data.picture is not None:
                individual.image_url = an_image_data.picture.url
    context = {
        'persons': persons,
        'persons_by_large_col': persons_by_large_col,
        'persons_by_medium_col': persons_by_medium_col,
    }
    return context
