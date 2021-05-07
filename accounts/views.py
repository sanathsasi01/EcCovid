from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages


from django.contrib.auth import get_user_model
User = get_user_model() 
# import uuid




# def registration(request):
#     hospitals = HospitalDetails.objects.all()

#     # myuuid = uuid.uuid4()

#     # print('Your UUID is: ' + str(myuuid))

#     return render(request, 'accounts/registration.html', {'hospitals' : hospitals})


# user registration
def sign_up(request):
    if request.method == 'POST':
        email = request.POST['email']
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, ' Email already in use ')
                return redirect('registration')
            else:
                # patient reg
                if request.POST.get('patient') is not None:
                    patient = User.objects.create_patient(email=email, firstname=firstname, lastname=lastname, password=password1)
                    details = PatientDetails(patient=patient)
                    details.save()
                    messages.info(request, ' Registration successfull ')
                    return redirect('registration')
                # hospital reg               
                elif request.POST.get('hospital') is not None:
                    branch = request.POST['branch']

                    hospital = User.objects.create_hospital(email=email, firstname=firstname, password=password1)
                    HosDetails = HospitalDetails(hospital=hospital, branch=branch)
                    HosDetails.save()
                    return redirect('adminPage')
                # doctor reg
                else:
                    if request.POST['hospitalname'] == None:
                        messages.info(request, ' Select a hospital ')
                        return redirect('registration')
                    else:
                        hospital_id = request.POST['hospitalname']
                        hospital_obj = HospitalDetails.objects.get(id=hospital_id)
                        
                        doc = User.objects.create_doctor(email=email, firstname=firstname,lastname=lastname, password=password1)

                        approval = DoctorDetails(doctor=doc, hospital=hospital_obj)
                        approval.save()
                        
                        return redirect('registration')
                    # return redirect('adminPage')
        else:
            messages.info(request, ' Passwords does not match ')
            return redirect('registration')

# user login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.admin:
                # response = redirect('adminPage')
                # response.set_cookie('username', username)
                login(request, user)         
                return redirect('adminPage')
            else:
                login(request, user)         
                return redirect('doctorPage')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')



def userPage(request):
    return HttpResponse('<h1>Welcome Rogi</h1>')

# user logout
def logout_view(request):
    # del request.session['username']
    logout(request)
    return redirect('login')