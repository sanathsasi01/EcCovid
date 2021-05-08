from django.shortcuts import render, redirect
from .forms import CaseFileForm
from django.contrib import messages
from DoctorModule.models import DoctorPatientRelation
# Create your views here.


def CaseSheet(request, patient_id=None, day=None):
    if request.method == 'POST':
        form = CaseFileForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            messages.error(request, 'Adding casefile failed, try again')
        return redirect('doctorPage')
    else:           
        doc_pat_relation = DoctorPatientRelation.objects.get(patient=patient_id, doctor=request.user.id)
        # print(doc_pat_relation)
        form = CaseFileForm(initial={
            'day' : day,
            'doc_pat_relation' : doc_pat_relation.id
        })
        context = {
            'form' : form
        }
        return render(request, 'doctor/caseFileForm.html', context)