# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Person(models.Model):
    date_created = models.DateTimeField(db_column='Date Created', blank=True,
                                        null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_modified = models.DateTimeField(db_column='Date Modified', blank=True,
                                         null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    first_name = models.CharField(db_column='First Name', max_length=20, blank=True,
                                  null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    middle_name = models.CharField(db_column='Middle Name', max_length=20, blank=True,
                                   null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_name = models.CharField(db_column='Last Name', max_length=20, blank=True,
                                 null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    name_to_call_me = models.CharField(db_column='Name to Call Me', max_length=20, blank=True,
                                       null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.
    home_address = models.CharField(db_column='Home Address', max_length=40, blank=True,
                                    null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    home_city = models.CharField(db_column='Home City', max_length=25, blank=True,
                                 null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    home_state = models.CharField(db_column='Home State', max_length=2, blank=True,
                                  null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    home_zip = models.CharField(db_column='Home Zip', max_length=10, blank=True,
                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    home_phone = models.CharField(db_column='Home Phone', max_length=13, blank=True,
                                  null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dob = models.DateTimeField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    dob_year = models.IntegerField(db_column='DOB_YEAR', blank=True, null=True)  # Field name made lowercase.
    hair = models.CharField(db_column='Hair', max_length=10, blank=True, null=True)  # Field name made lowercase.
    eyes = models.CharField(db_column='Eyes', max_length=10, blank=True, null=True)  # Field name made lowercase.
    race = models.CharField(db_column='Race', max_length=1, blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='Sex', max_length=1, blank=True, null=True)  # Field name made lowercase.
    height = models.IntegerField(db_column='Height', blank=True, null=True)  # Field name made lowercase.
    weight = models.IntegerField(db_column='Weight', blank=True, null=True)  # Field name made lowercase.
    picture = models.BinaryField(db_column='Picture', blank=True, null=True)  # Field name made lowercase.
    picture_date = models.DateTimeField(db_column='Picture Date', blank=True,
                                        null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    emergency_contact_1_name = models.CharField(db_column='Emergency Contact 1 Name', max_length=30, blank=True,
                                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    emergency_contact_1_phone = models.CharField(db_column='Emergency Contact 1 Phone', max_length=20, blank=True,
                                                 null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    emergency_contact_1_relationship = models.CharField(db_column='Emergency Contact 1 Relationship', max_length=20,
                                                        blank=True,
                                                        null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    emergency_contact_1_address = models.CharField(db_column='Emergency Contact 1 Address', max_length=50, blank=True,
                                                   null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    emergency_contact_1_comments = models.TextField(db_column='Emergency Contact 1 Comments', blank=True,
                                                    null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    emergency_contact_2_name = models.CharField(db_column='Emergency Contact 2 Name', max_length=30, blank=True,
                                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    emergency_contact_2_phone = models.CharField(db_column='Emergency Contact 2 Phone', max_length=20, blank=True,
                                                 null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    emergency_contact_2_relationship = models.CharField(db_column='Emergency Contact 2 Relationship', max_length=20,
                                                        blank=True,
                                                        null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    emergency_contact_2_address = models.CharField(db_column='Emergency Contact 2 Address', max_length=50, blank=True,
                                                   null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    emergency_contact_2_comments = models.TextField(db_column='Emergency Contact 2 Comments', blank=True,
                                                    null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    emergency_contact_3_name = models.CharField(db_column='Emergency Contact 3 Name', max_length=30, blank=True,
                                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    emergency_contact_3_phone = models.CharField(db_column='Emergency Contact 3 Phone', max_length=20, blank=True,
                                                 null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    emergency_contact_3_relationship = models.CharField(db_column='Emergency Contact 3 Relationship', max_length=20,
                                                        blank=True,
                                                        null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    emergency_contact_3_address = models.CharField(db_column='Emergency Contact 3 Address', max_length=50, blank=True,
                                                   null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    emergency_contact_3_comments = models.TextField(db_column='Emergency Contact 3 Comments', blank=True,
                                                    null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    emergency_contact_4_name = models.CharField(db_column='Emergency Contact 4 Name', max_length=30, blank=True,
                                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    emergency_contact_4_phone = models.CharField(db_column='Emergency Contact 4 Phone', max_length=20, blank=True,
                                                 null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    emergency_contact_4_relationship = models.CharField(db_column='Emergency Contact 4 Relationship', max_length=20,
                                                        blank=True,
                                                        null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    emergency_contact_4_address = models.CharField(db_column='Emergency Contact 4 Address', max_length=50, blank=True,
                                                   null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    emergency_contact_4_comments = models.TextField(db_column='Emergency Contact 4 Comments', blank=True,
                                                    null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    emergency_contact_5_name = models.CharField(db_column='Emergency Contact 5 Name', max_length=30, blank=True,
                                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    emergency_contact_5_phone = models.CharField(db_column='Emergency Contact 5 Phone', max_length=20, blank=True,
                                                 null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    emergency_contact_5_relationship = models.CharField(db_column='Emergency Contact 5 Relationship', max_length=20,
                                                        blank=True,
                                                        null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    emergency_contact_5_address = models.CharField(db_column='Emergency Contact 5 Address', max_length=50, blank=True,
                                                   null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    emergency_contact_5_comments = models.TextField(db_column='Emergency Contact 5 Comments', blank=True,
                                                    null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization = models.CharField(db_column='Organization', max_length=30, blank=True,
                                    null=True)  # Field name made lowercase.
    record_type = models.CharField(db_column='Record Type', max_length=30, blank=True,
                                   null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    braclet_id = models.CharField(db_column='Braclet ID', max_length=20, blank=True,
                                  null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    emergency_contact_1_cphone = models.CharField(db_column='Emergency Contact 1 CPhone', max_length=20, blank=True,
                                                  null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    emergency_contact_2_cphone = models.CharField(db_column='Emergency Contact 2 CPhone', max_length=20, blank=True,
                                                  null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    emergency_contact_3_cphone = models.CharField(db_column='Emergency Contact 3 CPhone', max_length=20, blank=True,
                                                  null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    emergency_contact_4_cphone = models.CharField(db_column='Emergency Contact 4 CPhone', max_length=20, blank=True,
                                                  null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    emergency_contact_5_cphone = models.CharField(db_column='Emergency Contact 5 CPhone', max_length=20, blank=True,
                                                  null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    primarykey = models.CharField(db_column='PrimaryKey', primary_key=True, max_length=22)  # Field name made lowercase.

    def search(self, first_name="", last_name="", middle_name="", name_to_call_me ="", home_city="", home_state="",
               home_zip="", dob="", dob_year="", hair="", eyes="", race="", sex="", height="", weight="",):
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
        YEAR_THRESH = 5
        total = 0
        correct = 0
        if first_name != "":
            if self.stringAlignment(first_name, self.first_name):
                correct += 1
            total += 1
        if last_name != "":
            if self.stringAlignment(last_name, self.last_name):
                correct += 1
            total += 1
        if middle_name != "":
            if self.stringAlignment(middle_name, self.middle_name):
                correct += 1
            total += 1
        if name_to_call_me != "":
            if self.stringAlignment(name_to_call_me, self.name_to_call_me):
                correct += 1
            total += 1
        if home_city != "":
            if home_city != self.home_city:
                correct += 1
            total += 1
        if home_state != "":
            if home_state != self.home_state:
                correct += 1
            total += 1
        if home_zip != "":
            if self.zipMatch(home_zip, self.home_zip):
                correct += 1
            total += 1
        if dob != "":
            if self.dobMatch(dob, self.dob):
                correct += 1
            total += 1
        if dob_year != "":
            if self.dob_year - YEAR_THRESH <= dob_year <= self.dob_year + YEAR_THRESH:
                correct += 1
            total += 1
        if hair != "":
            if hair == self.hair:
                correct += 1
            total += 1
        if eyes != "":
            if eyes == self.eyes:
                correct += 1
            total += 1
        if race != "":
            if race == self.race:
                correct += 1
            total += 1
        if sex != "":
            if sex == self.sex:
                correct += 1
            total += 1
        if height != "":
            if self.heightMatch(height, self.height):
                correct += 1
            total += 1
        if weight != "":
            if self.weightMatch(weight, self.weight):
                correct += 1
            total += 1
        print(self.first_name, self.last_name, correct/total)
        if correct/total >= 0.6:
            return True
        else:
            return False

    def weightMatch(self, input_weight, attached_weight):
        """
        checks if a given weight is within the acceptable threshold
        :param input_weight: the weight of the search target
        :param attached_weight: the weight of the class
        :return: True if within the threshold, False otherwise
        """
        WEIGHT_THRESH = 30
        return attached_weight - WEIGHT_THRESH <= input_weight <= attached_weight + WEIGHT_THRESH

    def heightMatch(self, input_height, attached_height):
        """
        checks if a given height is within the acceptable threshold
        :param input_height: the height of the search target
        :param attached_height: the height of the class
        :return: True if within the threshold, False otherwise
        """
        HEIGHT_THRESH = 3
        return attached_height - HEIGHT_THRESH <= input_height <= attached_height + HEIGHT_THRESH

    def dobMatch(self, input_dob, attached_dob):
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


    def zipMatch(self, input_zip, attached_zip):
        """
        checks if two zips are within a reasonable distance of one another
        :param input_zip: the zip given as a search term
        :param attached_zip: the zip in the class
        :return: True if within the zone, false otherwise
        """
        return input_zip == attached_zip

    def stringAlignment(self, str_one, str_two):
        """
        Checks alignment between two strings
        :param str_one: first string (the passed in search term)
        :param str_two: second string (the class name_field)
        :return: True if there is a 70% match, False otherwise
        """
        str1_len = len(str_one)
        str2_len = len(str_two)

        if not str1_len or not str2_len: return max(str1_len, str2_len)

        # each entry is a row
        matrix = [0] * (str2_len + 1)
        for i in range(str2_len + 1):
            matrix[i] = [0] * (str1_len + 1)

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


    class Meta:
        #  managed = False
        db_table = 'TAKEMEHOME'


class ImageData(models.Model):
    primarykey = models.CharField(db_column='PrimaryKey', max_length=22)
    picture = models.ImageField(db_column='PictureURL', upload_to='tmh/static')
    embedding = models.TextField(db_column='Embedding', blank=True, null=True)

    class Meta:
        db_table = 'Image_Data'


class CfgLookup(models.Model):
    choice = models.CharField(db_column='Choice', max_length=25, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, blank=True,
                                   null=True)  # Field name made lowercase.
    typeid = models.IntegerField(db_column='TypeId', blank=True, null=True)  # Field name made lowercase.
    uniquekey = models.CharField(db_column='UniqueKey', primary_key=True, max_length=22)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cfg_Lookup'


class CfgType(models.Model):
    class Meta:
        managed = False
        db_table = 'Cfg_Type'
