from authentication.decorators import allowed_user
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from audit.models import *



@login_required(login_url="/login/")
@allowed_user(allowed_roles=['auditor'])
def fnb(request):
    fnb_checklist = CheckList.objects.filter(id=1)
    fnb_section = Section.objects.filter(level_id=1)
    fnb_subsection = Subsection.objects.filter(id__in=fnb_section)
    fnb_question = Question.objects.filter(level_id__in=fnb_subsection)
    tenant = Tenant.objects.get(id=1)
    paginator = Paginator(fnb_question,1)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
  

    context = {
        'fnb_checklist':fnb_checklist, 
        'fnb_section' :fnb_section,
        'fnb_subsection':fnb_subsection,
        'fnb_question':fnb_question,
        'page_obj':page_obj,
        'tenant':tenant
    }

    

    return render(request,'audit/fnb-checklist.html',context)