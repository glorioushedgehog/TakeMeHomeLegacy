from math import ceil

from tmh.models import ImageData


def context_from_person_list(persons):
    large_row_size = 4
    medium_row_size = 2
    persons_by_large_row = []
    for i in range(ceil(len(persons) / large_row_size)):
        a_row = []
        for j in range(large_row_size):
            if i * large_row_size + j >= len(persons):
                break
            a_row.append(persons[i * large_row_size + j])
        persons_by_large_row.append(a_row)

    persons_by_medium_row = []
    for i in range(ceil(len(persons) / medium_row_size)):
        a_row = []
        for j in range(medium_row_size):
            if i * medium_row_size + j >= len(persons):
                break
            a_row.append(persons[i * medium_row_size + j])
        persons_by_medium_row.append(a_row)

    images = ImageData.objects.none()
    for individual in persons:
        an_id = individual.primarykey
        new_query_set = ImageData.objects.filter(primarykey=an_id)
        images = images.union(new_query_set)
    context = {
        'persons': persons,
        'persons_by_large_row': persons_by_large_row,
        'persons_by_medium_row': persons_by_medium_row,
        'images': images
    }
    return context
