from django.urls import path
from . import views

app_name = 'appointment'

urlpatterns = [
    path('', views.appointments, name='appointments'),

    path('appointment/<str:pk>/', views.appointment, name='appointment'),
    path('create-appointment/', views.createAppointment, name='make-appointment'),
    path('edit-appointment/<str:pk>/', views.updateAppointment, name='edit-appointment'),
    path('delete-appointment/<str:pk>/', views.deleteAppointment, name='delete-appointment'),
]
