from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import FieldBooking

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2'] 
    

class CustomLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)



class FieldBookingForm(forms.ModelForm):
    class Meta:
        model = FieldBooking
        fields = ['field_name', 'booking_date', 'booking_time']
