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

    swab_taken = models.CharField(max_length=3, null=True, blank=True)
    hrct_taken = models.CharField(max_length=3, null=True, blank=True)
    lab_name_with_address = models.TextField(null=True, blank=True)
    date_of_test = models.DateField(null=True, blank=True)
    positive_or_negative = models.CharField(max_length=10, null=True, blank=True)
    sr_id = models.CharField(max_length=50, null=True, blank=True)
    icmr_id = models.CharField(max_length=50, null=True, blank=True)
    ct_thorax_taken = models.CharField(max_length=3, null=True, blank=True)
    ct_thorax_date = models.DateField(null=True, blank=True)


class Symptoms(models.Model):
    patient = models.ForeignKey(PatientDetails, on_delete=models.CASCADE, null=True)
    fever = models.BooleanField(default=False)
    fever_date = models.DateField(null=True, blank=True)

    cough = models.BooleanField(default=False)
    cough_date = models.DateField(null=True, blank=True)

    throat_pain = models.BooleanField(default=False)
    throat_pain_date = models.DateField(null=True, blank=True)

    breathlessness = models.BooleanField(default=False)
    breathlessness_date = models.DateField(null=True, blank=True)

    loose_stool = models.BooleanField(default=False)
    loose_stool_date = models.DateField(null=True, blank=True)
    
    body_pain = models.BooleanField(default=False)
    body_pain_date = models.DateField(null=True, blank=True)

    loss_smell = models.BooleanField(default=False)
    loss_smell_date = models.DateField(null=True, blank=True)

    loss_of_taste = models.BooleanField(default=False)
    loss_of_taste_date = models.DateField(null=True, blank=True)



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
    systematic_hypertension_treatment = models.CharField(max_length=20, null=True, blank=True)

    diabetes_mellitess = models.BooleanField(default=False)
    diabetes_mellitess_year = models.CharField(max_length=4 , null=True)
    diabetes_mellitess_treatment = models.CharField(max_length=20, null=True, blank=True)

    bronchial_asthma = models.BooleanField(default=False)
    bronchial_asthma_year = models.CharField(max_length=4 , null=True)
    bronchial_asthma_treatment = models.CharField(max_length=20, null=True, blank=True)

    chronic_kidney_disease = models.BooleanField(default=False)
    chronic_kidney_disease_year = models.CharField(max_length=4 , null=True)
    chronic_kidney_disease_treatment = models.CharField(max_length=20, null=True, blank=True)

    copd = models.BooleanField(default=False)
    copd_year = models.CharField(max_length=4 , null=True)
    copd_treatment = models.CharField(max_length=20, null=True, blank=True)

    hiv = models.BooleanField(default=False)
    hiv_year = models.CharField(max_length=4 , null=True)
    hiv_treatment = models.CharField(max_length=20, null=True, blank=True)

    hepatitis_b = models.BooleanField(default=False)
    hepatitis_b_year = models.CharField(max_length=4 , null=True)
    hepatitis_b_treatment = models.CharField(max_length=20, null=True, blank=True)

    hepatitis_c = models.BooleanField(default=False)
    hepatitis_c_year = models.CharField(max_length=4 , null=True)
    hepatitis_c_treatment = models.CharField(max_length=20, null=True, blank=True)

    abdominal_pain = models.BooleanField(default=False)
    abdominal_pain_year = models.CharField(max_length=4 , null=True)
    abdominal_pain_treatment = models.CharField(max_length=20, null=True, blank=True)

    diarrhea = models.BooleanField(default=False)
    diarrhea_year = models.CharField(max_length=4 , null=True)
    diarrhea_treatment = models.CharField(max_length=20, null=True, blank=True)

    jaundice = models.BooleanField(default=False)
    jaundice_year = models.CharField(max_length=4 , null=True)
    jaundice_treatment = models.CharField(max_length=20, null=True, blank=True)

    malignancy = models.BooleanField(default=False)
    malignancy_year = models.CharField(max_length=4 , null=True)
    malignancy_treatment = models.CharField(max_length=20, null=True, blank=True)

    past_history = models.BooleanField(default=False)
    past_history_year = models.CharField(max_length=4 , null=True)
    past_history_treatment = models.CharField(max_length=20, null=True, blank=True)

    other_person_history = models.BooleanField(default=False)
    other_person_year = models.CharField(max_length=4 , null=True)
    other_person_treatment = models.CharField(max_length=20, null=True, blank=True)



class Examination(models.Model):
    patient = models.ForeignKey(PatientDetails, on_delete=models.CASCADE)
    # general examination
    pallor = models.BooleanField(default=False)
    ictcrus = models.BooleanField(default=False)
    cyanosis = models.BooleanField(default=False)
    clubbing = models.BooleanField(default=False)
    lymphadenpathy = models.BooleanField(default=False)
    edema = models.BooleanField(default=False)
    # systematic examination
    respiratory_system =  models.CharField(max_length=10, null=True)
    respiratory_normal = models.CharField(max_length=30, null=True)
    respiratory_abnormal = models.CharField(max_length=30, null=True)

    cardiovascular_system = models.CharField(max_length=10, null=True)
    cardiovascular_normal = models.CharField(max_length=30, null=True)
    cardiovascular_abnormal = models.CharField(max_length=30, null=True)

    gastrointestinal = models.CharField(max_length=10, null=True)
    gastrointestinal_normal = models.CharField(max_length=30, null=True)
    gastrointestinal_abnormal = models.CharField(max_length=30, null=True)

    cns = models.CharField(max_length=10, null=True)
    cns_normal = models.CharField(max_length=30, null=True)
    cns_abnormal = models.CharField(max_length=30, null=True)


class DifferentialDiagnosis(models.Model):
    patient = models.ForeignKey(PatientDetails, on_delete=models.CASCADE, null=True)
    covid19Pneumonitis = models.BooleanField(default=False)
    viralPneumonitis = models.BooleanField(default=False)
    others = models.BooleanField(default=False)


class HealthFacalities(models.Model):
    patient = models.ForeignKey(PatientDetails, on_delete=models.CASCADE, null=True)
    Facalitiedvisited = models.CharField(max_length=50, null=True)
    date = models.DateField(null=True)
    treatment = models.CharField(max_length=80, null=True)
    remarks = models.CharField(max_length=100)


class Microbiology(models.Model):
    patient = models.ForeignKey(PatientDetails, on_delete=models.CASCADE)

    rt_pcr_covid_date = models.DateField(null=True)
    rt_pcr_covid_result = models.CharField(max_length=20, null=True)

    rapid_anti_body_date = models.DateField(null=True)
    rapid_anti_body_date = models.CharField(max_length=20, null=True) 

    rt_pcr_H1N_date = models.DateField(null=True)
    rt_pcr_H1N_result = models.CharField(max_length=20, null=True)

    viral_culture_date = models.DateField(null=True)
    viral_culture_result = models.CharField(max_length=20, null=True)

    viral_culture_date2 = models.DateField(null=True)
    viral_culture_result2 = models.CharField(max_length=20, null=True)

    
class Treatment(models.Model):
    patient = models.ForeignKey(PatientDetails, on_delete=models.CASCADE)
    # first row
    o2 = models.IntegerField()
    nasalcannula = models.BooleanField(default=False, blank=True)
    hudson_mask = models.BooleanField(default=False, blank=True)
    nrbm = models.BooleanField(default=False, blank=True)
    niv = models.BooleanField(default=False, blank=True)
    niv_f102 = models.BooleanField(default=False, blank=True)
    niv_peep = models.BooleanField(default=False, blank=True)
    niv_rr = models.BooleanField(default=False, blank=True)
    niv_ps = models.BooleanField(default=False, blank=True)

    # second set
    inj_remdesivir = models.BooleanField(default=False, blank=True)
    tab_favipiravir = models.BooleanField(default=False, blank=True)
    
    inj_lmwh = models.BooleanField(default=False, blank=True)
    inj_lmwh_40mg = models.BooleanField(default=False, blank=True)
    inj_lmwh_40mg_od_bd = models.BooleanField(default=False, blank=True)
    inj_lmwh_60mg = models.BooleanField(default=False, blank=True)
    inj_lmwh_60mg_od_bd = models.BooleanField(default=False, blank=True)

    inj_dexamethaxone = models.BooleanField(default=False, blank=True)
    inj_dexamethaxone_40mg = models.BooleanField(default=False, blank=True)
    inj_dexamethaxone_40mg_odbd = models.BooleanField(default=False, blank=True)

    pantaprozole_40mg = models.BooleanField(default=False, blank=True)
    pantaprozole_40mg_bd = models.BooleanField(default=False, blank=True)

    emeset_4g = models.BooleanField(default=False, blank=True)
    emeset_4g_tds = models.BooleanField(default=False, blank=True)

    inj_ulinastatin = models.BooleanField(default=False, blank=True)
    inj_ulinastatin_bd = models.BooleanField(default=False, blank=True)
    inj_ulinastatin_tds = models.BooleanField(default=False, blank=True)

    t_pirfenidone_200mg = models.BooleanField(default=False, blank=True)
    t_pirfenidone_200mg_bd = models.BooleanField(default=False, blank=True)

    t_vitaminc_500mg = models.BooleanField(default=False, blank=True)
    t_vitaminc_500mg_tds = models.BooleanField(default=False, blank=True)

    t_zincovit_40mg = models.BooleanField(default=False, blank=True)
    t_zincovit_40mg_od = models.BooleanField(default=False, blank=True)

    t_nac_600mg = models.BooleanField(default=False, blank=True)
    t_nac_600mg_bd = models.BooleanField(default=False, blank=True)

    nebulisation = models.BooleanField(default=False, blank=True)
    nebulisation_budocort = models.BooleanField(default=False, blank=True)
    nebulisation_budocort_qh = models.IntegerField( blank=True)
    nebulisation_duolin = models.BooleanField(default=False, blank=True)
    nebulisation_duolin_qh = models.IntegerField(default=False, blank=True)




    prone_ventilation = models.BooleanField(default=False, blank=True)
    spirometer_excercise = models.BooleanField(default=False, blank=True)






