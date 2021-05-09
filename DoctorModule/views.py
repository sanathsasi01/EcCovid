from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages

from AdminModule.forms import DoctorForm

from PatientModule.forms import *
from PatientModule.models import PatientDetails

from DoctorModule.models import DoctorPatientRelation


from django.contrib.auth import get_user_model
User = get_user_model() 

def doctorPage(request):
    doc_id = request.user.id
    patients = PatientDetails.objects.filter(doctor=doc_id)

    # forms
    AddPatientForm  = AddPatient(initial={ 'doctor' : doc_id })
    PatientSymptomsForm = SymptomsForm()
    PatientSignsForm = SignsForm()
    PatientPastHistoryForm = PastHistoryForm()
    PatientExaminationForm = ExaminationForm()
    PatientDifferentialDiagnosisForm = DifferentialDiagnosisForm()
    PatientMicrobiologyForm = MicrobiologyForm()

    context = {
        'patients' : patients,
        'AddPatientForm' : AddPatientForm,
        'PatientSymptomsForm' : PatientSymptomsForm,
        'PatientSignsForm' : PatientSignsForm,
        'PatientPastHistoryForm' : PatientPastHistoryForm,
        'PatientExaminationForm' : PatientExaminationForm,
        'PatientDifferentialDiagnosisForm' : PatientDifferentialDiagnosisForm,
        'PatientMicrobiologyForm' : PatientMicrobiologyForm
    }
    return render(request, 'doctor/doctor.html', context)


def AddDoctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            sex = form.cleaned_data['sex']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'Username already taken')
                else:
                    doctor = User.objects.create_doctor(username=username, firstname=firstname, lastname=lastname, password=password1, sex=sex)
                    doctor.save()
                    form = DoctorForm()
                    messages.success(request, 'Doctor added suuccessfuly')
            else:
                messages.error(request, 'Passwords does not match')
        return redirect('adminPage')
            
                    

