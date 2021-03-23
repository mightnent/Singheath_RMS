from django.shortcuts import render,redirect
from .models import ChecklistInstance

# Create your views here.
def audit(request):
    if request.method == 'POST':
        pass