from math import ceil
import time


def grid_of_persons(persons):
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

    context = {
        'persons': persons,
        'persons_by_large_col': persons_by_large_col,
        'persons_by_medium_col': persons_by_medium_col,
    }
    return context


def facial_recognition_coverage(people):
    num_with_imagedata = 0
    num_without_imagedata = 0
    num_ready_for_fr = 0
    num_not_ready_for_fr = 0
    for a_person in people:
        if hasattr(a_person, 'imagedata'):
            num_with_imagedata += 1
            if a_person.imagedata.embedding is not None:
                num_ready_for_fr += 1
            else:
                num_not_ready_for_fr += 1
        else:
            num_without_imagedata += 1
            num_not_ready_for_fr += 1
    num_persons = people.count()
    if num_persons > 0:
        imagedata_percentage = str((num_with_imagedata * 100) // num_persons) + "%"
        fr_ready_percentage = str((num_ready_for_fr * 100) // num_persons) + "%"
    else:
        imagedata_percentage = "0%"
        fr_ready_percentage = "0%"
    context = {
        'num_persons': num_persons,
        'num_with_imagedata': num_with_imagedata,
        'num_without_imagedata': num_without_imagedata,
        'imagedata_percentage': imagedata_percentage,
        'num_ready_for_fr': num_ready_for_fr,
        'num_not_ready_for_fr': num_not_ready_for_fr,
        'fr_ready_percentage': fr_ready_percentage,
    }
    return context


def person_details_context(a_person):
    age = None
    if a_person.dob is not None:
        age_in_seconds = time.time() - a_person.dob.timestamp()
        seconds_in_year = 60 * 60 * 24 * 360
        age = int(age_in_seconds) // seconds_in_year
    context = {'person': a_person, 'age': age}
    return context
