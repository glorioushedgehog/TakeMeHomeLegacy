from tmh.models import Person

AGE_GUESS_MARGIN = 5


def weight_match(a_person, input_weight, attached_weight):
    """
    checks if a given weight is within the acceptable threshold
    :param input_weight: the weight of the search target
    :param attached_weight: the weight of the class
    :return: True if within the threshold, False otherwise
    """
    WEIGHT_THRESH = 30
    return attached_weight - WEIGHT_THRESH <= input_weight <= attached_weight + WEIGHT_THRESH


def height_match(a_person, input_height, attached_height):
    """
    checks if a given height is within the acceptable threshold
    :param input_height: the height of the search target
    :param attached_height: the height of the class
    :return: True if within the threshold, False otherwise
    """
    HEIGHT_THRESH = 3
    return attached_height - HEIGHT_THRESH <= input_height <= attached_height + HEIGHT_THRESH


def dob_match(a_person, input_dob, attached_dob):
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


def zip_match(a_person, input_zip, attached_zip):
    """
    checks if two zips are within a reasonable distance of one another
    :param input_zip: the zip given as a search term
    :param attached_zip: the zip in the class
    :return: True if within the zone, false otherwise
    """
    return input_zip == attached_zip


def string_alignment(a_person, str_one, str_two):
    """
    Checks alignment between two strings
    :param str_one: first string (the passed in search term)
    :param str_two: second string (the class name_field)
    :return: True if there is a 70% match, False otherwise
    """
    str1_len = len(str_one)
    str2_len = len(str_two)

    if not str1_len or not str2_len: return max(str1_len, str2_len)

    # # each entry is a row
    # matrix = [0] * (str2_len + 1)
    # for i in range(str2_len + 1):
    #     matrix[i] = [0] * (str1_len + 1)

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


def search(a_person, first_name="", last_name="", middle_name="", name_to_call_me="", home_city="", home_state="",
           home_zip="", dob="", dob_year="", hair="", eyes="", race="", sex="", height="", weight="", ):
    """
    returns a boolean based on if there is a match between the parameters and the instance's details
    :param first_name: the first name of the search target
    :param last_name: the last name of the search target
    :param middle_name: the middle name of the search target
    :param name_to_call_me: the nickname of the search target
    :param home_city: the home city of the search target
    :param home_state: the home state of the search target
    :param home_zip: the home zip of the search target
    :param dob: the date of birth of the search target
    :param dob_year: the date of birth year of the search target
    :param hair: the hair color of the search target
    :param eyes: the eye color of the search target
    :param race: the race/ethnicity of the search target
    :param sex: the sex of the search target
    :param height: the approximate height of the search target
    :param weight: the weight of the search target
    :return: True if over 75% of the search terms match (to all given paramas), false otherwise
    """
    total = 0
    correct = 0
    if first_name != "":
        if string_alignment(a_person, first_name, a_person.first_name):
            correct += 1
            print("first_name correct")
        total += 1
    if last_name != "":
        if string_alignment(a_person, last_name, a_person.last_name):
            correct += 1
        total += 1
    if middle_name != "":
        if string_alignment(a_person, middle_name, a_person.middle_name):
            correct += 1
        total += 1
    if name_to_call_me != "":
        if string_alignment(a_person, name_to_call_me, a_person.name_to_call_me):
            correct += 1
        total += 1
    if home_city != "":
        if home_city.strip() == a_person.home_city:
            correct += 1
        total += 1
    if home_state != "":
        if home_state == a_person.home_state:
            correct += 1
        total += 1
    if home_zip != "":
        if zip_match(a_person, home_zip, a_person.home_zip):
            correct += 1
        total += 1
    if dob != "":
        if dob_match(a_person, dob, a_person.dob):
            correct += 1
        total += 1
    if dob_year != "":
        if a_person.dob_year - AGE_GUESS_MARGIN <= dob_year <= a_person.dob_year + AGE_GUESS_MARGIN:
            correct += 1
        total += 1
    if hair != "":
        if hair == a_person.hair:
            correct += 1
        total += 1
    if eyes != "":
        if eyes == a_person.eyes:
            correct += 1
        total += 1
    if race != "":
        if race == a_person.race:
            correct += 1
        total += 1
    if sex != "":
        if sex == a_person.sex:
            correct += 1
        total += 1
    if height != "":
        if height_match(a_person, height, a_person.height):
            correct += 1
        total += 1
    if weight != "":
        if weight_match(a_person, weight, a_person.weight):
            correct += 1
        total += 1
    print(a_person.first_name, a_person.last_name, correct / total)
    if correct / total >= 0.5:
        return True
    else:
        return False


def get_matching_persons(search_params):
    people = Person.objects.all()
    first_name = ""
    last_name = ""
    middle_name = ""
    name_to_call_me = ""
    home_city = ""
    home_state = ""
    home_zip = ""
    dob = ""
    dob_year = ""
    hair = ""
    eyes = ""
    race = ""
    sex = ""
    height = ""
    weight = ""
    remove_list = []
    for entry in search_params:
        if search_params[entry] is None:
            remove_list.append(entry)
    for entry in remove_list:
        search_params.pop(entry, None)
    if "first_name" in search_params:
        first_name = search_params["first_name"]
    if "last_name" in search_params:
        last_name = search_params["last_name"]
    if "middle_name" in search_params:
        middle_name = search_params["middle_name"]
    if "name_to_call_me" in search_params:
        name_to_call_me = search_params["name_to_call_me"]
    if "home_city" in search_params:
        home_city = search_params["home_city"]
    if "home_state" in search_params:
        home_state = search_params["home_state"]
    if "home_zip" in search_params:
        home_zip = search_params["home_zip"]
    if "dob" in search_params:
        dob = search_params["dob"]
    if "dob_year" in search_params:
        dob_year = search_params["dob_year"]
    if "hair" in search_params:
        hair = search_params["hair"]
    if "eyes" in search_params:
        eyes = search_params["eyes"]
    if "race" in search_params:
        race = search_params["race"]
    if "sex" in search_params:
        sex = search_params["sex"]
    if "height" in search_params:
        height = search_params["height"]
    if "weight" in search_params:
        weight = search_params["weight"]

    persons = []
    for peep in people:
        if search(peep, first_name, last_name, middle_name, name_to_call_me, home_city,
                  home_state, home_zip, dob, dob_year, hair, eyes, race, sex, height,
                  weight):
            persons.append(peep)
    return persons
