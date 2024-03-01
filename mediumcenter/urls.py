from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import patients, doctors, cmedium


urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('rosetta/', include('rosetta.urls')),
    path('blog/', include('blogs.urls')),
    path('', include('accounts.urls')),
    path('appointment/', include('appointment.urls')),

    path('accounts/', include('django.contrib.auth.urls')),

    path('accounts/register/doctor/', doctors.RegisterDoctor.as_view(), name='doctor_register'),

    path('accounts/register/patient/', patients.RegisterPatient.as_view(), name='patient_register'),
    path('accounts/signup/', cmedium.SignUpView.as_view(), name='signup'),
    path('edit-account/patient/', patients.EditPatientAccount, name="edit-patient-account"),
    path('edit-account/doctor/', doctors.EditAuthorAccount, name="edit-doctor-account"),
    path('account/doctor/', doctors.doctorAccount, name="doctor-account"),
    path('account/patient/', patients.patientAccount, name="patient-account"),

    prefix_default_language=False

)


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
