from datetime import datetime

from crispy_forms.helper import FormHelper
from django.forms import ModelForm
from .models import Appointment
from django import forms
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Row, Field, HTML


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ('first_name', 'last_name', 'email', 'date_of_appointment', 'phone_number', 'gender', 'image_appointment', 'message')
        widgets = {
            'date_of_appointment': forms.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(

            Row(Field('first_name', ), ),
            Field('last_name', ),
            Field('gender', ),
            Row(Field('gender'), ),
        )

        for name, fiels in self.fields.items():
            self.fields[name].widget.attrs.update({'class': 'input'})
