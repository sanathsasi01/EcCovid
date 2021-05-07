from django import forms
from .models import PatientDetails

# class AddPatient(forms.Form):
#     sex_choice = (
#         ('male','Male'),
#         ('female','Female'),
#         ('other','Other'),
#     )
#     firstname = forms.CharField(label='First Name', max_length=30)
#     lastname = forms.CharField(label='Last Name', max_length=30)
#     sex = forms.ChoiceField(choices=sex_choice)
    
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
    sex = forms.ChoiceField(choices=sex_choice)
    criticallity = forms.ChoiceField(choices=criticality_choice)
    class Meta:
        model = PatientDetails
        fields = '__all__'
        
