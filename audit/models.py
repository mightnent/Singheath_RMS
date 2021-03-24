from django.db import models
from datetime import datetime

# Create your models here.
class TenantLocation(models.Model):
    name = models.CharField(max_length=200)
    institution = models.CharField(max_length=500)
    def __str__(self):
        return self.name

class ChecklistInstance(models.Model):
    checklist_type = models.CharField(max_length=500)
    section = models.CharField(max_length=500)
    subsection = models.CharField(max_length=500)
    question = models.CharField(max_length=1000)
    question_id = models.IntegerField()
    score = models.IntegerField()
    tenant_location = models.CharField(max_length=50)
    comment = models.CharField(max_length=2000,blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', height_field=None, width_field=None, max_length=None,blank=True)

    
    