from django.db import models
import datetime

YEAR_CHOICES = []
for r in range(2012, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))

class Schools(models.Model):
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
    school_established_year = models.IntegerField(('year'), max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    elementry_recognition = models.IntegerField(('year'), max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    secondary_recognition = models.IntegerField(('year'), max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    hssc_recognition = models.IntegerField(('year'), max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    year_upgrade_primary_to_UP = models.IntegerField(('year'), max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    year_upgrade_primary_to_secondary = models.IntegerField(('year'), max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    year_upgrade_primary_to_HSSC = models.IntegerField(('year'), max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    is_specialschool_CWSN = models.BooleanField()
    is_shift_school = models.BooleanField()
