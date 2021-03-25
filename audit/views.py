from django.shortcuts import render,redirect
from .models import ChecklistInstance


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
        tenant_location = data['tenant_location']
        comment = data['comment']
        if(data['submit'] == "FAIL"):
            score = 0
        elif(data['submit'] == "PASS"):
            score = 1
        else:
            score = -1
        page = request.GET['page']
        print(page)
        checklistInstance = ChecklistInstance(checklist_type=checklist_type,section=section,subsection=subsection,question=question,question_id=question_id,tenant_location=tenant_location,comment=comment,score=score,photo=photo)
        
        checklistInstance.save()
        return redirect('/audit/fnb-checklist?page=2')

def create(request):
    pass