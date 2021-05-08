from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import *
from DoctorModule.models import DoctorPatientRelation
from django .contrib.auth import get_user_model

User = get_user_model()

# patient registraion functions


def AddPatients(request):
    if request.method == 'POST':
        form1 = AddPatient(request.POST)
        form2 = SymptomsForm(request.POST)
        form3 = SignsForm(request.POST)

        is_form1_valid = form1.is_valid()
        is_form2_valid = form2.is_valid()
        is_form3_valid = form3.is_valid()


        if is_form1_valid  and is_form2_valid and is_form3_valid:

            patient_instance = form1.save()
            form2_instance = form2.save(commit=False)
            form2_instance.patient = patient_instance
            form2_instance.save()

            form3_instance = form3.save(commit=False)
            form3_instance.patient = patient_instance
            form3_instance.save()

            messages.success(request, 'patient added successfuly')
        else:
            messages.error(request, 'something went wrong, try again')
        return redirect('doctorPage')
        
# def AddPatients(request):
#     if request.method == 'POST':
#         form = AddPatient(request.POST)

#         if form.is_valid():
#             try:
#                 patient=form.save()
#                 # messages.success(request, 'Patient added successfuly')
                
#                 return render(request, 'patients/caseSheet.html')
#             except:
#                 messages.error(request, 'Something wrong try again')
#                 return redirect('doctorPage')
#         else:
#             print(form.errors)
#             messages.error(request, 'Patient not added')
#         return redirect('doctorPage')   

def CaseSheet(request):
    pass

