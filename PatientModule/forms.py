from django import forms
from .models import *


# custom date filter
class DateInput(forms.DateInput):
    input_type = 'date'



class AddPatient(forms.ModelForm):
    choices = (
        ('Yes','Yes'),
        ('No','No'),
    )
    pos_or_neg = (
        ('Positive','Positive'),
        ('Negative','Negative')
    )
    swab_taken = forms.TypedChoiceField(
        required=False,
        choices=choices,
        widget=forms.RadioSelect
    )
    hrct_taken = forms.TypedChoiceField(
        required=False,
        choices=choices,
        widget=forms.RadioSelect
    )
    ct_thorax_taken = forms.TypedChoiceField(
        required=False,
        choices=choices,
        widget=forms.RadioSelect
    )
    positive_or_negative = forms.TypedChoiceField(
        choices=choices,
        widget=forms.RadioSelect
    )
    sex_choice = (
            ('','select'),
            ('male',"Male"),
            ('female',"Female"),
            ('other',"Other")
    )
    criticality_choice = (
            ('low',"Low"),
            ('medium',"Medium"),
            ('high',"High")
    )
    sex = forms.ChoiceField(choices=sex_choice, required=True)
    criticallity = forms.ChoiceField(choices=criticality_choice)
    # swab_taken = forms.TypedChoiceField(
    #     choices=choices,
    #     widget=forms.RadioSelect
    # )
    # hrct_taken = forms.TypedChoiceField(
    #     choices=choices,
    #     widget=forms.RadioSelect
    # )
    # ct_thorax_taken = forms.TypedChoiceField(
    #     choices=choices,
    #     widget=forms.RadioSelect
    # )
    positive_or_negative = forms.TypedChoiceField(
        required=False,
        choices=choices,
        widget=forms.RadioSelect
    )
    icmr_id = forms.CharField(required=True)
    class Meta:
        model = PatientDetails
        fields = '__all__'
        widgets = {
            'dob': DateInput(),
            'dateAdmitted' : DateInput(),
            'ct_thorax_date': DateInput(),
            'date_of_test' : DateInput(),
        }

# case Sheet form
class SymptomsForm(forms.ModelForm):
    class Meta:
        model = Symptoms
        exclude = ('patient',)
        widgets = {
            'fever_date': DateInput(),
            'cough_date' : DateInput(),
            'throat_pain_date': DateInput(),
            'breathlessness_date' : DateInput(),
            'loose_stool_date' : DateInput(),
            'body_pain_date' : DateInput(),
            'loss_smell_date' : DateInput(),
            'loss_of_taste_date' : DateInput(),
        }

class SignsForm(forms.ModelForm):
    pulse_rate = forms.CharField(required=False,
                           widget= forms.TextInput
                           (attrs={'placeholder':'/MIN'}))
    blood_pressure = forms.CharField(required=False,
                           widget= forms.TextInput
                           (attrs={'placeholder':'/MM OF HG'}))
    respiratory_rate = forms.CharField(required=False,
                           widget= forms.TextInput
                           (attrs={'placeholder':'/MIN'}))    
    spo2 =  forms.CharField(required=False,
                           widget= forms.TextInput
                           (attrs={'placeholder':'%RA'}))
    cbg =  forms.CharField(required=False,
                           widget= forms.TextInput
                           (attrs={'placeholder':'MG/DC'}))
    temperature =  forms.CharField(required=False,
                           widget= forms.TextInput
                           (attrs={'placeholder':'/F'}))

    class Meta:
        model = Signs
        exclude = ('patient',)
        # widgets = {
        #     'pulse_rate': forms.CharField(attrs={'placeholder': 'rate'})
        # }



class PastHistoryForm(forms.ModelForm):
    class Meta:
        model = PastHistory
        exclude = ('patient',)


class ExaminationForm(forms.ModelForm):
    choices = (
        ('normal','Normal'),
        ('abnormal','Abnormal'),
    )

    respiratory_system = forms.ChoiceField(
        required=False,
        choices=choices,
        widget=forms.RadioSelect
    )
    cardiovascular_system = forms.ChoiceField(
        required=False,
        choices=choices,
        widget=forms.RadioSelect
    )
    gastrointestinal = forms.ChoiceField(
        required=False,
        choices=choices,
        widget=forms.RadioSelect
    )
    cns = forms.ChoiceField(
        required=False,
        choices=choices,
        widget=forms.RadioSelect
    )

    respiratory_choices = (
        ('','select'),
        ('BILATERAL AIR ENTRY','BILATERAL AIR ENTRY'),
        ('NVBS','NVBS'),
        ('NO ADDED SOUNDS','NO ADDED SOUNDS')
    )
    cardiovascular_choices = (
        ('','select'),
        ('S1 + S2', 'S1 + S2'),
        ('NO MURMYRS', 'NO MURMYRS'),
    )
    gastro_choices = (
        ('','select'),
        ('SOFT, NON-TENDER', 'SOFT, NON-TENDER'),
        ('BS+', 'BS+'),
    )
    cns_choices = (
        ('','select'),
        ('HMF N', 'HMF N'),
        ('NO FND', 'NO FND'),
        ('GCS:15/15', 'GCS:15/15'),
    )

    respiratory_normal = forms.ChoiceField(choices=respiratory_choices,required=False)
    cardiovascular_normal = forms.ChoiceField(choices=cardiovascular_choices,required=False)
    gastrointestinal_normal = forms.ChoiceField(choices=gastro_choices,required=False)
    cns_normal = forms.ChoiceField(choices=cns_choices,required=False)


    class Meta:
        model = Examination
        exclude = ('patient',)


class DifferentialDiagnosisForm(forms.ModelForm):
    class Meta:
        model = DifferentialDiagnosis
        exclude = ('patient',)


class MicrobiologyForm(forms.ModelForm):
    class Meta:
        model = Microbiology
        exclude = ('patient',)
        widgets = {
            'rt_pcr_covid_date': DateInput(),
            'rapid_anti_body_date' : DateInput(),
            'rt_pcr_H1N_date': DateInput(),
            'viral_culture_date' : DateInput(),
            'viral_culture_date2' : DateInput()
        }


class TreatmentForm(forms.ModelForm):

    choice = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10'),
        ('11','11'),
        ('12','12'),
    )


    o2 = forms.ChoiceField(choices=choice)
    nebulisation_budocort_qh = forms.ChoiceField(choices=choice)
    nebulisation_duolin_qh = forms.ChoiceField(choices=choice)
    class Meta:
        model = Treatment
        exclude = ('patient',)






























# class RTPCR_Detail(forms.ModelForm):
#     choices = (
#         ('Yes','Yes'),
#         ('No','No'),
#     )
#     pos_or_neg = (
#         ('Positive','Positive'),
#         ('Negative','Negative')
#     )
#     swab_taken = forms.TypedChoiceField(
#         choices=choices,
#         widget=forms.RadioSelect
#     )
#     hrct_taken = forms.TypedChoiceField(
#         choices=choices,
#         widget=forms.RadioSelect
#     )
#     ct_thorax_taken = forms.TypedChoiceField(
#         choices=choices,
#         widget=forms.RadioSelect
#     )
#     positive_or_negative = forms.TypedChoiceField(
#         choices=choices,
#         widget=forms.RadioSelect
#     )
#     class Meta:
#         model = RT_PCR_Details
#         fields = '__all__'
#         widgets = {
#             'ct_thorax_date': DateInput(),
#             'date_of_test' : DateInput()
#         }
        
