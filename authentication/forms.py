from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",                
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control",
                "id": "pw"
            }
        ))
        
class AuditForm(forms.Form):
    CHOICES = [(1, 'F&B'), (2, 'Non F&B'), (3, 'COVID-19')]
    checklist_type = forms.ChoiceField(choices = CHOICES, widget = forms.RadioSelect(attrs={'class': 'form-check-inline'}))
# class SignUpForm(UserCreationForm):
#     username = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 "placeholder" : "Username",                
#                 "class": "form-control"
#             }
#         ))
#     email = forms.EmailField(
#         widget=forms.EmailInput(
#             attrs={
#                 "placeholder" : "Email",                
#                 "class": "form-control"
#             }
#         ))
#     password1 = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "placeholder" : "Password",                
#                 "class": "form-control"
#             }
#         ))
#     password2 = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "placeholder" : "Password check",                
#                 "class": "form-control"
#             }
#         ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
