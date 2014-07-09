from django.contrib import admin
from samagra.apps.dise.models import School
from samagra.apps.dise.models import AccademicYear_inspections
from samagra.apps.dise.models import Financial_year_schoolfund
from samagra.apps.dise.models import Staff_category
from samagra.apps.dise.models import School_puticulars_instructional_days

admin.site.register(School)
admin.site.register(AccademicYear_inspections)
admin.site.register(Financial_year_schoolfund)
admin.site.register(Staff_category)
admin.site.register(School_puticulars_instructional_days)
# Register your models here.
