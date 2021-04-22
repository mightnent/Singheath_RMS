from django.shortcuts import render
from authentication.decorators import allowed_user
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from authentication.forms import AuditForm
from django.contrib.auth.models import User,Group
from checklist.models import *
from audit.models import *
import checklist.views as checkListViews
from django.urls import reverse
from urllib.parse import urlencode
from django.db.models import Avg, Max, Min
from .forms import NotificationForm
from .models import *
from datetime import datetime

# Create your views here.
@login_required(login_url="/login/")
@allowed_user(allowed_roles=['tenant'])
def notifications(request):
    tenant = request.user.username
    notifications = Notification.objects.filter(tenant__in=[tenant,"0"]).order_by('-id')
    for n in notifications:
        print(n.content)
    return render(request,'notifications.html', {'notifications': notifications})

@login_required(login_url="/login/")
@allowed_user(allowed_roles=['auditor'])    
def broadcast(request):

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NotificationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            content = form.cleaned_data['content']
            date = datetime.date(datetime.now())
            new_notif = Notification(date_created = date, content = content)
            new_notif.save()
            form = NotificationForm()
            return render(request,"broadcast.html", {'form': form})
    else:
        form = NotificationForm()

    return render(request,"broadcast.html", {'form': form})


def appealAlert(request):
    if(request.method=='POST'):
        data = request.POST
        row_id = data['row_id']
        new_date = data['new_date']
        reason = data['reason']
        original_date = data['date_due']
        original_date = datetime.strptime(original_date,'%B %d, %Y').date()
        comment = data['comment']
        checklist_type = data['checklist_type']
        tenant = request.user.username
        appealAlert = AppealAlert(new_date=new_date,reason=reason,original_date=original_date,comment=comment,tenant=tenant,row_id=row_id,checklist_type=checklist_type)
        appealAlert.save()
        checklistInstance = ChecklistInstance.objects.get(id=row_id)
        checklistInstance.appeal_status = 0
        checklistInstance.save()
    return redirect('tenant')

def appealReply(request):
    if request.method=="POST":
        data = request.POST
        row_id = data['row_id']
        #appeal_id = data['appeal_id']
        new_date = data['new_date']
        new_date = datetime.strptime(new_date,'%B %d, %Y').date()
        checklistInstance = ChecklistInstance.objects.get(id=row_id)
        tenant = AppealAlert.objects.get(row_id=row_id)
        AppealAlert.objects.filter(row_id=row_id).delete()
        if data['submit'] == "appeal-approve":
            content = "Your appeal for issue: " + data['comment']+" has been approved."
            new_notif = Notification(content = content,tenant=tenant.tenant)
            new_notif.save()
            checklistInstance.appeal_status = 1
            checklistInstance.date_due = new_date
            checklistInstance.save()
        elif data['submit'] == "appeal-reject":
            content = "Your appeal for issue: " + data['comment']+" has been rejected. Please rectify ASAP"
            new_notif = Notification(content = content,tenant=tenant.tenant)
            new_notif.save()
            checklistInstance.appeal_status = -1
            checklistInstance.save()
    return redirect('attention')

def rectificationAlert(request):
    if request.method == 'POST':
        data = request.POST
        photo = request.FILES.get('photo')
        row_id = data['row_id']
        update = data['update']
        date_due = data['date_due']
        date_due = datetime.strptime(date_due,'%B %d, %Y').date()
        comment = data['comment']
        checklist_type = data['checklist_type']
        tenant = request.user.username
        rectificationAlert = RectificationAlert(row_id=row_id)
        rectificationAlert.save()
        rectificationTable= RectificationTable(photo=photo,row_id=row_id,update=update,date_due=date_due,comment=comment,checklist_type=checklist_type,tenant=tenant,status=0)
        rectificationTable.save()
        checklistInstance = ChecklistInstance.objects.get(id=row_id)
        checklistInstance.rect_status=0
        checklistInstance.save()
    return redirect('tenant')

def rectificationReply(request):
    if request.method=="POST":
        data = request.POST
        row_id = data['row_id']
        rectificationAlert = RectificationAlert.objects.get(row_id=row_id)
        checklistInstance = ChecklistInstance.objects.get(id=row_id)
        rectificationTable = RectificationTable.objects.get(row_id=rectificationAlert.row_id)
        RectificationAlert.objects.filter(row_id=row_id).delete()
        if data['submit'] == "rectification-approve":
            content = "Your rectification for issue: " + data['comment']+" has been approved."
            new_notif = Notification(content = content,tenant=checklistInstance.tenant)
            new_notif.save()
            rectificationTable.status = 1
            checklistInstance.rect_status = 1
            rectificationTable.save()
            checklistInstance.save()
        elif data['submit'] == "rectification-reject":
            content = "Your rectification for issue: " + data['comment']+" has been rejected. Please rectify ASAP"
            new_notif = Notification(content = content,tenant=checklistInstance.tenant)
            new_notif.save()
            rectificationTable.status = -1
            checklistInstance.rect_status = -1
            rectificationTable.save()
            checklistInstance.save()
    return redirect('attention')