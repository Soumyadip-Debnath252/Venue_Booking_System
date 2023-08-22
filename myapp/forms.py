from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Book, CustomUser
from datetime import date, timedelta

class DateInput(forms.DateInput):
    input_type = 'date'

class MyUserRegFrm(UserCreationForm):
    username=forms.CharField(label='Enter username*', widget=forms.TextInput(
        attrs={
            'class': 'form-control border-primary',
            'placeholder': 'Enter username'
        }))
    first_name = forms.CharField(label='Enter your first name*', widget=forms.TextInput(
        attrs={
            'class': 'form-control border-primary',
            'placeholder': 'Enter your first name'
        }))
    last_name = forms.CharField(label='Enter your last name*', widget=forms.TextInput(
        attrs={
            'class': 'form-control border-primary',
            'placeholder': 'Enter your last name'
        }))
    mobile=forms.CharField(label='Enter your Contact Number*', widget=forms.NumberInput(
        attrs={
            'class': 'form-control border-primary',
            'placeholder': 'Enter your Contact Number'
        }))
    email = forms.CharField(label='Enter your email-ID*', widget=forms.EmailInput(
        attrs={
            'class': 'form-control border-primary',
            'placeholder': 'Enter your email-ID'
        }))
    password1 = forms.CharField(label='Enter your password*', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control border-primary',
            'placeholder': 'Enter your password'
        }))
    password2 = forms.CharField(label='Enter confirm password*', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control border-primary',
            'placeholder': 'Enter confirm password'
        }))
    address=forms.CharField(label='Enter your address*', widget=forms.TextInput(
        attrs={
            'class': 'form-control border-primary',
            'placeholder': 'Enter your address'
        }))
    class Meta:
        model=CustomUser
        fields=['username','first_name','last_name','mobile','email', 'password1','password2','address']

class MyLoginFrm(AuthenticationForm):
    username = forms.CharField(label='Enter username*', widget=forms.TextInput(
        attrs={
            'class': 'form-control border-primary',
            'placeholder': 'Enter username'
        }))
    password = forms.CharField(label='Enter password*', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control border-primary',
            'placeholder': 'Enter password'
        }))

class BookingForm(forms.ModelForm):
    description=forms.CharField(label='Enter Event Description*', widget=forms.Textarea(
        attrs={
            'class': 'form-control border-primary',
            'placeholder': 'Enter Event Description'
        }))
    eventdate=forms.DateField(label="Select Your event date*",
            widget=DateInput(attrs={
            'class': 'form-control border-primary'
        }))
    def clean_eventdate(self):
        sd = self.cleaned_data['eventdate']
        td=date.today()
        fd=date.today() + timedelta(days=120)
        # age = (date.today() - sd)
        if sd==td:
            raise forms.ValidationError('Selected date may not be today')
        elif sd < td:
            raise forms.ValidationError('Selected date may not be previous day')
        elif sd > fd:
            raise forms.ValidationError('Selected date must be within 20 days from current date')
        return sd
    class Meta:
        widgets={'eventdate':DateInput()}
        model=Book
        fields=['bid', 'description', 'eventdate']