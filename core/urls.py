# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = "SingHealth RMS Admin";
admin.site.site_title = "SingHealth RMS Admin";

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("authentication.urls")), # Auth routes - login / register
    path("", include("app.urls")),             # UI Kits Html files
    path("new-audit/",include("checklist.urls")),
    path("audit/",include("audit.urls")),
    path("notifications/",include("notifications.urls"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
