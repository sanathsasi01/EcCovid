from django.shortcuts import render, redirect, HttpResponseRedirect
from AdminModule.forms import DoctorForm
from django.contrib import messages
from PatientModule.forms import AddPatient
from django.contrib.auth import get_user_model
User = get_user_model() 

def doctorPage(request):
    form  = AddPatient()
    return render(request, 'doctor/doctor.html', {'form':form})


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
            # return redirect('adminPage')

            # return render(request, 'admin/admin.html', {'form':form})
        return redirect('adminPage')
            
                    

