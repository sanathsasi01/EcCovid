from .models import CaseFile
from django import forms



class CaseFileForm(forms.ModelForm):
    # respiratory = forms.CharField(widget=forms.TextInput(
    #     attrs={
    #         'id' : 'respiratory'
    #     }
    # ))
    class Meta:
        model = CaseFile
        fields = '__all__'