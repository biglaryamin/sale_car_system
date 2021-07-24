from django import forms
from .models import *





class Person_form(forms.ModelForm):
    class Meta:
        model = Person
        fields="__all__"




class Buy_car_form(forms.ModelForm):
    class Meta:
        model = Car
        fields="__all__"

