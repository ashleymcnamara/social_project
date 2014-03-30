from django.forms import ModelForm
from django import forms
import django.forms
from django.forms.widgets import PasswordInput
from django.forms.extras.widgets import Select

from apps.lists.models import *


class LISTInputForm(ModelForm):
    timeString = forms.CharField(max_length=100)

    class Meta:
        model = LIST
        exclude = ('user', 'completed', 'time')

    def clean_time(self):
        pass



class DeleteLISTForm(ModelForm):
    class Meta:
        model = LIST
        fields = []