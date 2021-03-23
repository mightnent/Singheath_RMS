# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from authentication.decorators import allowed_user
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

@login_required(login_url="/login/")
def index(request):
    return render(request,'index.html')

@login_required(login_url="/login/")
@allowed_user(allowed_roles=['auditor'])
def audit(request):
    return render(request,'audit.html')

def manageTenantView(request):
    return render(request,"manage-tenant.html")

def newAuditView(request):
    return render(request,"newAudit.html")

def manageAuditView(request):
    return render(request,"manageAudit.html")

def performance(request):
    return render(request,"performanceGraph.html")

def testSel(request):
    return render(request,"testSel.html")