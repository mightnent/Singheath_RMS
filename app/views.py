# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect


@login_required(login_url="/login/")
def index(request):
    return render(request,'index.html')

def audit(request):
    return render(request,'audit.html')
