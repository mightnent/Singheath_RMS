# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from . import views

urlpatterns = [

    path('notifications', views.notifications, name='notifications'),

    path("broadcast", views.broadcast, name='broadcast'),

    path('appeal-alert',views.appealAlert,name="appeal-alert"),

    path('appeal-reply',views.appealReply,name='appeal-reply')
]