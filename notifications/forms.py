from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NotificationForm(forms.Form):
    content = forms.CharField( max_length = 250)