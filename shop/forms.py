# from django.forms import ModelForm
# from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Address

class RegirationForm(UserCreationForm):
    first_name=forms.CharField(max_length=200)
    last_name=forms.CharField(max_length=200)
    email=forms.EmailField()

# class StudentForm(ModelForm):
#     class Meta:
#         model=Student
#         fields='__all__'
class AddressForm(forms.ModelForm):
    class Meta:
        model=Address
        exclude=("user",)
