from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *




class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image','bio']


class NeibaForm(forms.ModelForm):
    class Meta:
        model = Neiba
        exclude = ["user"]

class   HoodForm(forms.ModelForm):
    class Meta:
        model = Neiba
        fields = ['name','location','population','image']

class BusinessForm(forms.ModelForm):
    class Meta:
        model  = Neiba
        fields = ['name','location','population']
        
