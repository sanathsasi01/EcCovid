from django.urls import path
from . import views

urlpatterns = [
    path('', views.AddPatients, name='AddPatient' )
    # path('case-sheet/', views.CaseSheet, name='CaseSheet')
]