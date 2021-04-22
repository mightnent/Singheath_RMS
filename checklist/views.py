from app.models import Tenant
from authentication.decorators import allowed_user
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from audit.models import *
from django.contrib import messages
from django.urls import reverse
from app.email_handler import EmailHandler


tenant = ""
checklist_id = None

@login_required(login_url="/login/")
@allowed_user(allowed_roles=['auditor'])
def fnb(request):
    global tenant
    global checklist_id

    if request.GET.get('tenant') != None:
        tenant = request.GET.get('tenant')
    if request.GET.get('id') != None:
        checklist_id = request.GET.get('id')
    

    #empty checklist templates
    checklist = CheckList.objects.filter(id=1)
    section = Section.objects.filter(level_id=1)
    subsection = Subsection.objects.filter(id__in=section)
    question = Question.objects.filter(level_id__in=subsection).order_by("id")
    paginator = Paginator(question,1)
    page_number = request.GET.get('page')
    if page_number == None:
        page_number = 1
 
    current_checklist = ChecklistInstance.objects.filter(checklist_id=checklist_id).filter(page=page_number)
    page_obj = paginator.get_page(page_number)

    context = {
        'checklist':checklist, 
        'section' :section,
        'subsection':subsection,
        'question':question,
        'page_obj':page_obj,
        'tenant':tenant,
        'checklist_id':checklist_id,
        'current_checklist':current_checklist
    }   

    return render(request,'audit/fnb-checklist.html',context)

@login_required(login_url="/login/")
@allowed_user(allowed_roles=['auditor'])
def covid(request):
    global tenant
    global checklist_id

    if request.GET.get('tenant') != None:
        tenant = request.GET.get('tenant')
    if request.GET.get('id') != None:
        checklist_id = request.GET.get('id')
    

    #empty checklist templates
    checklist = CheckList.objects.filter(id=3)
    section = Section.objects.filter(level_id=3)
    subsection = Subsection.objects.filter(level_id__in=section)
    question = Question.objects.filter(level_id__in=subsection).order_by("id")
    paginator = Paginator(question,1)
    page_number = request.GET.get('page')
    if page_number == None:
        page_number = 1
 
    current_checklist = ChecklistInstance.objects.filter(checklist_id=checklist_id).filter(page=page_number)
    page_obj = paginator.get_page(page_number)

    context = {
        'checklist':checklist, 
        'section' :section,
        'subsection':subsection,
        'question':question,
        'page_obj':page_obj,
        'tenant':tenant,
        'checklist_id':checklist_id,
        'current_checklist':current_checklist
    }   

    return render(request,'audit/covid-checklist.html',context)

@login_required(login_url="/login/")
@allowed_user(allowed_roles=['auditor'])
def nonfnb(request):
    global tenant
    global checklist_id

    if request.GET.get('tenant') != None:
        tenant = request.GET.get('tenant')
    if request.GET.get('id') != None:
        checklist_id = request.GET.get('id')
    

    #empty checklist templates
    checklist = CheckList.objects.filter(id=2)
    section = Section.objects.filter(level_id=2)
    subsection = Subsection.objects.filter(level_id__in=section)
    question = Question.objects.filter(level_id__in=subsection).order_by("id")

    print(subsection)
    paginator = Paginator(question,1)
    print(paginator)
    page_number = request.GET.get('page')
    if page_number == None:
        page_number = 1
 
    current_checklist = ChecklistInstance.objects.filter(checklist_id=checklist_id).filter(page=page_number)
    page_obj = paginator.get_page(page_number)

    context = {
        'checklist':checklist, 
        'section' :section,
        'subsection':subsection,
        'question':question,
        'page_obj':page_obj,
        'tenant':tenant,
        'checklist_id':checklist_id,
        'current_checklist':current_checklist
    }   

    return render(request,'audit/non-fnb-checklist.html',context)

@login_required(login_url="/login/")
@allowed_user(allowed_roles=['auditor'])
def completeAudit(request):
    global tenant
    global checklist_id

    if request.GET.get('tenant') != None:
        tenant = request.GET.get('tenant')
    if request.GET.get('id') != None:
        checklist_id = request.GET.get('id')

    tenant_email = Tenant.objects.get(business_name = tenant, institution = request.user.groups.all()[1]).email
    EmailHandler.notify_audit_performed(tenant_email, request.build_absolute_uri("/viewaudit"), tenant, checklist_id)
    messages.info(request, "Audit successfully completed")
    return redirect(reverse("newAudit"))
