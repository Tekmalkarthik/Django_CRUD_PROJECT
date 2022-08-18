from socket import fromshare
from  django.core import validators
from .models import user
from django import forms

class EmployeeRegistration(forms.ModelForm):
    class Meta:
        model=user
        fields=["name","email","mobile","password"]
        widgets={
            "name":  forms.TextInput(attrs={'class':"form-control"}),
            "email":  forms.EmailInput(attrs={'class':"form-control"}),
            "mobile":  forms.TextInput(attrs={'class':"form-control"}),
            "password":  forms.PasswordInput(render_value=True , attrs={'class':"form-control"})
        }
