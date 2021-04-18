# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from authentication.decorators import allowed_user
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from authentication.forms import AuditForm
from django.contrib.auth.models import User,Group
from .models import Tenant
from checklist.models import *
from audit.models import *
import checklist.views as checkListViews
from django.urls import reverse
from urllib.parse import urlencode
from django.db.models import Avg, Max, Min
from .email_handler import EmailHandler


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

@login_required(login_url="/login/")
@allowed_user(allowed_roles=['auditor']) 
def createNewAudit(request):
    if(request.method=='POST'):
        
        try:
            last_id = ChecklistInstance.objects.all().aggregate(Max('checklist_id'))
            new_id = last_id.get('checklist_id__max') + 1
        except :
            new_id = 1
        data = request.POST
        tenant = data['tenant']
        if data['checklist'] == 'FnB':
            base_url = reverse('fnb-checklist')
            query_string =  urlencode({'tenant': tenant,'id':new_id})
            url = "{}?{}".format(base_url,query_string)
            return redirect(url)
        elif data['checklist'] == 'Covid':
            base_url = reverse('covid-checklist')
            query_string =  urlencode({'tenant': tenant,'id':new_id})
            url = "{}?{}".format(base_url,query_string)
            return redirect(url)
        elif data['checklist'] == 'Non-FnB':
            base_url = reverse('non-fnb-checklist')
            query_string =  urlencode({'tenant': tenant,'id':new_id})
            url = "{}?{}".format(base_url,query_string)
            return redirect(url)

def manageAuditView(request):
    
    return render(request,"manageAudit.html")

@login_required(login_url="/login/")
@allowed_user(allowed_roles=['auditor'])
def manageTenantView(request):
    tenants = Tenant.objects.all()
    context = {
        'tenants':tenants,       
    }
    
    return render(request,'manageTenants/manage-tenant.html',context)

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
            gen_password = User.objects.make_random_password()
            new_user = User(email=email,username=business_name)
            new_user.set_password(gen_password)           
            new_user.save()
            new_user.groups.add(Group.objects.get(name='tenant'))
            EmailHandler.send_new_tenant_email(email=email, login_link=request.build_absolute_uri("/login"), gen_password=gen_password, owner_name=name, username=business_name)
            return redirect('/manage-tenant')

@login_required(login_url="/login/")
@allowed_user(allowed_roles=['auditor'])
def viewAudits(request):
    tenants = Tenant.objects.all()
    checklists = CheckList.objects.all()
    checklistInstance = ChecklistInstance.objects.all()
    scoreTable = ScoreTable
    context = {
        'tenants':tenants,
        'checklists' :checklists,
        'checklistInstances' :checklistInstance,
        'scoreTable' :scoreTable
    }
    return render(request,'manageTenants/viewAudits.html',context)

@login_required(login_url="/login/")
@allowed_user(allowed_roles=['auditor'])    
def request(request):
    return render(request,"request.html")






# Allowed roles: tenant

@login_required(login_url="/login/")
@allowed_user(allowed_roles=['tenant'])
def tenant(request):
    username = request.user.username
    this_tenant = Tenant.objects.get(business_name=username)
    context = {
        'lease_end_date' : this_tenant.lease_end_date,
    }
    return render(request,'tenant.html',context)

@login_required(login_url="/login/")
@allowed_user(allowed_roles=['tenant'])
def viewaudit(request):
    return render(request,'viewaudit.html')

@login_required(login_url="/login/")
@allowed_user(allowed_roles=['tenant'])
def managenoncompliance(request):
    return render(request,'managenoncompliance.html')
