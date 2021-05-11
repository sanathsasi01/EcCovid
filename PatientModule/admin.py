from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(PatientDetails)
admin.site.register(Beds)
# admin.site.register(bedCount)
admin.site.register(FreeBeds)

