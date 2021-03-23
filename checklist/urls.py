from django.urls import path, re_path
from checklist import views

urlpatterns = [

    # The home page
    path('', views.index, name='audit'),

    path('fnb-checklist',views.fnb,name='fnb-checklist'),

]