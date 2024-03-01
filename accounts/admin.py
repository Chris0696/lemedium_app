from django.contrib import admin
from .models import *


# Register your models here.


class CustomerUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_doctor', 'is_patient')


class PatientProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'username', 'email', 'created', 'id')


class DoctorProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'username', 'email', 'created', 'id')


admin.site.register(CustomerUser, CustomerUserAdmin)

admin.site.register(DoctorProfile, DoctorProfileAdmin)

admin.site.register(PatientProfile, PatientProfileAdmin)

