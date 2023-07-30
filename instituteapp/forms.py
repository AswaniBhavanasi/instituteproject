from django import forms
from django.contrib.auth.models import User



class RegistrationForm(forms.Form):
    first_name=forms.CharField(
        label="Enter Your First Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'First Name'
            }
        )
    )
    last_name=forms.CharField(
        label="Enter Your Last Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Last Name'
            }
        )
    )
    username=forms.CharField(
        label="Enter Your Username",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Username'
            }
        )
    )
    password=forms.CharField(
        label="Enter Your Password",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Password'
            }
        )
    )
    email=forms.EmailField(
        label="Enter Your Email",
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Email'
            }
        )
    )
    mobile=forms.IntegerField(
        label="Enter Your Mobile Number",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Mobile Number'
            }
        )
    )
    city = forms.CharField(
        label="Enter Your City",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'CIty'
            }
        )
    )


class LoginForm(forms.Form):
    username=forms.CharField(
        label="Enter Your Username",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Username'
            }
        )
    )
    password=forms.CharField(
        label="Enter Your Password",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Password'
            }
        )
    )
