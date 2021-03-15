from authentication.decorators import allowed_user
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

@login_required(login_url="/login/")
@allowed_user(allowed_roles=['auditor'])
def index(request):
    return render(request,'audit/audit.html')

@login_required(login_url="/login/")
@allowed_user(allowed_roles=['auditor'])
def fnb(request):
    return render(request,'audit/fnb-checklist.html')