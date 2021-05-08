from django.urls import path
from . import views

urlpatterns = [
    path('<int:patient_id>/<int:day>', views.CaseSheet, name='CaseSheet'),
]