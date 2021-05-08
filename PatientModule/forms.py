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
    sex = forms.ChoiceField(choices=sex_choice)
    criticallity = forms.ChoiceField(choices=criticality_choice)
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
    class Meta:
        model = PatientDetails
        fields = '__all__'
        widgets = {
            'dob': DateInput(),
            'dateAdmitted' : DateInput(),
            'ct_thorax_date': DateInput(),
            'date_of_test' : DateInput()
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
    class Meta:
        model = Signs
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
        
