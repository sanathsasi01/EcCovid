from django.db import models
from django.contrib.auth import get_user_model

# from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

User = get_user_model()
class PatientDetails(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=True)
    age = models.CharField(max_length=3, null=True)
    sex = models.CharField(max_length=10, null=True)
    dob = models.DateField(null=True)
    adhaar = models.CharField(max_length=12, null=True)
    address = models.TextField(null=True)
    personal_mobile_no = models.CharField(null=True,max_length=10)
    bystander_mobile_no = models.CharField(null=True,max_length=10)
    dateAdmitted = models.DateTimeField(null=True)
    criticallity = models.CharField(max_length=10, null=True)

#     def __str__(self):
#         return self.name

# class RT_PCR_Details(models.Model):
    # patient = models.ForeignKey(PatientDetails, on_delete=models.CASCADE)
    swab_taken = models.CharField(max_length=3, null=True)
    hrct_taken = models.CharField(max_length=3, null=True)
    lab_name_with_address = models.TextField(null=True)
    date_of_test = models.DateField(null=True)
    positive_or_negative = models.CharField(max_length=10, null=True)
    sr_id = models.CharField(max_length=50, null=True)
    icmr_id = models.CharField(max_length=50, null=True)
    ct_thorax_taken = models.CharField(max_length=3, null=True)
    ct_thorax_date = models.DateField(null=True)


