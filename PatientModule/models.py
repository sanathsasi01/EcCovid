from django.db import models
from django.contrib.auth import get_user_model
import datetime
# from phonenumber_field.modelfields import PhoneNumberField

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

    swab_taken = models.CharField(max_length=3, null=True)
    hrct_taken = models.CharField(max_length=3, null=True)
    lab_name_with_address = models.TextField(null=True)
    date_of_test = models.DateField(null=True)
    positive_or_negative = models.CharField(max_length=10, null=True)
    sr_id = models.CharField(max_length=50, null=True)
    icmr_id = models.CharField(max_length=50, null=True)
    ct_thorax_taken = models.CharField(max_length=3, null=True)
    ct_thorax_date = models.DateField(null=True)


class Symptoms(models.Model):
    patient = models.ForeignKey(PatientDetails, on_delete=models.CASCADE, null=True)
    fever = models.BooleanField(default=False)
    fever_date = models.DateField(default=datetime.date.today)

    cough = models.BooleanField(default=False)
    cough_date = models.DateField(default=datetime.date.today)

    throat_pain = models.BooleanField(default=False)
    throat_pain_date = models.DateField(default=datetime.date.today)

    breathlessness = models.BooleanField(default=False)
    breathlessness_date = models.DateField(default=datetime.date.today)

    loose_stool = models.BooleanField(default=False)
    loose_stool_date = models.DateField(default=datetime.date.today)
    
    body_pain = models.BooleanField(default=False)
    body_pain_date = models.DateField(default=datetime.date.today)

    loss_smell = models.BooleanField(default=False)
    loss_smell_date = models.DateField(default=datetime.date.today)

    loss_of_taste = models.BooleanField(default=False)
    loss_of_taste_date = models.DateField(default=datetime.date.today)



class Signs(models.Model):
    patient = models.ForeignKey(PatientDetails, on_delete=models.CASCADE)

    pulse_rate = models.CharField(max_length=20, null=True)
    blood_pressure = models.CharField(max_length=20, null=True)
    respiratory_rate = models.CharField(max_length=20, null=True)
    spo2 = models.CharField(max_length=20, null=True)
    temperature = models.CharField(max_length=20, null=True)
    cbg = models.CharField(max_length=20, null=True)
    co2 = models.CharField(max_length=20, null=True)

