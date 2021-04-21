from django.urls import path, re_path
from checklist import views

urlpatterns = [

    path('fnb-checklist',views.fnb,name='fnb-checklist'),
    path('covid-checklist',views.covid,name='covid-checklist'),
    path('non-fnb-checklist',views.nonfnb,name='non-fnb-checklist'),
    path('complete-checklist', views.completeAudit, name="complete-checklist")

]