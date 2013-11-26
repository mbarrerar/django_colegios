from django import forms
from django.contrib.auth import authenticate, get_user_model

class loginForm(forms.Form):
    username = forms.CharField(max_length=12, required=True)
    password = forms.CharField(max_length=12, required=True)
    