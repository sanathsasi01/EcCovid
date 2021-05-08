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
    fever_date = models.DateField(null=True)

    cough = models.BooleanField(default=False)
    cough_date = models.DateField(null=True)

    throat_pain = models.BooleanField(default=False)
    throat_pain_date = models.DateField(null=True)

    breathlessness = models.BooleanField(default=False)
    breathlessness_date = models.DateField(null=True)

    loose_stool = models.BooleanField(default=False)
    loose_stool_date = models.DateField(null=True)
    
    body_pain = models.BooleanField(default=False)
    body_pain_date = models.DateField(null=True)

    loss_smell = models.BooleanField(default=False)
    loss_smell_date = models.DateField(null=True)

    loss_of_taste = models.BooleanField(default=False)
    loss_of_taste_date = models.DateField(null=True)



class Signs(models.Model):
    patient = models.ForeignKey(PatientDetails, on_delete=models.CASCADE)

    pulse_rate = models.CharField(max_length=20, null=True)
    blood_pressure = models.CharField(max_length=20, null=True)
    respiratory_rate = models.CharField(max_length=20, null=True)
    spo2 = models.CharField(max_length=20, null=True)
    temperature = models.CharField(max_length=20, null=True)
    cbg = models.CharField(max_length=20, null=True)
    


class PastHistory(models.Model):
    patient = models.ForeignKey(PatientDetails, on_delete=models.CASCADE)

    systematic_hypertension = models.BooleanField(default=False)
    systematic_hypertension_year = models.CharField(max_length=4 , null=True)
    systematic_hypertension_treatment = models.CharField(max_length=20, null=True)

    diabetes_mellitess = models.BooleanField(default=False)
    diabetes_mellitess_year = models.CharField(max_length=4 , null=True)
    diabetes_mellitess_treatment = models.CharField(max_length=20, null=True)

    bronchial_asthma = models.BooleanField(default=False)
    bronchial_asthma_year = models.CharField(max_length=4 , null=True)
    bronchial_asthma_treatment = models.CharField(max_length=20, null=True)

    chronic_kidney_disease = models.BooleanField(default=False)
    chronic_kidney_disease_year = models.CharField(max_length=4 , null=True)
    chronic_kidney_disease_treatment = models.CharField(max_length=20, null=True)

    copd = models.BooleanField(default=False)
    copd_year = models.CharField(max_length=4 , null=True)
    copd_treatment = models.CharField(max_length=20, null=True)

    hiv = models.BooleanField(default=False)
    hiv_year = models.CharField(max_length=4 , null=True)
    hiv_treatment = models.CharField(max_length=20, null=True)

    hepatitis_b = models.BooleanField(default=False)
    hepatitis_b_year = models.CharField(max_length=4 , null=True)
    hepatitis_b_treatment = models.CharField(max_length=20, null=True)

    hepatitis_c = models.BooleanField(default=False)
    hepatitis_c_year = models.CharField(max_length=4 , null=True)
    hepatitis_c_treatment = models.CharField(max_length=20, null=True)

    abdominal_pain = models.BooleanField(default=False)
    abdominal_pain_year = models.CharField(max_length=4 , null=True)
    abdominal_pain_treatment = models.CharField(max_length=20, null=True)

    diarrhea = models.BooleanField(default=False)
    diarrhea_year = models.CharField(max_length=4 , null=True)
    diarrhea_treatment = models.CharField(max_length=20, null=True)

    jaundice = models.BooleanField(default=False)
    jaundice_year = models.CharField(max_length=4 , null=True)
    jaundice_treatment = models.CharField(max_length=20, null=True)

    malignancy = models.BooleanField(default=False)
    malignancy_year = models.CharField(max_length=4 , null=True)
    malignancy_treatment = models.CharField(max_length=20, null=True)

    past_history = models.BooleanField(default=False)
    past_history_year = models.CharField(max_length=4 , null=True)
    past_history_treatment = models.CharField(max_length=20, null=True)

    other_person_history = models.BooleanField(default=False)
    other_person_year = models.CharField(max_length=4 , null=True)
    other_person_treatment = models.CharField(max_length=20, null=True)


