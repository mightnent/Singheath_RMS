from django.urls import path, re_path
from checklist import views

urlpatterns = [

    path('fnb-checklist',views.fnb,name='fnb-checklist'),

]