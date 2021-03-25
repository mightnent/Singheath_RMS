# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from authentication.decorators import allowed_user
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from authentication.forms import AuditForm
from django.contrib.auth.models import User,Group
from .models import Tenant
from checklist.models import CheckList


@login_required(login_url="/login/")
def index(request):
    return render(request,'index.html')

@login_required(login_url="/login/")
@allowed_user(allowed_roles=['auditor'])
def audit(request):
    form = AuditForm()
    print(form)
    context = {
        'form':form,
    }
    return render(request,'audit.html',context)

@login_required(login_url="/login/")
@allowed_user(allowed_roles=['auditor'])    
def newAuditView(request):
    tenants = Tenant.objects.all()
    checklists = CheckList.objects.all()
    context = {
        'tenants':tenants,
        'checklists':checklists
    }
    
    return render(request,"newAudit.html",context)

def manageAuditView(request):
    
    return render(request,"manageAudit.html")

@login_required(login_url="/login/")
@allowed_user(allowed_roles=['auditor'])
def manageTenantView(request):
    tenants = Tenant.objects.all()
    context = {
        'tenants':tenants,       
    }
    
    return render(request,"manage-tenant.html",context)

@login_required(login_url="/login/")
@allowed_user(allowed_roles=['auditor'])
def createTenantView(request):
    if(request.method == 'POST'):
        data = request.POST
        name = data['name']
        institution = data['institution']
        business_name = data['business_name']
        lease_end_date = data['lease_end_date']
        UEN = data['uen']
        contact = data['contact']  
        email = data['email']
        try:
            User.objects.get(username=business_name)
            return redirect('/manage-tenant')
        except User.DoesNotExist:
            new_tenant = Tenant(name=name,institution=institution,business_name=business_name,lease_end_date=lease_end_date,UEN=UEN,contact=contact,email=email)
            new_tenant.save()
            new_user = User(email=email,username=business_name,password='password1.1')            
            new_user.save()
            new_user.groups.add(Group.objects.get(name='tenant'))
            return redirect('/manage-tenant')

@login_required(login_url="/login/")
@allowed_user(allowed_roles=['auditor'])
def performance(request):
    return render(request,"performanceGraph.html")

@login_required(login_url="/login/")
@allowed_user(allowed_roles=['auditor'])    
def request(request):
    return render(request,"request.html")

@login_required(login_url="/login/")
@allowed_user(allowed_roles=['tenant'])
def tenant(request):
    return render(request,'tenant.html')
