from django.db import models


class Person(models.Model):
    EYES_CHOICES = (
        ('BLACK', 'BLACK'),
        ('BLUE', 'BLUE'),
        ('BROWN', 'BROWN'),
        ('GREEN', 'GREEN'),
        ('HAZEL', 'HAZEL'),
        ('OTHER', 'OTHER'),
    )
    HAIR_CHOICES = (
        ('BALD', 'BALD'),
        ('BLACK', 'BLACK'),
        ('BLONDE', 'BLONDE'),
        ('BLONDISH', 'BLONDISH'),
        ('BLUE', 'BLUE'),
        ('BROWN', 'BROWN'),
        ('BROWN RED', 'BROWN RED'),
        ('GRAY', 'GRAY'),
        ('GREEN', 'GREEN'),
        ('OTHER', 'OTHER'),
        ('PURPLE', 'PURPLE'),
        ('RED', 'RED'),
        ('SALT & PEP', 'SALT & PEP'),
        ('STRBRY BLD', 'STRBRY BLD'),
    )
    ORGANIZATION_CHOICES = (
        ('ALZHEIMERS', 'ALZHEIMERS'),
        ('ARC', 'ARC'),
        ('AUTISTIC FOUNDATION', 'AUTISTIC FOUNDATION'),
        ('BLIND', 'BLIND'),
        ('CARD', 'CARD'),
        ('COMMUNITY EXPERIENCES', 'COMMUNITY EXPERIENCES'),
        ('COUNCIL ON AGING', 'COUNCIL ON AGING'),
        ('D.D.', 'D.D.'),
        ('DEAF & HARD OF HEARING', 'DEAF & HARD OF HEARING'),
        ('DEVELOPMENTAL SERVICES', 'DEVELOPMENTAL SERVICES'),
        ('MENTALLY DISABLED', 'MENTALLY DISABLED'),
        ('OTHER', 'OTHER'),
        ('UNITED CEREBRAL PALSY', 'UNITED CEREBRAL PALSY'),
        ('WEST GATE SCHOOL', 'WEST GATE SCHOOL'),
    )
    RACE_CHOICES = (
        ('A', 'ASIAN'),
        ('B', 'AFRICAN AMERICAN'),
        ('BR', 'BI-RACIAL'),
        ('H', 'HISPANIC'),
        ('O', 'OTHER'),
        ('P', 'PACIFIC ISLANDER'),
        ('W', 'WHITE NON-HISPANIC'),
    )
    RECORD_TYPE_CHOICES = (
        ('ADHD & MENTALLY DISABLED', 'ADHD & MENTALLY DISABLED'),
        ('ALZHEIMER PATIENT', 'ALZHEIMER PATIENT'),
        ('AUTISTIC', 'AUTISTIC'),
        ('AUTISTIC & CEREBRAL PALSY', 'AUTISTIC & CEREBRAL PALSY'),
        ('AUTISTIC & DOWN SYNDROME', 'AUTISTIC & DOWN SYNDROME'),
        ('AUTISTIC & MENTALLY DISAB', 'AUTISTIC & MENTALLY DISABLED'),
        ('BLIND', 'BLIND'),
        ('BRAIN TUMOR', 'BRAIN TUMOR'),
        ('CEREBRAL PALSY', 'CEREBRAL PALSY'),
        ('DOWN SYNDROME', 'DOWN SYNDROME'),
        ('EPILEPSY & MENTALLY DISAB', 'EPILEPSY & MENTALLY DISABLED'),
        ('HYPOTONIC CEREBRAL PALSY', 'HYPOTONIC CEREBRAL PALSY'),
        ('MENTALLY HANDICAPPED', 'MENTALLY HANDICAPPED'),
        ('OTHER', 'OTHER'),
        ('PLASTIC STOMACH', 'PLASTIC STOMACH'),
        ('SPECIAL NEEDS', 'SPECIAL NEEDS'),
        ('TAY-SACHS DIS/NON-VBL,AMB', 'TAY-SACHS DIS/NON-VBL,AMBLITOR'),
    )
    EMERGENCY_CONTACT_RELATIONSHIP_CHOICES = (
        ('AUNT', 'AUNT'),
        ('AUNT & UNCLE', 'AUNT & UNCLE'),
        ('BABY SITTER', 'BABY SITTER'),
        ('BROTHER', 'BROTHER'),
        ('CAREGIVER', 'CAREGIVER'),
        ('COUSIN', 'COUSIN'),
        ('DAUGHTER', 'DAUGHTER'),
        ('DAY CARE PROVIDER', 'DAY CARE PROVIDER'),
        ('FATHER', 'FATHER'),
        ('FOSTER PARENT(S)', 'FOSTER PARENT(S)'),
        ('FRIEND', 'FRIEND'),
        ('GOD PARENTS', 'GOD PARENTS'),
        ('GRANDFATHER', 'GRANDFATHER'),
        ('GRANDMOTHER', 'GRANDMOTHER'),
        ('GRANDPARENTS', 'GRANDPARENTS'),
        ('GREAT AUNT', 'GREAT AUNT'),
        ('GREAT GRANDPARENT', 'GREAT GRANDPARENT'),
        ('GROUP HOME MANAGER', 'GROUP HOME MANAGER'),
        ('HUSBAND', 'HUSBAND'),
        ('IN-LAW', 'IN-LAW'),
        ('LEGAL GUARDIAN', 'LEGAL GUARDIAN'),
        ('MOTHER', 'MOTHER'),
        ('NEIGHBOR', 'NEIGHBOR'),
        ('NEPHEW', 'NEPHEW'),
        ('NIECE', 'NIECE'),
        ('OTHER', 'OTHER'),
        ('PARENTS', 'PARENTS'),
        ('SISTER', 'SISTER'),
        ('SON', 'SON'),
        ('STEP-FATHER', 'STEP-FATHER'),
        ('STEP-MOTHER', 'STEP-MOTHER'),
        ('SUPERVISOR', 'SUPERVISOR'),
        ('THERAPIST', 'THERAPIST'),
        ('UNCLE', 'UNCLE'),
        ('WIFE', 'WIFE'),
    )
    SEX_CHOICES = (
        ('F', 'FEMALE'),
        ('M', 'MALE'),
    )
    HOME_STATE_CHOICES = (
        ('AK', 'ALASKA'),
        ('AL', 'ALABAMA'),
        ('AR', 'ARKANSAS'),
        ('AZ', 'ARIZONA'),
        ('CA', 'CALIFORNIA'),
        ('CO', 'COLORADO'),
        ('CT', 'CONNECTICUT'),
        ('DC', 'DISTRICT OF COLUMBIA'),
        ('DE', 'DELAWARE'),
        ('FL', 'FLORIDA'),
        ('FR', 'FOREIGN'),
        ('GA', 'GEORGIA'),
        ('HI', 'HAWAII'),
        ('IA', 'IOWA'),
        ('ID', 'IDAHO'),
        ('IL', 'ILLINOIS'),
        ('IN', 'INDIANA'),
        ('KS', 'KANSAS'),
        ('KY', 'KENTUCKY'),
        ('LA', 'LOUISIANA'),
        ('MA', 'MASSACHUSETTS'),
        ('MD', 'MARYLAND'),
        ('ME', 'MAINE'),
        ('MI', 'MICHIGAN'),
        ('MN', 'MINNESOTA'),
        ('MO', 'MISSOURI'),
        ('MS', 'MISSISSIPPI'),
        ('MT', 'MONTANA'),
        ('NB', 'NEBRASKA'),
        ('NC', 'NORTH CAROLINA'),
        ('ND', 'NORTH DAKOTA'),
        ('NH', 'NEW HAMPSHIRE'),
        ('NJ', 'NEW JERSEY'),
        ('NM', 'NEW MEXICO'),
        ('NV', 'NEVADA'),
        ('NY', 'NEW YORK'),
        ('OH', 'OHIO'),
        ('OK', 'OKLAHOMA'),
        ('OR', 'OREGON'),
        ('PA', 'PENNSYLVANIA'),
        ('RI', 'RHODE ISLAND'),
        ('SC', 'SOUTH CAROLINA'),
        ('SD', 'SOUTH DAKOTA'),
        ('TN', 'TENNESSEE'),
        ('TX', 'TEXAS'),
        ('UT', 'UTAH'),
        ('VA', 'VIRGINIA'),
        ('VT', 'VERMONT'),
        ('WA', 'WASHINGTON'),
        ('WI', 'WISCONSIN'),
        ('WV', 'WEST VIRGINIA'),
        ('WY', 'WYOMING'),
    )
    DEFAULT_CHOICES = {
        'Agency Address': '411 N HAYNE ST, PENSACOLA FL 32501',
        'Agency Boss': 'CHIEF JOHN MATHIS',
        'Agency Name': 'PENSACOLA POLICE DEPARTMENT',
        'Agency Phone': '(850)425-1900',
        'Default Area Code': '850',
        'Default City': 'PENSACOLA',
        'Default State': 'FL',
        'Default Zip': '325',
    }
    date_created = models.DateTimeField(db_column='Date Created', auto_now_add=True, null=True)
    date_modified = models.DateTimeField(db_column='Date Modified', auto_now=True, null=True)
    first_name = models.CharField(db_column='First Name', max_length=20, blank=True, null=True)
    middle_name = models.CharField(db_column='Middle Name', max_length=20, blank=True, null=True)
    last_name = models.CharField(db_column='Last Name', max_length=20, blank=True, null=True)
    name_to_call_me = models.CharField(db_column='Name to Call Me', max_length=20, blank=True, null=True)
    comments = models.TextField(db_column='Comments', blank=True, null=True)
    home_address = models.CharField(db_column='Home Address', max_length=40, blank=True, null=True)
    home_city = models.CharField(db_column='Home City',
                                 max_length=25,
                                 default=DEFAULT_CHOICES['Default City'],
                                 blank=True,
                                 null=True)
    home_state = models.CharField(db_column='Home State',
                                  max_length=2,
                                  choices=HOME_STATE_CHOICES,
                                  default=DEFAULT_CHOICES['Default State'],
                                  blank=True,
                                  null=True)
    home_zip = models.CharField(db_column='Home Zip',
                                max_length=10,
                                default=DEFAULT_CHOICES['Default Zip'],
                                blank=True,
                                null=True)
    home_phone = models.CharField(db_column='Home Phone', max_length=13, blank=True, null=True)
    dob = models.DateTimeField(db_column='DOB', blank=True, null=True)
    dob_year = models.IntegerField(db_column='DOB_YEAR', blank=True, null=True)
    hair = models.CharField(db_column='Hair',
                            max_length=10,
                            choices=HAIR_CHOICES,
                            blank=True,
                            null=True)
    eyes = models.CharField(db_column='Eyes',
                            max_length=10,
                            choices=EYES_CHOICES,
                            blank=True,
                            null=True)
    race = models.CharField(db_column='Race',
                            max_length=1,
                            choices=RACE_CHOICES,
                            blank=True,
                            null=True)
    sex = models.CharField(db_column='Sex',
                           max_length=1,
                           choices=SEX_CHOICES,
                           blank=True,
                           null=True)
    height = models.IntegerField(db_column='Height', blank=True, null=True)
    weight = models.IntegerField(db_column='Weight', blank=True, null=True)
    picture = models.BinaryField(db_column='Picture', blank=True, null=True)
    picture_date = models.DateTimeField(db_column='Picture Date', blank=True, null=True)
    emergency_contact_1_name = models.CharField(db_column='Emergency Contact 1 Name', max_length=30, blank=True,
                                                null=True)
    emergency_contact_1_phone = models.CharField(db_column='Emergency Contact 1 Phone', max_length=20, blank=True,
                                                 null=True)
    emergency_contact_1_relationship = models.CharField(db_column='Emergency Contact 1 Relationship',
                                                        max_length=20,
                                                        choices=EMERGENCY_CONTACT_RELATIONSHIP_CHOICES,
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
    emergency_contact_2_relationship = models.CharField(db_column='Emergency Contact 2 Relationship',
                                                        max_length=20,
                                                        choices=EMERGENCY_CONTACT_RELATIONSHIP_CHOICES,
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
    emergency_contact_3_relationship = models.CharField(db_column='Emergency Contact 3 Relationship',
                                                        max_length=20,
                                                        choices=EMERGENCY_CONTACT_RELATIONSHIP_CHOICES,
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
    emergency_contact_4_relationship = models.CharField(db_column='Emergency Contact 4 Relationship',
                                                        max_length=20,
                                                        choices=EMERGENCY_CONTACT_RELATIONSHIP_CHOICES,
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
    emergency_contact_5_relationship = models.CharField(db_column='Emergency Contact 5 Relationship',
                                                        max_length=20,
                                                        choices=EMERGENCY_CONTACT_RELATIONSHIP_CHOICES,
                                                        blank=True,
                                                        null=True)
    emergency_contact_5_address = models.CharField(db_column='Emergency Contact 5 Address', max_length=50, blank=True,
                                                   null=True)
    emergency_contact_5_comments = models.TextField(db_column='Emergency Contact 5 Comments', blank=True,
                                                    null=True)
    organization = models.CharField(db_column='Organization',
                                    max_length=30,
                                    choices=ORGANIZATION_CHOICES,
                                    blank=True, null=True)
    record_type = models.CharField(db_column='Record Type',
                                   max_length=30,
                                   choices=RECORD_TYPE_CHOICES,
                                   blank=True, null=True)
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
    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE,
        primary_key=True,
        max_length=22
    )
    picture = models.ImageField(db_column='PictureURL', upload_to='tmh/static/images')
    embedding = models.TextField(db_column='Embedding', blank=True, null=True)

    class Meta:
        db_table = 'Image_Data'


class InferenceTask(models.Model):
    LOCATING_FACE = 'LOCATING_FACE'
    ANALYZING_FACE = 'ANALYZING_FACE'
    SUCCESS = 'SUCCESS'
    ERROR = 'ERROR'
    STATES = (
        (LOCATING_FACE, 'Locating face...'),
        (ANALYZING_FACE, 'Analyzing face...'),
        (SUCCESS, 'Success!'),
        (ERROR, 'Something went wrong.'),
    )
    state = models.CharField(
        max_length=22,
        choices=STATES,
        default=LOCATING_FACE,
    )
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
