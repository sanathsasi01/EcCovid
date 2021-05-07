from django.urls import path
from . import views

urlpatterns = [
    path('', views.AddPatients, name='AddPatient' )
]