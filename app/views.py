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
from notifications.models import *
import checklist.views as checkListViews
from django.urls import reverse
from urllib.parse import urlencode
from django.db.models import Avg, Max, Min,F
from .email_handler import EmailHandler
import datetime
import statistics


@login_required(login_url="/login/")
@allowed_user(allowed_roles=['auditor'])
def index(request):
    username = request.user.username
    today = datetime.datetime.now()
    #tenant_location must be the same as user group
    tenant_location = request.user.groups.all()[1]
    scoreTable = ScoreTable.objects.filter(tenant_location=tenant_location).filter(num_visited=F('page_num'),date__year=today.year)
    
    checklistTable = ChecklistInstance.objects.filter(checklist_id__in = [x.checklist_id for x in scoreTable]).exclude(comment__exact='').order_by('-date')[:5]

    month_list = [[]for i in range(13)]
    
    for stb in scoreTable:
        frac = stb.score / stb.total
        if stb.date.month == 1:            
            month_list[1].append(frac)
        elif stb.date.month == 2:
            month_list[2].append(frac)
        elif stb.date.month == 3:
            month_list[3].append(frac)
        elif stb.date.month == 4:
            month_list[4].append(frac)
        elif stb.date.month == 5:
            month_list[5].append(frac)
        elif stb.date.month == 6:
            month_list[6].append(frac)
        elif stb.date.month == 7:
            month_list[7].append(frac)
        elif stb.date.month == 8:
            month_list[8].append(frac)
        elif stb.date.month == 9:
            month_list[9].append(frac)
        elif stb.date.month == 10:
            month_list[10].append(frac)
        elif stb.date.month == 11:
            month_list[11].append(frac)
        elif stb.date.month == 12:
            month_list[12].append(frac)

    institution_data = []
    
    for i in month_list:
        try:
            montly_mean = round(statistics.mean(i)*100)
            institution_data.append(montly_mean)
        except:
            institution_data.append(0)
    
    #slicing because month starts from 1
    context={
        'institution_data':institution_data[1:],
        'checklistTable':checklistTable,
        'username':username
    }
        
    return render(request,'index.html',context)

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
    tenant_location = request.user.groups.all()[1]
    tenants = Tenant.objects.filter(institution=tenant_location)
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
            print(last_id)
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
    tenant_location = request.user.groups.all()[1]
    tenants = Tenant.objects.filter(institution=tenant_location)
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
        institution = request.user.groups.all()[1]
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
def performance(request):
    return render(request,"performanceGraph.html")

@login_required(login_url="/login/")
@allowed_user(allowed_roles=['auditor'])    
def attention(request):
    appealTable = AppealAlert.objects.all()
    rectificationAlert = RectificationAlert.objects.all()
    rectificationTable = RectificationTable.objects.filter(row_id__in = [x.row_id for x in rectificationAlert])
    context = {
        'appealTable' : appealTable,
        'rectificationTable' : rectificationTable
    }
    return render(request,"attention.html",context)

@login_required(login_url="/login/")
@allowed_user(allowed_roles=['tenant'])
def tenant(request):
    username = request.user.username
   
    this_tenant = Tenant.objects.get(business_name=username)
    scoreTable = ScoreTable.objects.filter(tenant=username).filter(num_visited=F('page_num'))
    scoreTableCompliance = scoreTable.filter(non_compliance=True)  

    checklistTable = ChecklistInstance.objects.filter(checklist_id__in = [x.checklist_id for x in scoreTableCompliance]).filter(date_due__isnull=False)
  
    context = {
        'lease_end_date' : this_tenant.lease_end_date,
        'checklistTable' : checklistTable,
        'scoreTable' : scoreTable,
        'username': username
    }
    return render(request,'tenant/tenant.html',context)

@login_required(login_url="/login/")
@allowed_user(allowed_roles=['tenant'])
def appeal(request):
    if(request.method=='POST'):
        this_id = request.POST['qn']
    print(this_id)

    row = ChecklistInstance.objects.get(id=this_id)
    context={
        'row':row,
    }

    return render(request,'tenant/appeal.html',context)

@login_required(login_url="/login/")
@allowed_user(allowed_roles=['tenant'])
def rectification(request):
    if(request.method=='POST'):
        this_id = request.POST['qn']
    row = ChecklistInstance.objects.get(id=this_id)
    context={
        'row':row,
    }

    return render(request,'tenant/rectification.html',context)

@login_required(login_url="/login/")
@allowed_user(allowed_roles=['tenant'])
def viewaudit(request):
    return render(request,'viewaudit.html')

@login_required(login_url="/login/")
@allowed_user(allowed_roles=['auditor'])
def tenantInfo(request):
    
    if(request.method=='POST'):
        tenant = request.POST['tenant']
    #filter out all the records that's completed for the tenant
    scoreTable = ScoreTable.objects.filter(tenant=tenant).filter(num_visited=F('page_num'))

    context = {
        'scoreTable':scoreTable,
    }
    return render(request,'tenant-info.html',context)

@login_required(login_url="/login/")
@allowed_user(allowed_roles=['tenant'])
def managenoncompliance(request):
    return render(request,'managenoncompliance.html')
