from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import AddPatient
from DoctorModule.models import DoctorPatientRelation
from django .contrib.auth import get_user_model

User = get_user_model()


def AddPatients(request):
    if request.method == 'POST':
        form = AddPatient(request.POST)
        # form2 = RTPCR_Detail(request.POST)

        if form.is_valid() :
            # doc_username = request.user.username
            # doctor = User.objects.get(username=doc_username)
            patient=form.save()
            # doc_patient_realtion = DoctorPatientRelation(patient=patient, doctor=doctor)
            # doc_patient_realtion.save()
            messages.success(request, 'Patient added successfuly')
            # except doctor.DoesNotExist:
            #     messages.error(request, 'Something went wrong, try again!')
            return redirect('doctorPage')
        else:
            print(form.errors)
            messages.error(request, 'Patient not added')
        return redirect('doctorPage')   