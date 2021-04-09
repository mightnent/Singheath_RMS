from django.shortcuts import render,redirect
from .models import ChecklistInstance
from django.contrib.auth.models import User,Group


# Create your views here.
def audit(request):
    
    if request.method == 'POST':
        
        data = request.POST
        photo = request.FILES.get('photo')
        checklist_type = data['checklist_type']
        section = data['section_title']
        subsection = data['subsection_title']
        question = data['question']
        question_id = data['question_id']
        tenant = data['tenant']
        checklist_id = data['checklist_id']
        page = data['page']
        date_due = data['date_due']

        if(page==''):
            page = "1"

        auditor = request.user.username
        tenant_location = request.user.groups.all()[1]

        comment = data['comment']
        if(data['submit'] == "FAIL"):
            score = 0
        elif(data['submit'] == "PASS"):
            score = 1
        else:
            score = -1
        
        int_page = int(page) + 1
        new_page = str(int_page)

        if ChecklistInstance.objects.filter(checklist_id=checklist_id,page=page).exists():
            row = ChecklistInstance.objects.get(checklist_id=checklist_id,page=page)
            row.comment = comment
            row.photo = photo
            if date_due != "":
                row.date_due = date_due
            row.save()
        else:
            if date_due != "":
                checklistInstance = ChecklistInstance(checklist_type=checklist_type,section=section,subsection=subsection,question=question,question_id=question_id,tenant_location=tenant_location,comment=comment,score=score,photo=photo,auditor=auditor,tenant=tenant,checklist_id=checklist_id,page=page,date_due=date_due)
            else:
                checklistInstance = ChecklistInstance(checklist_type=checklist_type,section=section,subsection=subsection,question=question,question_id=question_id,tenant_location=tenant_location,comment=comment,score=score,photo=photo,auditor=auditor,tenant=tenant,checklist_id=checklist_id,page=page)
            
            checklistInstance.save()
        if checklist_type=="FnB":
            return redirect('/new-audit/fnb-checklist?page='+new_page)
        elif checklist_type=="Covid":
            return redirect('/new-audit/covid-checklist?page='+new_page)
        elif checklist_type=="Non-FnB":
            return redirect('/new-audit/non-fnb-checklist?page='+new_page)
