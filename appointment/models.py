from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _
from django.db.models.deletion import CASCADE
from django.urls import reverse
from accounts.models import PatientProfile


# Create your models here.


class Appointment(models.Model):
    patient = models.ForeignKey(PatientProfile, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(_('first_name'), max_length=200, null=True, blank=True)
    last_name = models.CharField(_('last_name'), max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=500, null=True, blank=True)
    image_appointment = models.ImageField(
      _('image_appointment'), null=True, blank=True, upload_to='profiles/customers_profile', default="profiles/user"
                                                                                                     "-default.png"
    )
    date_of_appointment = models.DateField(_('date_of_appointment'), null=True, blank=True)
    phone_number = models.CharField(_('phone_number'), max_length=200, null=True, blank=True)
    gender = models.CharField(_('gender'), max_length=200, null=True, blank=True,
                              choices=[('M', _('Male')), ('F', _('Female')), ('C', _('Child')), ('O', _('Other'))])
    message = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.first_name)

    class Meta:
        ordering = ['created']
