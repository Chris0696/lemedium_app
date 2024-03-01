from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.views.generic import CreateView, TemplateView
from django.utils.translation import gettext_lazy as _
from appointment.models import Appointment
from ..models import DoctorProfile, PatientProfile
from ..forms import PatientRegisterForm

User = get_user_model()


class SignUpView(TemplateView):
    template_name = 'accounts/signup_form.html'


def index(request):
    profiles = DoctorProfile.objects.all()

    appments = Appointment.objects.all()

    print(profiles)

    context = {'profiles': profiles}
    return render(request, 'accounts/index.html', context)


def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, _('Username does not exist'))

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('appointment:appointments')


    return render(request, 'accounts/login_form.html')


def logoutUser(request):
    logout(request)
    # print('User was logged out!')
    messages.info(request, _('You have logged out'))
    return redirect('accounts:login')


def aboutUs(request):
    return render(request, 'accounts/about_us.html')


def contact(request):
    return render(request, 'accounts/contact.html')


def doctorsProfiles(request):
    profiles = DoctorProfile.objects.all()

    print(profiles)

    context = {'profiles': profiles}
    return render(request, 'accounts/doctors_profiles.html', context)


def doctorProfile(request, pk):
    profile = DoctorProfile.objects.get(id=pk)

    '''print(profile.project)'''

    context = {'profile': profile}
    return render(request, 'accounts/doctor_profile.html', context)


def patientsProfiles(request):
    profiles = PatientProfile.objects.all()

    context = {'profiles': profiles}
    return render(request, 'accounts/patients_profiles.html', context)


def patientProfile(request, pk):
    profile = PatientProfile.objects.get(id=pk)
    print(profile.name)
    '''print(profile.project)'''

    context = {'profile': profile}
    return render(request, 'accounts/patient_profile.html', context)


def service(request):
    return render(request, 'accounts/service.html')

