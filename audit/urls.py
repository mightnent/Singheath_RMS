from django.urls import path
from . import views

urlpatterns = [
    path('audit',views.audit, name='audit'),
    path('create',views.create,name='create')
]
