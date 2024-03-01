from datetime import datetime

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from django.urls import reverse_lazy
from django.contrib.auth.models import Group
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import *

User = get_user_model()


class PatientRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']
        labels = {
            'first_name': 'Name'

        }

    def __init__(self, *args, **kwargs):
        super(PatientRegisterForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('patient_register')
        self.helper.form_method = 'POST'

        for name, fiels in self.fields.items():
            self.fields[name].widget.attrs.update({'class': 'input'})
            self.fields[name].help_text = None

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_patient = True
        user.username = user.username.lower()
        if commit:
            user.save()
        return user


class DoctorRegisterForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']
        labels = {
            'first_name': 'Name'
        }

    def __init__(self, *args, **kwargs):
        super(DoctorRegisterForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('doctor_register')
        self.helper.form_method = 'POST'

        for name, fiels in self.fields.items():
            self.fields[name].widget.attrs.update({'class': 'input'})
            self.fields[name].help_text = None

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_doctor = True
        user.username = user.username.lower()
        user.save()

        return user


class DoctorProfileForm(ModelForm):
    class Meta:
        model = DoctorProfile
        fields = ['username', 'name', 'email', 'location', 'short_intro', 'speciality', 'degrees', 'experience',
                  'work_days', 'training', 'profile_image', 'social_github', 'social_twitter', 'social_linkedin', 'social_youtube', 'social_website']
        widgets = {
            'grade': forms.CheckboxSelectMultiple
        }

    def __init__(self, *args, **kwargs):
        super(DoctorProfileForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('users:author-account')
        self.helper.form_method = 'POST'

        for name, fiels in self.fields.items():
            self.fields[name].widget.attrs.update({'class': 'input'})


class PatientProfileForm(ModelForm):
    class Meta:
        model = PatientProfile
        fields = ['username', 'name', 'email', 'date_of_birth', 'adress', 'profile_image']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'max': datetime.now().date()})
        }

    def __init__(self, *args, **kwargs):
        super(PatientProfileForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('patient-account')
        self.helper.form_method = 'POST'

        for name, fiels in self.fields.items():
            self.fields[name].widget.attrs.update({'class': 'input'})

