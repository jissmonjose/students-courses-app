from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import TimeTable
from django.conf import settings


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class TimeTableForm(ModelForm):
    class Meta:
        model = TimeTable
        fields = '__all__'
