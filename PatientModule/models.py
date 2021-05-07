from django.db import models

# Create your models here.


class PatientDetails(models.Model):
    firstname = models.CharField(max_length=30, null=True)
    lastname = models.CharField(max_length=30, null=True)
    sex = models.CharField(max_length=10, null=True)
    dateAdmitted = models.DateTimeField(auto_now_add=True)
    criticallity = models.CharField(max_length=10, null=True    )