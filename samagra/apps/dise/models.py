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
COMMON_OPTIONS_CHOICE = (
        (1,'Male'),
        (2,'Female'),
        )

CLASS_CHOICES = (
    (1,"I"),
    (2,"II"),
    (3,"III"),
    (4,"IV"),
    (5,"V"),
    (6,"VI"),
    (7,"VII"),
    (8,"VIII"),
    (9,"IX"),
    (10,"X"),
    (11,"XI"),
    (12,"XII"),
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
    def __unicode__(self):
        return self.name

class AccademicYear_inspections(models.Model):
    school= models.ForeignKey(School)
    year = models.IntegerField(('Accademic year'), max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    SCHOOL_BUILDING = (
            (1,"Private"),
            (2,"Rented"),
            (3,"Government"),
            (4,"Gov: school in a rent free building"),
            (5,"No building"),
            (5,"Dilapidated"),
            (6,"Under Construction"),
            )
    status_school_building = models.IntegerField(choices=SCHOOL_BUILDING)
    accademic_inspection = models.IntegerField(default=0)
    visits_by_crc_coordinator = models.IntegerField(default=0)
    visits_by_blocklevel_officer = models.IntegerField(default=0)
    class Meta:
        unique_together = (("school", "year"),)
    def __unicode__(self):
       return u"{0} - {1}".format(self.school.name,self.year)

class Financial_year_schoolfund(models.Model):
    school= models.ForeignKey(School)
    year = models.IntegerField(('Accademic year'), max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    SDG_receipt = models.FloatField(default=0)
    SDG_expenditure = models.FloatField(default=0)
    SMG_receipt = models.FloatField(default=0)
    SMG_expenditure = models.FloatField(default=0)
    teachers_receipt = models.FloatField(default=0)
    teachers_expenditure = models.FloatField(default=0)
    class Meta:
        unique_together = (("school", "year"),)
    def __unicode__(self):
       return u"{0} - {1}".format(self.school.name,self.year)

class Staff_category(models.Model):
    school= models.ForeignKey(School)
    year = models.IntegerField(('year'), max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    POST_TYPE_CHOICE = (
            (1,'Sanctioned post'),
            (2,'In position'),
            )
    category = models.IntegerField(choices=POST_TYPE_CHOICE)
    session = models.IntegerField(choices=CLASS_TYPE_CHOICE)
    TEACHER_TYPE_CHOICE = (
            (1,'Regular Teachers'),
            (2,'Contract Teachers'),
            (3,'Part-time instructor'),
            )
    teacher_type = models.IntegerField(choices=TEACHER_TYPE_CHOICE)
    totalnumber = models.IntegerField(default=0)
    class Meta:
        unique_together = (("school", "year","category","session","teacher_type"),)
    def __unicode__(self):
       return u"{0} - {1} - {2} - {3} - {4}".format(self.school.name,self.year,self.category,self.session,self.teacher_type)


class School_puticulars_instructional_days(models.Model):
    school= models.ForeignKey(School)
    year = models.IntegerField(('year'), max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    session = models.IntegerField(choices=CLASS_TYPE_CHOICE)
    instructional_days = models.IntegerField(default=0)
    school_hours = models.IntegerField(default=0)
    teacher_hours = models.IntegerField(default=0)
    is_cce = models.BooleanField()
    is_cumulative_maintained = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICE)
    is_cumulative_record_shared = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICE)
    class Meta:
        unique_together = (("school", "year","session"),)
    def __unicode__(self):
        return u"{0} - {1}".format(self.school.name,self.year)

class School_management_commitee(models.Model):
    school = models.ForeignKey(School)
    year = models.IntegerField(('Accademic year'), max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    is_smc = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICE)
    male_total_member_in_smc = models.IntegerField(default=0)
    maleparents = models.IntegerField(default=0)
    male_local_authority = models.IntegerField(default=0)
    female_total_member_in_smc = models.IntegerField(default=0)
    femaleparents = models.IntegerField(default=0)
    female_local_authority = models.IntegerField(default=0)
    number_of_smc_meating = models.IntegerField(default=0)
    is_smc_prepare_sdp = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICE)
    is_statebank_exist = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICE)
    bank_name = models.CharField(max_length=128)
    bank_branch = models.CharField(max_length=128)
    bank_acc_no = models.CharField(max_length=128)
    bank_acc_name = models.CharField(max_length=128)
    bank_ifsc_code = models.CharField(max_length=128)
    is_child_enrolled_training = models.BooleanField()
    male_num_children = models.IntegerField(default=0)
    female_num_children = models.IntegerField(default=0)
    male_children_completed = models.IntegerField(default=0)
    female_children_completed = models.IntegerField(default=0)
    TRAINING_CONDUCTED_CHOICE = (
            (1,"School teachers"),
            (2,"Special engaged teachers"),
            (3,"Both"),
            (4,"NGO"),
            (5,"Others"),
            (6,"None"),
            )
    conducted_by = models.IntegerField(choices=TRAINING_CONDUCTED_CHOICE)
    TRAINING_CONDUCTED_IN = (
            (1,"School prenises"),
            (2,"Other than school premises"),
            (3,"Both"),
            )
    training_contected_in = models.IntegerField(choices=TRAINING_CONTECTED_IN)
    TRAINING_BEING_CONTECTED = (
            (1,"Residential"),
            (2,"Non-residential"),
            (3,"Both"),
            )
    training_contectd = models.IntegerField(choices=TRAINING_BEING_CONTECTED)

class Accademic_purticular(models.Model):
    school = models.ForeignKey(School)
    year = models.IntegerField(('Accademic year'), max_length=4,choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    is_textbook_received = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICE)
    when_received_textbook = model.IntegerField(default=0) #need to change to options year and month
    primary_freebook_received = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICE)
    uprimary_freebook_received = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICE)
    is_primary_tle_available = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICE)
    is_uprimary_tle_available = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICE)
    is_primary_playmaterial_available = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICE)
    is_uprimary_playmaterial_available = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICE)
    number_of_smdc_held = models.IntegerField(default=0)
    is_smdc_held_school_improvement_plan = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICE)
    is_seperate_bank_account = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICE)
    bank_name = models.CharField(max_length=128)
    branch_name =models.CharField(max_length=128)
    account_number = models.CharField(max_length=128)
    Account_name = models.CharField(max_length=128)
    IFSC_code = models.CharField(max_length=128)
    is_sbc = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICES)
    is_PTA = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICES)
    total_pta_meeting = models.IntegerField(default=0)
    class Meta:
        unique_together = (("school", "year"),)

 class Accademic_purticular(models.Model):
    school = models.ForeignKey(School)
    year = models.IntegerField(('Accademic year'), max_length=4,choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    is_smc_smdc_same = models.BooleanField()
    catagory = models.IntegerField(choices=COMMON_OPTIONS_CHOICE)
    total_members = models.IntegerField()
    local_representatives = models.IntegerField()
    from_backward_community = models.IntegerField()
    womengroup = models.IntegerField()
    sc_st = models.IntegerField()
    DEO = models.IntegerField()
    AAD = models.IntegerField()
    sub_expert = models.IntegerField()
    teachers = models.IntegerField()
    vice_principal = models.IntegerField()
    principal  = models.IntegerField()
    chairperson  = models.IntegerField()
    class Meta:
        unique_together = (("school","year","catagory"),)

class physical_class_fecility(models.Model):
    school = models.ForeignKey(School)
    year = models.IntegerField(('Accademic year'), max_length=4,choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    class_room = models.IntegerField(choices=CLASS_CHOICES)
    total_class_room_used = models.IntegerField(default=0)
    TYPE_OF_BUILDING = (
            (1,"Pucca"),
            (2,"Partially Pucca"),
            (3,"Kuchcha"),
            (4,"Tent"),
            )
    building_block = models.IntegerField(choices=TYPE_OF_BUILDING)
    under_construction = models.IntegerField(default=0)
    furniture_availability = models.IntegerField(default=0)
    total_other_rooms = models.IntegerField(default=0)
    under_construction = models.IntegerField(default=0)
    in_good_condition = models.IntegerField(default=0)
    in_need_miner_repair = models.IntegerField(default=0)
    in_need_major_repair = models.IntegerField(default=0)

class physical__fecility(models.Model):
    school = models.ForeignKey(School)
    year = models.IntegerField(('Accademic year'), max_length=4,choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    is_construction_land_available = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICE)
    is_seperate_room_for_head = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICES)
    boys_toilets_number = models.IntegerField(default=0)
    girls_toilets_number = models.IntegerField(default=0)
    boys_toilet_functional = models.IntegerField(default=0)
    girls_toilet_functional = models.IntegerField(default=0)
    boys_toilets_water_available = models.IntegerField(default=0)
    girls_toilet_water_available = models.IntegerField(default=0)
    boys_urinal_available = models.IntegerField(default=0)
    girls_urinal_available = models.IntegerField(default=0)
    is_handwashing_facility_near_toilet = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICES)
    is_childrenfriendly-toilets = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICES)
    DRINKING_WATER_CHOICES = (
            (1,"Hand Pump"),
            (2,"Well"),
            (3,"Tap water"),
            (4,"Others"),
            (5,"None"),
            )
    main_source_of_drinking_water = models.IntegerField(choices=DRINKING_WATER_CHOICES)
    is_drinking_facility_functional = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICES)
    is_electricity_connection_available = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICES)
    BOUNDRY_OPTIONS_CHOICES = (
            (0,"Not Applicable"),
            (1,"Pucca"),
            (2,"Pucca but broken"),
            (3,"Barbed wire fencing"),
            (4,"Hedges"),
            (5,"No boundry wall"),
            (6,"Others"),
            (7,"Partial"),
            (8,"Under Construction"),
            )
    type_boundry_well = models.IntegerField(choices=BOUNDRY_OPTIONS_CHOICES)
    is_library = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICES)
    total_books = models.integerField(default=0)
    is_fulltime_librararian = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICES)
    is_newspaper_subscribe = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICES)
    is_playground = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICES)
    is_land_available_for_playground = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICES)
    class Meta:
        unique_together = (("school","year","catagory"),)

class Fecility_learning(models.Model):
    school = models.ForeignKey(School)
    year = models.IntegerField(('Accademic year'), max_length=4,choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    is_computer_lab = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICES)
    total_computer_available = models.IntegerField(default=0)
    total_computer_functional = models.IntegerField(default=0)
    is_computer_aided_learning = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICES)
    is_medical_checkup_conducted = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICES)
    is_ramp_needed_for_disabled_children = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICES)
    is_ramp_available = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICES)
    is_handheld_ramp_available = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICES)
    class Meta:
        unique_together = (("school","year"),)

class Hostalfacility(models.Model):
    school = models.ForeignKey(School)
    year = models.IntegerField(('Accademic year'), max_length=4,choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    is_hostel = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICES)
    is_boys_hostel = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICES)
    total_boys = models.IntegerField(default=0)
    is_girls_hostel = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICES)
    total_girls = models.IntegerField(default=0)
    class Meta:
        unique_together = (("school","year"),)

class Rooms_availability(models.Model):
    school = models.ForeignKey(School)
    year = models.IntegerField(('Accademic year'), max_length=4,choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    is_room_for_head = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICES)
    is_room_for_girls = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICES)
    is_staffroom = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICES)
    is_ict_lab = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICES)
    is_computer_room = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICES)
    is_cocurricular_room = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICES)
    is_staff_quarter = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICES)
    is_science_lab = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICES)
    is_library_room = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICES)
    is_audio_visual_equipment = models.integerField(choices=BOOLEAN_OPTIONS_CHOICES)
    is_projector_equipment = models.integerField(choices=BOOLEAN_OPTIONS_CHOICES)
    is_fire_extinguisher_equipment = models.integerField(choices=BOOLEAN_OPTIONS_CHOICES)
    is_internet_connection_equipment = models.integerField(choices=BOOLEAN_OPTIONS_CHOICES)
    is_rainwater_harvesting = models.integerField(choices=BOOLEAN_OPTIONS_CHOICES)
    is_science_kit = models.integerField(choices=BOOLEAN_OPTIONS_CHOICES)
    is_maths_kit = models.integerField(choices=BOOLEAN_OPTIONS_CHOICES)
    class Meta:
        unique_together = (("school","year"),)


class Rooms_availability(models.Model):
    school = models.ForeignKey(School)
    year = models.IntegerField(('Accademic year'), max_length=4,choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    SUBJECT_TYPE_CHOICES = (
            (1,"Physics"),
            (2,"Chemistry"),
            (3,"Biology"),
            (4,"Computer"),
            (5,"Mathematics"),
            (6,"Language"),
            (7,"Geography"),
            (8,"Homescience"),
            (9,"Psychology"),
            )
    subject = models.IntegerField(choices=SUBJECT_TYPE_CHOICES)
    is_seperate_room = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICES)
    CONDITION_CHOICE = (
            (1,"Not Applicable"),
            (2,"Fully equipped"),
            (3,"Partially equipped"),
            (4,"Not equipped"),
            (5,"Not Available"),
            )
    present_condition = models.IntegerField(choices=CONDITION_CHOICE)
    class Meta:
        unique_together = (("school","year","subject"),)

class Mid_day_meal(models.Model):
    school = models.ForeignKey(School)
    year = models.IntegerField(('Accademic year'), max_length=4,choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    SCHOOL_TYPE = (
            (1,"Government"),
            (2,"Govt. Aided"),
            )
    school_type = models.IntegerField(choices=SCHOOL_TYPE)
    STATUS_CHOICES = (
            (1,"Not Applicable"),
            (2,"Not Provided"),
            (3,"Provided & prepared in school premises"),
            (4,"Provided but not prepared in school premises"),
            )
    status = models.IntegerField(choices=STATUS_CHOICES)
    ROOM_STATUS = (
            (1,"Not applicable"),
            (2,"Available"),
            (3,"Not available"),
            (4,"Under Construction"),
            (5,"ClassRoom used as kitchen"),
            )
    status_kitchen_shed = models.IntegerField(choices=ROOM_STATUS)
    SOURCE_OF_MDM = (
            (1,"Nearby school"),
            (2,"NGO"),
            (3,"Self Help Group"),
            (4,"PTA/MPTA"),
            (5,"Others"),
            (6,"Gram panchayat"),
            (7,"Central kitchen"),
            )
    souce_of_mdm = models.IntegerField(choices=SOURCE_OF_MDM)
    class Meta:
        unique_together = (("school","year"),)

class Teachers_and_instructors(models.Model):
    teacher_code = models.IntegerField(default=0)
    aadhar_pnr = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    gender = model.IntegerField(choices=COMMON_OPTIONS_CHOICE)
    Dateofbirth = models.DateField()
    socialcategory= model.IntegerField(choices=SOCIAL_CATEGORY)
    type_teacher = models.IntegerField(choices=TEACHER_TYPES)
    appoinment_nature =models.IntegerField(choices=APPOINMENT_NATURE)
    joining_date = models.DateField()
    academic = models.CharField(max_ength=256)
    professional = models.CharField(max_ength=256)
    classes_taught = models.IntegerField(choices=CLASSES_TAUGHT_CHOICES)
    appointed_subject = models.IntegerField(choices=APPOINTED_SUBJECT)
    main_subject1 = models.IntegerField(choices=MAIN_SUBJECT_CHOICES)
    total_days_brc = models.IntegerField(default=0)
    total_days_crc = models.IntegerField(default=0)
    total_days_diet = models.IntegerField(default=0)
    total_days_others = models.IntegerField(default=0)
    days_non_teaching = models.IntegerField(default=0)
    maths_science_studied_upto = models.IntegerField(default=0)
    english_studied_upto = models.IntegerField(default=0)
    socialstudies_upto = models.IntegerField(default=0)
    working_current_school_since_year = models.IntegerField(default=0)
    type_disability = models.IntegerField(choices=DISABILITY_TYPE)
    is_trained = models.IntegerField(choices=BOOLEAN_OPTIONS_CHOICES)
    state_defined_variable = models.CharField(max_length=128)


