from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import EmailInput, TextInput, PasswordInput



class Userform(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name","last_name","email","password","username"]
        widgets = {
            "email": forms.EmailInput(attrs={"placeholder":"Enter your Email", "class":"form-control"}),
            "first_name": forms.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}),
            "last_name": forms.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}),
            "username": forms.TextInput(attrs={"placeholder":"Username", "class":"form-control"}),
            "password": forms.TextInput(attrs={"placeholder":"Password", "class":"form-control"}),
        }