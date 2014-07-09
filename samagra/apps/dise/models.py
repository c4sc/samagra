from django.db import models
import datetime

YEAR_CHOICES = []
for r in range(2010, (datetime.datetime.now().year+3)):
    YEAR_CHOICES.append((r,r))

CLASS_TYPE_CHOICE = (
   (1,'Primary'),
   (2,'Upper Primary'),
   (3,'Secondary'),
   (4,'Higher secondary'),
                )
BOOLEAN_OPTIONS_CHOICE = (
        (0,'Not applicable'),
        (1,'Yes'),
        (2,'No'),
        )

class School(models.Model):
    CATEGORY_CHOICES = (
                         (1, 'Primary only (1-5)'),
                         (2, 'Primary with UP (1-8)'),
                         (3, 'Primary with UP , secondary and HSSC(1-12)'),
                         (4, 'Upper Primary (1-10)'),
                         (5, 'UP with secondary and HSSC(6-12)'),
                         (6, 'Primary with UP and Secondary(1-10)'),
                         (7, 'UP with Secondary(6-10)'),
                         (8, 'Secondary (9&10)'),
                         (9, 'Secondary with HSSC(9-12)'),
                         (10, 'HSSC/ jr.College(11-12)'),
                       )
    name = models.CharField(max_length=128)
    is_rural = models.BooleanField()
    rural_area_name = models.CharField(max_length=128, blank=True, null = True)
    urban_area_name = models.CharField(max_length=128, blank=True, null = True)
    rural_village_name = models.CharField(max_length=128, blank=True, null = True)
    urban_ward_number = models.CharField(max_length=50, blank=True, null = True)
    pincode = models.CharField(max_length=10)
    rural_panchayath_name = models.CharField(max_length=75, blank=True, null=True)
    crc_name = models.CharField(max_length=100)
    block = models.CharField(max_length=100)
    educational_zone = models.CharField(max_length=128)
    assembly_constituency = models.CharField(max_length=128)
    municipality = models.CharField(max_length=128, blank=True, null=True)
    city = models.CharField(max_length=128, blank=True, null =True)
    office_stdcode = models.CharField(max_length=6, blank=True, null=True)
    office_land_number = models.CharField(max_length=8, blank=True, null=True)
    office_mobile = models.CharField(max_length=15, blank=True, null=True)
    respondent_stdcode = models.CharField(max_length=6, blank=True, null=True)
    respondent_land_number = models.CharField(max_length=8, blank=True, null=True)
    respondent_mobile = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=128, blank=True, null=True)
    website = models.CharField(max_length=128, blank=True, null=True)
    category = models.IntegerField(choices=CATEGORY_CHOICES)
    lowest_class = models.CharField(max_length=3)
    highest_class = models.CharField(max_length=3)
    TYPE_SCHOOL_CHOICES = (
            (1, 'Boys'),
            (2, 'Girls'),
            (3, 'Co-educational'),
            )
    elementry_type = models.IntegerField(choices=TYPE_SCHOOL_CHOICES)
    secondary_type = models.IntegerField(choices=TYPE_SCHOOL_CHOICES)
    higher_secondary_type = models.IntegerField(choices=TYPE_SCHOOL_CHOICES)
    MANAGEMENT_CHOICES = (
            (1, 'Department of education'),
            (2, 'Tribal/ Social welfare Department'),
            (3, 'Local body'),
            (4, 'Pvt. Aided'),
            (5, 'Pvt .Unaided'),
            (6, 'others'),
            (7, 'Central Government'),
            (8, 'Unrecognised'),
            (9, 'Madarsa recognized'),
            (10, 'Madrasa unrecognised'),
            )
    managed_by = models.IntegerField(choices=MANAGEMENT_CHOICES)
    distance_from_primary = models.CharField(max_length=7, blank=True, null=True)
    distance_from_upi = models.CharField(max_length=7, blank=True, null=True)
    is_weather_roads = models.BooleanField()
    school_established_year = models.IntegerField(('school established year'), max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    elementry_recognition = models.IntegerField(('elementry recognition'), max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    secondary_recognition = models.IntegerField(('secondary recognition'), max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    hssc_recognition = models.IntegerField(('hssc recognition'), max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    year_upgrade_primary_to_UP = models.IntegerField(('year of upgrade primary to UP'), max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    year_upgrade_primary_to_secondary = models.IntegerField(('year of upgrade primary to Secondary'), max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    year_upgrade_primary_to_HSSC = models.IntegerField(('year of upgrade Primary to HSSC'), max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    is_specialschool_CWSN = models.BooleanField()
    is_shift_school = models.BooleanField()
    TYPE_RESIDENTIAL_CHOICES = (
            (1, 'Ashram(Govt)'),
            (2, 'Non Ashram (Govt)'),
            (3, 'Private'),
            (4, 'Others'),
            (5, 'Kasturba gandhi Balika Vidhyalaya'),
            (6, 'Model school'),
            )
    is_residential = models.BooleanField()
    Primary_residential_choice = models.IntegerField(choices=TYPE_RESIDENTIAL_CHOICES, null=True)
    UpperPrimary_residential_choice = models.IntegerField(choices=TYPE_RESIDENTIAL_CHOICES, null=True)
    Secondary_residential_choice = models.IntegerField(choices=TYPE_RESIDENTIAL_CHOICES, null=True)
    HSSC__residential_choice = models.IntegerField(choices=TYPE_RESIDENTIAL_CHOICES, null=True)
    MEDIUM_INSTRUCTION_CHOICES = (
            (1, 'English'),
            (2, 'Hindi'),
            (3, 'Malayalam'),
            (4, 'Tamil'),
            (5, 'Assamese'),
            (6, 'Bengali'),
            (7, 'Gujarati'),
            (8, 'Kannada'),
            (9, 'Kashmiri'),
            (10, 'Konkani'),
            (11, 'Manipuri'),
            (12, 'Marathi'),
            (13, 'Nepali'),
            (14, 'Sanskrit'),
            (15, 'Sindhi'),
            (17, 'Telugu'),
            (18, 'Urdu'),
            (20, 'Bodo'),
            (21, 'Mising'),
            (22, 'Dogri'),
            (23, 'Khasi'),
            (24, 'Garo'),
            (25, 'Mizo'),
            (26, 'Bhutia'),
            (27, 'Leptcha'),
            (28, 'Limboo'),
            (29, 'French'),
            (30, 'Odia'),
            (31, 'Panjabi'),
            (32, 'Others'),
            )
    primary_medium = models.IntegerField(choices=MEDIUM_INSTRUCTION_CHOICES)
    secondary_medium = models.IntegerField(choices=MEDIUM_INSTRUCTION_CHOICES)
    tertiary_medium = models.IntegerField(choices=MEDIUM_INSTRUCTION_CHOICES)
    quartery_medium = models.IntegerField(choices=MEDIUM_INSTRUCTION_CHOICES)
    AFFILIATION_BOARD_CHOICE = (
            (0,'Not applicable'),
            (1,'CBSE'),
            (2,'StateBoard'),
            (3,'ICSE'),
            (4,'International'),
            (5,'Others'),
            )
    secondary_affiliation_board = models.IntegerField(choices=AFFILIATION_BOARD_CHOICE)
    HSSC_affiliation_board = models.IntegerField(choices=AFFILIATION_BOARD_CHOICE)
    lattitude_degree = models.IntegerField(default=0)
    lattitude_minutes = models.IntegerField(default=0)
    lattitude_seconds = models.IntegerField(default=0)
    longitude_degree = models.IntegerField(default=0)
    longitude_minutes = models.IntegerField(default=0)
    longitude_seconds = models.IntegerField(default=0)
    is_preprimary = models.BooleanField()
    preprimary_total_students = models.IntegerField(default=0)
    preprimary_total_teachers = models.IntegerField(default=0)
    is_anganwadi = models.BooleanField()
    anganwadi_total_students = models.IntegerField(default=0)
    anganwadi_total_workers = models.IntegerField(default=0)


class AccademicYear_inspections(models.Model):
    school= models.ForeignKey(School)
    year = models.IntegerField(('year'), max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    accademic_inspection = models.IntegerField(default=0)
    visits_by_crc_coordinator = models.IntegerField(default=0)
    visits_by_blocklevel_officer = models.IntegerField(default=0)

class Financial_year_Schoolfunds(models.Model):
    school= models.ForeignKey(School)
    year = models.IntegerField(('year'), max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    SDG_receipt = models.FloatField(default=0)
    SDG_expenditure = models.FloatField(default=0)
    SMG_receipt = models.FloatField(default=0)
    SMG_expenditure = models.FloatField(default=0)
    teachers_receipt = models.FloatField(default=0)
    teachers_expenditure = models.FloatField(default=0)

class Staff_category(models.Model):
    school= models.ForeignKey(School)
    year = models.IntegerField(('year'), max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    sanctioned = models.IntegerField(choices=CLASS_TYPE_CHOICE)
    inposition = models.IntegerField(choices=CLASS_TYPE_CHOICE)
    TEACHER_TYPE_CHOICE = (
            (1,'Regular Teachers'),
            (2,'Contract Teachers'),
            (3,'Part-time instructor'),
            )
    teacher_type = models.IntegerField(choices=TEACHER_TYPE_CHOICE)
    totalnumber = models.IntegerField(default=0)


class School_puticulars_instructional_days(models.Model):
    school= models.ForeignKey(School)
    year = models.IntegerField(('year'), max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    instructional_days = models.IntegerField(default=0)
    school_hours = models.IntegerField(default=0)
    teacher_hours = models.IntegerField(default=0)
    is_cce = models.BooleanField()
    is_cumulative_maintained = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICE)
    is_cumulative_record_shared = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICE)
    is_smc = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICE)

