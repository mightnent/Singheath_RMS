# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),
    path('audit',views.audit,name='audit'),

    path('newAudit', views.newAuditView, name='newAudit'),

    path('manageAudit', views.manageAuditView, name='manageAudit'),

    path('manageTenant',views.manageTenantView, name="manageTenant"),

    path('performance', views.performance, name='performance'),

    path('request', views.request, name='request'),




    path('tenant', views.tenant, name='tenant'),
]
