from django import forms
from .models import *



class measurementform(forms.ModelForm):
    class Meta:
        model=measurement
        fields =['location','destination']
