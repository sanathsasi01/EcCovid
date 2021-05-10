from django.urls import path
from . import views

urlpatterns = [
    path('', views.AddDoctor, name='AddDoctor'),
    path('docx/', views.doctorPage, name='doctorPage'),
    path('criticalityChange/', views.criticalityChange, name='criticalityChange'),

]