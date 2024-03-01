from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Appointment
from .forms import AppointmentForm
from accounts.decorators import patient_required


def appointments(request):
    appments = Appointment.objects.all()

    context = {'appments': appments}
    return render(request, 'appointment/appointments.html', context)


def appointment(request, pk):
    appmentObj = Appointment.objects.get(id=pk)

    context = {'project': appmentObj}
    return render(request, 'appointment/single-appointments.html', context)


@login_required(login_url='accounts:login')
def createAppointment(request):
    patientprofile = request.user.patientprofile
    form = AppointmentForm()

    if request.method == 'POST':
        form = AppointmentForm(request.POST, request.FILES)
        if form.is_valid():
            appments = form.save(commit=False)
            appments.patient = patientprofile
            appments.save()
            messages.success(request, 'Appointment was created successfully!')
            return redirect('patient-account')

    context = {'form': form}
    return render(request, 'appointment/appointment_form.html', context)


@login_required(login_url='users:login')
@patient_required
def updateAppointment(request, pk):
    profile = request.user.profile
    appments = profile.project_set.get(id=pk)
    form = AppointmentForm(instance=appments)

    if request.method == 'POST':
        form = AppointmentForm(request.POST, request.FILES, instance=appments)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project was update successfully!')
            return redirect('author-account')

    context = {'form': form}
    return render(request, 'appointment/appointment_form.html', context)


@login_required(login_url='accounts:login')
@patient_required
def deleteAppointment(request, pk):
    profile = request.user.profile
    appments = profile.project_set.get(id=pk)
    if request.method == 'POST':
        appments.delete()
        messages.success(request, 'Project was deleted successfully!')
        return redirect("author-account")
    context = {'object': appments}
    return render(request, 'delete_template.html', context)

