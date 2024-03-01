from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.db import transaction
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from ..decorators import doctor_required
from ..forms import DoctorRegisterForm, DoctorProfileForm
from ..models import DoctorProfile

User = get_user_model()


class RegisterDoctor(CreateView):
    model = User
    form_class = DoctorRegisterForm
    template_name = 'accounts/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'doctor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, 'Author created successfully!')
        login(self.request, user)
        return redirect('accounts:doctors-profiles')


@login_required(login_url='users:login')
def doctorAccount(request):
    profile = request.user.profile

    context = {'profile': profile}

    return render(request, 'accounts/doctor_account.html', context)


@login_required(login_url='users:login')
@doctor_required
def EditAuthorAccount(request):
    profile = request.user.profile
    form = DoctorProfileForm(instance=profile)

    if request.method == 'POST':
        form = DoctorProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('accounts:doctor-account')

    context = {'form': form}
    return render(request, 'accounts/doctor_profile_form.html', context)


