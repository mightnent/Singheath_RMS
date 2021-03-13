# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Audits(models.Model):
    class Meta():
        db_table = 'audits'
    audit_id = models.IntegerField()
    tenant = models.CharField(max_length = 100)
    auditor = models.CharField(max_length = 100)
    type = models.CharField(max_length = 100)
    status = models.IntegerField()