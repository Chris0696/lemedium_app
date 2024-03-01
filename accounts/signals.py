from django.db.models.signals import post_save, post_delete

from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import *
from django.conf import settings
from django.core.mail import send_mail
from django.conf import settings


@receiver(post_save, sender=settings.AUTH_USER_MODEL)  # listens to user model, we want it to notice if a new user is
# added and create a profile
def createProfile(sender, instance, created, **kwargs):
    print('Profile signal triggered')
    if created:
        user = instance

        if user.is_doctor:

            profile = DoctorProfile.objects.create(
                user=user,
                username=user.username,
                email=user.email,
                name=user.first_name,
            )
            profile.save()

        elif user.is_patient:

            patientprofile = PatientProfile.objects.create(
                user=user,
                username=user.username,
                email=user.email,
                name=user.first_name,
            )
            patientprofile.save()

        # subject = 'Welcome to DevSearch'
        # message = "We are glad you are here!"

        # send_mail(
        #     subject,
        #     message,
        #     settings.EMAIL_HOST_USER,
        #     [profile.email],
        #     fail_silently=False,
        # )


@receiver(post_save, sender=PatientProfile)
def updatePatient(sender, instance, created, **kwargs):
    patientprofile = instance
    user = patientprofile.user

    if not created:  # ensures consistency between user and profile (avoid recursion erorr)
        # User.objects.create(username=profile.username, email=profile.username, first_name=profile.first_name,
        # last_name=profile.last_name, is_participant=True) else:

        user.first_name = patientprofile.name
        user.username = patientprofile.username
        user.email = patientprofile.email
        user.is_patient = True
        user.save()


@receiver(post_save, sender=DoctorProfile)
def updateDoctor(sender, instance, created, **kwargs):
    doctorprofile = instance
    user = doctorprofile.user

    if not created:  # ensures consistency between user and profile (avoid recursion erorr)
        user.first_name = doctorprofile.name
        user.username = doctorprofile.username
        user.email = doctorprofile.email
        user.is_doctor = True
        user.save()


@receiver(post_delete, sender=PatientProfile)  # listens to profile, we want it to notice if a profile is delete
# and delete the user too
def deleteAuthor(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass


@receiver(post_delete, sender=DoctorProfile)  # listens to profile, we want it to notice if a profile is delete
# and delete the user too
def deleteCustomer(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass
