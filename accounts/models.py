from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.utils.translation import gettext_lazy as _
from django.utils.html import escape, mark_safe
from django.conf import settings


class CustomerUser(AbstractUser):
    is_doctor = models.BooleanField("Doctor", default=False)
    is_patient = models.BooleanField('Patient', default=False)
    created = models.DateTimeField(auto_now_add=True)  # auto_now_add, creates automatic timestamp


class DoctorProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    speciality = models.CharField(max_length=200, blank=True, null=True)
    degrees = models.CharField(max_length=200, blank=True, null=True)
    experience = models.CharField(max_length=200, blank=True, null=True)
    short_intro = models.CharField(max_length=200, blank=True, null=True)
    training = models.TextField(blank=True, null=True)
    work_days = models.CharField(max_length=200, blank=True, null=True)
    profile_image = models.ImageField(
        null=True, blank=True, upload_to='profiles/authors_profiles', default="profiles/user-default.png")
    social_github = models.CharField(max_length=200, blank=True, null=True)
    social_twitter = models.CharField(max_length=200, blank=True, null=True)
    social_linkedin = models.CharField(max_length=200, blank=True, null=True)
    social_youtube = models.CharField(max_length=200, blank=True, null=True)
    social_website = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.username)

    class Meta:
        ordering = ['created']


class PatientProfile(models.Model):
    # relation to user
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(_('name'), max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    username = models.CharField(_('Username'), max_length=200, blank=True, null=True)
    date_of_birth = models.DateField(_('date_of_birth'), null=True, blank=True)
    profile_image = models.ImageField(
        _('profile_image'), null=True, blank=True, upload_to='profiles/customers_profile', default="profiles/user"
                                                                                                "-default.png")
    adress = models.CharField(_('adress'), max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.username)

    class Meta:
        ordering = ['created']
