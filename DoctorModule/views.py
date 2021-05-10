from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

from AdminModule.forms import DoctorForm

from PatientModule.forms import *
from PatientModule.models import PatientDetails

from DoctorModule.models import DoctorPatientRelation


from django.contrib.auth import get_user_model
User = get_user_model() 



def criticalityChange(request):
    if request.is_ajax and request.method == 'GET':
        newCriticality = request.GET.get('newCriticality', None)
        # print(newCriticality)
        patientid = request.GET.get('patientId', None)
        # print(patientid)
        try:
            patient = PatientDetails.objects.get(id=patientid)
            patient.criticallity = newCriticality
            patient.save()
            return HttpResponse("")
        except:
            messages.error(request, 'Something went wrong, try again')
            return redirect('doctorPage')

        


def doctorPage(request):
    doc_id = request.user.id
    # patients = PatientDetails.objects.filter(doctor=doc_id)
    patients = PatientDetails.objects.order_by('dateAdmitted')
    if request.method == 'POST':
        AddPatientForm = AddPatient(request.POST)
        PatientSymptomsForm = SymptomsForm(request.POST)
        PatientSignsForm = SignsForm(request.POST)
        PatientPastHistoryForm = PastHistoryForm(request.POST)
        PatientExaminationForm = ExaminationForm(request.POST)
        PatientDifferentialDiagnosisForm = DifferentialDiagnosisForm(request.POST)

        PatientMicrobiologyForm = MicrobiologyForm(request.POST)
        patientTreatmentForm = TreatmentForm(request.POST)

        is_AddPatientForm_valid = AddPatientForm.is_valid()
        is_PatientSymptomsForm_valid = PatientSymptomsForm.is_valid()
        is_PatientSignsForm_valid = PatientSignsForm.is_valid()
        is_PatientPastHistoryForm_valid = PatientPastHistoryForm.is_valid()
        is_PatientExaminationForm_valid = PatientExaminationForm.is_valid()
        is_PatientDifferentialDiagnosisForm_valid = PatientDifferentialDiagnosisForm.is_valid()
        is_PatientMicrobiologyForm_valid = PatientMicrobiologyForm.is_valid()
        is_patientTreatmentForm_valid = patientTreatmentForm.is_valid()

        if is_AddPatientForm_valid  and is_PatientSignsForm_valid and is_PatientSymptomsForm_valid and is_PatientPastHistoryForm_valid and is_PatientExaminationForm_valid and is_PatientDifferentialDiagnosisForm_valid and is_PatientMicrobiologyForm_valid and is_patientTreatmentForm_valid :

            patient_instance = AddPatientForm.save()

            PatientSymptomsForm_instance = PatientSymptomsForm.save(commit=False)
            PatientSymptomsForm_instance.patient = patient_instance
            PatientSymptomsForm_instance.save()

            PatientSignsForm_instance = PatientSignsForm.save(commit=False)
            PatientSignsForm_instance.patient = patient_instance
            PatientSignsForm_instance.save()

            PatientPastHistoryForm_instance = PatientPastHistoryForm.save(commit=False)
            PatientPastHistoryForm_instance.patient = patient_instance
            PatientPastHistoryForm_instance.save()

            PatientExaminationForm_instance = PatientExaminationForm.save(commit=False)
            PatientExaminationForm_instance.patient = patient_instance
            PatientExaminationForm_instance.save()

            PatientDifferentialDiagnosisForm_instance = PatientDifferentialDiagnosisForm.save(commit=False)
            PatientDifferentialDiagnosisForm_instance.patient = patient_instance
            PatientDifferentialDiagnosisForm_instance.save()

            PatientMicrobiologyForm_instance = PatientMicrobiologyForm.save(commit=False)
            PatientMicrobiologyForm_instance.patient = patient_instance
            PatientMicrobiologyForm_instance.save()

            patientTreatmentForm_instance = patientTreatmentForm.save(commit=False)
            patientTreatmentForm_instance.patient = patient_instance
            patientTreatmentForm_instance.save()

            messages.success(request, 'patient added successfuly')
        else:
            print(AddPatientForm.errors)
            print(PatientSymptomsForm.errors)
            print(PatientSignsForm.errors)
            print(PatientPastHistoryForm.errors)
            print(PatientExaminationForm.errors)
            print(PatientDifferentialDiagnosisForm.errors)
            print(PatientMicrobiologyForm.errors)
            print(patientTreatmentForm.errors)
            messages.error(request, 'something went wrong, try again')
    else:
        # forms
        AddPatientForm  = AddPatient(initial={ 'doctor' : doc_id })
        PatientSymptomsForm = SymptomsForm(use_required_attribute=False)
        PatientSignsForm = SignsForm(use_required_attribute=False)
        PatientPastHistoryForm = PastHistoryForm(use_required_attribute=False)
        PatientExaminationForm = ExaminationForm(use_required_attribute=False)
        PatientDifferentialDiagnosisForm = DifferentialDiagnosisForm(use_required_attribute=False)
        PatientMicrobiologyForm = MicrobiologyForm(use_required_attribute=False)
        patientTreatmentForm = TreatmentForm(use_required_attribute=False)

    context = {
        'patients' : patients,
        'AddPatientForm' : AddPatientForm,
        'PatientSymptomsForm' : PatientSymptomsForm,
        'PatientSignsForm' : PatientSignsForm,
        'PatientPastHistoryForm' : PatientPastHistoryForm,
        'PatientExaminationForm' : PatientExaminationForm,
        'PatientDifferentialDiagnosisForm' :PatientDifferentialDiagnosisForm,
        'PatientMicrobiologyForm' : PatientMicrobiologyForm,
        'patientTreatmentForm' : patientTreatmentForm,


    }
    return render(request, 'doctor/dashboard.html', context)


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
            
                    

