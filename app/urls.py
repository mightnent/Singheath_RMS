# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views
import notifications

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),
    path('audit',views.audit,name='audit'),
    
    path('new-audit', views.newAuditView, name='newAudit'),

    path('create-new-audit',views.createNewAudit,name='createNewAudit'),

    path('manage-audit', views.manageAuditView, name='manageAudit'),

    path('manage-tenant',views.manageTenantView, name="manageTenant"),

    path('create-tenant',views.createTenantView, name='createTenant'),

    path('viewAudits', views.viewAudits, name='viewAudits'),

    path('request', views.request, name='request'),

    path('tenant', views.tenant, name='tenant'),

    path('viewaudit', views.viewaudit, name='viewaudit'),

    path("managenonompliance", views.managenoncompliance, name='managenoncompliance')


]
