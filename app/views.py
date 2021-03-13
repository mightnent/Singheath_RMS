# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from authentication.decorators import allowed_user
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from app.models import Audits
from authentication.forms import AuditForm

@login_required(login_url="/login/")
def index(request):
    return render(request,'index.html')

@login_required(login_url="/login/")
@allowed_user(allowed_roles=['auditor'])
def audit(request):
    audits = Audits.objects.all()
    form = AuditForm(request.POST or None)

    if request.method == "POST":

        if form.is_valid():
            checklist_type = form.cleaned_data.get("checklist_type")
            if(checklist_type == '1'):
                print("FNB")
            elif(checklist_type == '2'):
                print("NonFNB")
            elif(checklist_type == '3'):
                print("COVID")
            
 

    context = {
        'audits': audits,
        'form': form
    }
    return render(request,'audit.html', context)

