from django import forms
from .models import *


# custom date filter
class DateInput(forms.DateInput):
    input_type = 'date'



class AddPatient(forms.ModelForm):
    sex_choice = (
            ('male',"Male"),
            ('female',"Female"),
            ('other',"Other")
    )
    criticality_choice = (
            ('low',"Low"),
            ('medium',"Medium"),
            ('high',"High")
        )
    choices = (
        ('Yes','Yes'),
        ('No','No'),
    )
    pos_or_neg = (
        ('Positive','Positive'),
        ('Negative','Negative')
    )
    swab_taken = forms.TypedChoiceField(
        choices=choices,
        widget=forms.RadioSelect
    )
    hrct_taken = forms.TypedChoiceField(
        choices=choices,
        widget=forms.RadioSelect
    )
    ct_thorax_taken = forms.TypedChoiceField(
        choices=choices,
        widget=forms.RadioSelect
    )
    positive_or_negative = forms.TypedChoiceField(
        choices=choices,
        widget=forms.RadioSelect
    )
    sex = forms.ChoiceField(choices=sex_choice)
    criticallity = forms.ChoiceField(choices=criticality_choice)
    class Meta:
        model = PatientDetails
        fields = '__all__'
        # exclude = ['doctor']
        widgets = {
            'dob': DateInput(),
            'dateAdmitted' : DateInput(),
            'ct_thorax_date': DateInput(),
            'date_of_test' : DateInput()
        }

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
#         exclude = ['patient']
#         widgets = {
#             'ct_thorax_date': DateInput(),
#             'date_of_test' : DateInput()
#         }
        
