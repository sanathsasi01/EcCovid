from django.contrib import admin
from .models import PatientDetails, Beds, bedCount
# Register your models here.

admin.site.register(PatientDetails)
admin.site.register(Beds)
admin.site.register(bedCount)
