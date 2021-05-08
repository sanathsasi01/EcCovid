from django.db import models

# Create your models here.
from PatientModule.models import PatientDetails
from django.contrib.auth import get_user_model

User = get_user_model()

class DoctorPatientRelation(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    patient = models.ForeignKey(PatientDetails, on_delete=models.CASCADE)

    def  __str__(self):
        return self.doctor.firstname + ' ' + self.patient.firstname
    

