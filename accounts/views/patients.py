from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from appointment.models import Appointment
from ..decorators import patient_required

from ..forms import PatientRegisterForm, PatientProfileForm
from ..models import PatientProfile

User = get_user_model()


class RegisterPatient(CreateView):
    model = User
    form_class = PatientRegisterForm
    template_name = 'accounts/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'patient'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, 'User created successfully!')
        login(self.request, user)
        return redirect('accounts:index')


@login_required(login_url='accounts:login')
def patientAccount(request):
    patientprofile = request.user.patientprofile

    appments = Appointment.objects.all()

    context = {'patientprofile': patientprofile, 'appments': appments}
    return render(request, 'accounts/patient_account.html', context)


@login_required(login_url='accounts:login')
@patient_required()
def EditPatientAccount(request):
    patientprofile = request.user.patientprofile
    form = PatientProfileForm(instance=patientprofile)

    if request.method == 'POST':
        form = PatientProfileForm(request.POST, request.FILES, instance=patientprofile)
        if form.is_valid():
            form.save()

            return redirect('patient-account')

    context = {'form': form}
    return render(request, 'accounts/patient_profile_form.html', context)
