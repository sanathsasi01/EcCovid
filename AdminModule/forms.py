from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class DoctorForm(forms.Form):
    sexChoices = (
        ('male','Male'),
        ('female','Female'),
        ('other','Other'),
    )
    username = forms.CharField(max_length=50,label='User Name', required=True,widget= forms.TextInput(
                           attrs={'class':'some_class','id':'some_id'}))
    firstname = forms.CharField(max_length=50, label='First Name', required=True)
    lastname = forms.CharField(max_length=50, label='Last Name', required=True)
    sex = forms.ChoiceField(choices=sexChoices, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(), required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(), required=True)



# class DoctorForm(forms.ModelForm):
#     sexChoices = (
#         ('male','Male'),
#         ('female','Female'),
#         ('other','Other'),
#     )
#     sex = forms.ChoiceField(choices=sexChoices, required=True)
#     class Meta:
#         model = User
#         fields = '__all__'