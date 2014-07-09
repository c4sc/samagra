from django.contrib import admin
from samagra.apps.dise.models import School
from samagra.apps.dise.models import AccademicYear_inspections
from samagra.apps.dise.models import Financial_year_schoolfund

admin.site.register(School)
admin.site.register(AccademicYear_inspections)
admin.site.register(Financial_year_schoolfund)
# Register your models here.
