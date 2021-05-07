from django import forms


class DoctorForm(forms.Form):
    sexChoices = (
        ('male','Male'),
        ('female','Female'),
        ('other','Other'),
    )
    username = forms.CharField(max_length=50,label='User Name', required=True)
    firstname = forms.CharField(max_length=50, label='First Name', required=True)
    lastname = forms.CharField(max_length=50, label='Last Name', required=True)
    sex = forms.ChoiceField(choices=sexChoices, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(), required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(), required=True)