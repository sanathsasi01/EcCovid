from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import AddPatient


def AddPatients(request):
    if request.method == 'POST':
        form = AddPatient(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient added successfuly')
        else:
            messages.error(request, 'Patient not added')
        return redirect('doctorPage')   