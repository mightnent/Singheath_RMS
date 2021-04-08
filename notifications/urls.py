# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from . import views

urlpatterns = [

    path('notifications', views.notifications, name='notifications'),

    path("broadcast", views.broadcast, name="broadcast")
]