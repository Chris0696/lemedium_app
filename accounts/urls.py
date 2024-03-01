from django.urls import path
from .views import cmedium

app_name = 'accounts'

urlpatterns = [
    path('', cmedium.index, name='index'),

    path('login/', cmedium.loginUser, name='login'),
    path('logout/', cmedium.logoutUser, name='logout'),

    path('about-us/', cmedium.aboutUs, name='about'),

    path('contact/', cmedium.contact, name='contact'),

    path('service/', cmedium.service, name="service"),

    path('doctors-profiles/', cmedium.doctorsProfiles, name="doctors-profiles"),
    path('doctor/profile/<str:pk>/', cmedium.doctorProfile, name="doctor-profile"),

    path('patient/', cmedium.patientsProfiles, name="patients-profiles"),
    path('patient/profile/<str:pk>/', cmedium.PatientProfile, name="patient-profile"),

]
