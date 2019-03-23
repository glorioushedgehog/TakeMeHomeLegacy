from django.db import models


class Person(models.Model):
    date_created = models.DateTimeField(db_column='Date Created', auto_now_add=True, null=True)
    date_modified = models.DateTimeField(db_column='Date Modified', auto_now=True, null=True)
    first_name = models.CharField(db_column='First Name', max_length=20, blank=True, null=True)
    middle_name = models.CharField(db_column='Middle Name', max_length=20, blank=True, null=True)
    last_name = models.CharField(db_column='Last Name', max_length=20, blank=True, null=True)
    name_to_call_me = models.CharField(db_column='Name to Call Me', max_length=20, blank=True, null=True)
    comments = models.TextField(db_column='Comments', blank=True, null=True)
    home_address = models.CharField(db_column='Home Address', max_length=40, blank=True, null=True)
    home_city = models.CharField(db_column='Home City', max_length=25, blank=True, null=True)
    home_state = models.CharField(db_column='Home State', max_length=2, blank=True, null=True)
    home_zip = models.CharField(db_column='Home Zip', max_length=10, blank=True, null=True)
    home_phone = models.CharField(db_column='Home Phone', max_length=13, blank=True, null=True)
    dob = models.DateTimeField(db_column='DOB', blank=True, null=True)
    dob_year = models.IntegerField(db_column='DOB_YEAR', blank=True, null=True)
    hair = models.CharField(db_column='Hair', max_length=10, blank=True, null=True)
    eyes = models.CharField(db_column='Eyes', max_length=10, blank=True, null=True)
    race = models.CharField(db_column='Race', max_length=1, blank=True, null=True)
    sex = models.CharField(db_column='Sex', max_length=1, blank=True, null=True)
    height = models.IntegerField(db_column='Height', blank=True, null=True)
    weight = models.IntegerField(db_column='Weight', blank=True, null=True)
    picture = models.BinaryField(db_column='Picture', blank=True, null=True)
    picture_date = models.DateTimeField(db_column='Picture Date', blank=True, null=True)
    emergency_contact_1_name = models.CharField(db_column='Emergency Contact 1 Name', max_length=30, blank=True,
                                                null=True)
    emergency_contact_1_phone = models.CharField(db_column='Emergency Contact 1 Phone', max_length=20, blank=True,
                                                 null=True)
    emergency_contact_1_relationship = models.CharField(db_column='Emergency Contact 1 Relationship', max_length=20,
                                                        blank=True,
                                                        null=True)
    emergency_contact_1_address = models.CharField(db_column='Emergency Contact 1 Address', max_length=50, blank=True,
                                                   null=True)
    emergency_contact_1_comments = models.TextField(db_column='Emergency Contact 1 Comments', blank=True,
                                                    null=True)
    emergency_contact_2_name = models.CharField(db_column='Emergency Contact 2 Name', max_length=30, blank=True,
                                                null=True)
    emergency_contact_2_phone = models.CharField(db_column='Emergency Contact 2 Phone', max_length=20, blank=True,
                                                 null=True)
    emergency_contact_2_relationship = models.CharField(db_column='Emergency Contact 2 Relationship', max_length=20,
                                                        blank=True,
                                                        null=True)
    emergency_contact_2_address = models.CharField(db_column='Emergency Contact 2 Address', max_length=50, blank=True,
                                                   null=True)
    emergency_contact_2_comments = models.TextField(db_column='Emergency Contact 2 Comments', blank=True,
                                                    null=True)
    emergency_contact_3_name = models.CharField(db_column='Emergency Contact 3 Name', max_length=30, blank=True,
                                                null=True)
    emergency_contact_3_phone = models.CharField(db_column='Emergency Contact 3 Phone', max_length=20, blank=True,
                                                 null=True)
    emergency_contact_3_relationship = models.CharField(db_column='Emergency Contact 3 Relationship', max_length=20,
                                                        blank=True,
                                                        null=True)
    emergency_contact_3_address = models.CharField(db_column='Emergency Contact 3 Address', max_length=50, blank=True,
                                                   null=True)
    emergency_contact_3_comments = models.TextField(db_column='Emergency Contact 3 Comments', blank=True,
                                                    null=True)
    emergency_contact_4_name = models.CharField(db_column='Emergency Contact 4 Name', max_length=30, blank=True,
                                                null=True)
    emergency_contact_4_phone = models.CharField(db_column='Emergency Contact 4 Phone', max_length=20, blank=True,
                                                 null=True)
    emergency_contact_4_relationship = models.CharField(db_column='Emergency Contact 4 Relationship', max_length=20,
                                                        blank=True,
                                                        null=True)
    emergency_contact_4_address = models.CharField(db_column='Emergency Contact 4 Address', max_length=50, blank=True,
                                                   null=True)
    emergency_contact_4_comments = models.TextField(db_column='Emergency Contact 4 Comments', blank=True,
                                                    null=True)
    emergency_contact_5_name = models.CharField(db_column='Emergency Contact 5 Name', max_length=30, blank=True,
                                                null=True)
    emergency_contact_5_phone = models.CharField(db_column='Emergency Contact 5 Phone', max_length=20, blank=True,
                                                 null=True)
    emergency_contact_5_relationship = models.CharField(db_column='Emergency Contact 5 Relationship', max_length=20,
                                                        blank=True,
                                                        null=True)
    emergency_contact_5_address = models.CharField(db_column='Emergency Contact 5 Address', max_length=50, blank=True,
                                                   null=True)
    emergency_contact_5_comments = models.TextField(db_column='Emergency Contact 5 Comments', blank=True,
                                                    null=True)
    organization = models.CharField(db_column='Organization', max_length=30, blank=True, null=True)
    record_type = models.CharField(db_column='Record Type', max_length=30, blank=True, null=True)
    braclet_id = models.CharField(db_column='Braclet ID', max_length=20, blank=True, null=True)
    emergency_contact_1_cphone = models.CharField(db_column='Emergency Contact 1 CPhone', max_length=20, blank=True,
                                                  null=True)
    emergency_contact_2_cphone = models.CharField(db_column='Emergency Contact 2 CPhone', max_length=20, blank=True,
                                                  null=True)
    emergency_contact_3_cphone = models.CharField(db_column='Emergency Contact 3 CPhone', max_length=20, blank=True,
                                                  null=True)
    emergency_contact_4_cphone = models.CharField(db_column='Emergency Contact 4 CPhone', max_length=20, blank=True,
                                                  null=True)
    emergency_contact_5_cphone = models.CharField(db_column='Emergency Contact 5 CPhone', max_length=20, blank=True,
                                                  null=True)
    primarykey = models.CharField(db_column='PrimaryKey', primary_key=True, max_length=22)

    class Meta:
        managed = False
        db_table = 'TAKEMEHOME'


class ImageData(models.Model):
    primarykey = models.CharField(db_column='PrimaryKey', primary_key=True, max_length=22)
    picture = models.ImageField(db_column='PictureURL', upload_to='tmh/static/images')
    embedding = models.TextField(db_column='Embedding', blank=True, null=True)

    class Meta:
        db_table = 'Image_Data'


class InferenceTask(models.Model):
    LOCATING_FACE = 'LOCATING_FACE'
    ANALYZING_FACE = 'ANALYZING_FACE'
    DONE = 'DONE'
    ERROR = 'ERROR'
    STATES = (
        (LOCATING_FACE, 'Locating face...'),
        (ANALYZING_FACE, 'Analyzing face...'),
        (DONE, 'Success!'),
        (ERROR, 'Something went wrong.'),
    )
    state = models.CharField(
        max_length=22,
        choices=STATES,
        default=LOCATING_FACE,
    )
    primarykey = models.CharField(db_column='PrimaryKey', max_length=22, blank=True, null=True)
    embedding = models.TextField(db_column='Embedding', blank=True, null=True)
    date_created = models.DateTimeField(db_column='Date Created', auto_now_add=True, null=True)

    class Meta:
        db_table = 'Inference_Task'


class CfgLookup(models.Model):
    choice = models.CharField(db_column='Choice', max_length=25, blank=True, null=True)
    description = models.CharField(db_column='Description', max_length=50, blank=True,
                                   null=True)
    typeid = models.IntegerField(db_column='TypeId', blank=True, null=True)
    uniquekey = models.CharField(db_column='UniqueKey', primary_key=True, max_length=22)

    class Meta:
        managed = False
        db_table = 'Cfg_Lookup'


class CfgType(models.Model):
    class Meta:
        managed = False
        db_table = 'Cfg_Type'
