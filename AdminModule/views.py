from django.shortcuts import render
from .forms import DoctorForm

# Create your views here.


def adminPage(request):
    form = DoctorForm()
    context = {
        'form' : form
    }
    return render(request, 'admin/admin.html', context)