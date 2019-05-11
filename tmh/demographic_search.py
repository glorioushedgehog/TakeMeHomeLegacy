from tmh.models import Person


def weight_match(input_weight, attached_weight):
    """
    checks if a given weight is within the acceptable threshold
    :param input_weight: the weight of the search target
    :param attached_weight: the weight of the class
    :return: True if within the threshold, False otherwise
    """
    WEIGHT_THRESH = 30
    return attached_weight - WEIGHT_THRESH <= input_weight <= attached_weight + WEIGHT_THRESH


def height_match(input_height, attached_height):
    """
    checks if a given height is within the acceptable threshold
    :param input_height: the height of the search target
    :param attached_height: the height of the class
    :return: True if within the threshold, False otherwise
    """
    HEIGHT_THRESH = 3
    return attached_height - HEIGHT_THRESH <= input_height <= attached_height + HEIGHT_THRESH


def dob_match(input_dob, attached_dob):
    """
    returns true if some fields match, false otherwise
    :param input_dob: the search dob
    :param attached_dob: the class dob
    :return: True if a match is determined, False otherwise
    """
    YEAR_THRESH = 5
    if input_dob.day != attached_dob.day:
        return False
    if input_dob.month != attached_dob.month:
        return False
    if not attached_dob.year - YEAR_THRESH <= input_dob.year <= attached_dob.year + YEAR_THRESH:
        return False
    return True


def zip_match(input_zip, attached_zip):
    """
    checks if two zips are within a reasonable distance of one another
    :param input_zip: the zip given as a search term
    :param attached_zip: the zip in the class
    :return: True if within the zone, false otherwise
    """
    return input_zip == attached_zip


def dob_year_match(input_dob_year, attached_dob_year):
    AGE_GUESS_MARGIN = 5
    return attached_dob_year - AGE_GUESS_MARGIN <= input_dob_year <= attached_dob_year + AGE_GUESS_MARGIN


def string_alignment(str_one, str_two):
    """
    Checks alignment between two strings
    :param str_one: first string (the passed in search term)
    :param str_two: second string (the class name_field)
    :return: True if there is a 70% match, False otherwise
    """
    str1_len = len(str_one)
    str2_len = len(str_two)

    # this is an n-squared algorithm, so check n-squared
    # and demand total (case-insensitive) equality for large big-O's
    if str1_len * str2_len > 10000:
        return str_one.lower() == str_two.lower()

    if not str1_len or not str2_len:
        return max(str1_len, str2_len)

    matrix = []
    for _ in range(str2_len + 1):
        temp = []
        for _ in range(str1_len + 1):
            temp.append(0)
        matrix.append(temp)

    for i in range(str1_len + 1):
        matrix[0][i] = i

    for i in range(str2_len + 1):
        matrix[i][0] = i

    for j in range(1, str1_len + 1):
        for i in range(1, str2_len + 1):
            cost = 0
            if str_one[j - 1].lower() != str_two[i - 1].lower():
                cost += 1
            above = matrix[i - 1][j] + 1
            left = matrix[i][j - 1] + 1
            diag = matrix[i - 1][j - 1] + cost
            matrix[i][j] = min(above, left, diag)

    val = matrix[str2_len - 1][str1_len - 1]
    if val / str2_len <= 0.3:
        return True
    return False


def match_percentage(a_person, search_params):
    """
    tells if there is a match between the parameters and a person
    :param a_person: the person being checked
    :param search_params: the values the user entered into demographic search
    :return: True if over 75% of the search terms match (to all given params), false otherwise
    """

    total = 0
    correct = 0
    # Demographics
    if search_params['dob_year'] is not None and a_person.dob_year is not None:
        if dob_year_match(search_params['dob_year'], a_person.dob_year):
            correct += 1
        total += 1
    if search_params['height'] is not None and a_person.height is not None:
        if height_match(search_params['height'], a_person.height):
            correct += 1
        total += 1
    if search_params['weight'] is not None and a_person.weight is not None:
        if weight_match(search_params['weight'], a_person.weight):
            correct += 1
        total += 1
    if search_params['sex'] is not None and a_person.sex is not None:
        if search_params['sex'] == a_person.sex:
            correct += 1
        total += 1
    if search_params['hair'] is not None and a_person.hair is not None:
        if search_params['hair'] == a_person.hair:
            correct += 1
        total += 1
    if search_params['eyes'] is not None and a_person.eyes is not None:
        if search_params['eyes'] == a_person.eyes:
            correct += 1
        total += 1
    if search_params['race'] is not None and a_person.race is not None:
        if search_params['race'] == a_person.race:
            correct += 1
        total += 1
    # Name
    if search_params['last_name'] is not None and a_person.last_name is not None:
        if string_alignment(search_params['last_name'], a_person.last_name):
            correct += 1
        total += 1
    if search_params['first_name'] is not None and a_person.first_name is not None:
        if string_alignment(search_params['first_name'], a_person.first_name):
            correct += 1
        total += 1
    if search_params['middle_name'] is not None and a_person.middle_name is not None:
        if string_alignment(search_params['middle_name'], a_person.middle_name):
            correct += 1
        total += 1
    if search_params['name_to_call_me'] is not None and a_person.name_to_call_me is not None:
        if string_alignment(search_params['name_to_call_me'], a_person.name_to_call_me):
            correct += 1
        total += 1
    # Type / Organization
    if search_params['braclet_id'] is not None and a_person.braclet_id is not None:
        if string_alignment(search_params['braclet_id'], a_person.braclet_id):
            correct += 1
        total += 1
    if search_params['record_type'] is not None and a_person.record_type is not None:
        if search_params['record_type'] == a_person.record_type:
            correct += 1
        total += 1
    if search_params['organization'] is not None and a_person.organization is not None:
        if search_params['organization'] == a_person.organization:
            correct += 1
        total += 1
    # Address / Phone
    if search_params['home_address'] is not None and a_person.home_address is not None:
        if string_alignment(search_params['home_address'], a_person.home_address):
            correct += 1
        total += 1
    if search_params['home_city'] is not None and a_person.home_city is not None:
        if string_alignment(search_params['home_city'], a_person.home_city):
            correct += 1
        total += 1
    if search_params['home_state'] is not None and a_person.home_state is not None:
        if search_params['home_state'] == a_person.home_state:
            correct += 1
        total += 1
    if search_params['home_zip'] is not None and a_person.home_zip is not None:
        if zip_match(search_params['home_zip'], a_person.home_zip):
            correct += 1
        total += 1
    if search_params['home_phone'] is not None and a_person.home_phone is not None:
        if string_alignment(search_params['home_phone'], a_person.home_phone):
            correct += 1
        total += 1

    if total == 0:
        return 0
    return correct / total


def get_matching_persons(search_params):
    MATCH_THRESHOLD = 0.5
    MAX_NUM_RESULTS = 20
    people = Person.objects.all()
    match_scores = [match_percentage(a_person, search_params) for a_person in people]
    indices_sorted_by_score = list(range(len(match_scores)))
    indices_sorted_by_score.sort(key=lambda i: match_scores[i], reverse=True)
    matching_people = []
    for index in indices_sorted_by_score:
        if len(matching_people) >= MAX_NUM_RESULTS:
            break
        if match_scores[index] >= MATCH_THRESHOLD:
            matching_people.append(people[index])
        else:
            break
    return matching_people
