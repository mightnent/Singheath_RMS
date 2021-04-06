# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tenant(models.Model):
    name = models.CharField(max_length=200)
    institution = models.CharField(max_length=500)
    business_name = models.CharField(max_length=500)
    lease_end_date = models.DateField(blank=True)
    UEN = models.CharField(max_length=50,blank=True)
    contact = models.CharField(max_length=50)    
    email = models.EmailField(max_length=254)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.business_name