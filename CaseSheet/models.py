from django.db import models
from DoctorModule.models import DoctorPatientRelation
# Create your models here.


class CaseFile(models.Model):
    doc_pat_relation = models.ForeignKey(DoctorPatientRelation, on_delete=models.CASCADE)
    day = models.IntegerField()
    respiratory = models.CharField(max_length=50, null=True, blank=True)
    medicines = models.TextField(blank=True)
    allergies = models.CharField(max_length=50, null=True, blank=True)