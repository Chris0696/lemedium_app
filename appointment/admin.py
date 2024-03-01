from django.contrib import admin
from .models import *


class AdminAppointment(admin.ModelAdmin):

    list_display = ('first_name', 'last_name', 'email', 'date_of_appointment', 'message')


admin.site.register(Appointment, AdminAppointment)
