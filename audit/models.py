from django.db import models
from datetime import date

# Create your models here.


class ChecklistInstance(models.Model):
    checklist_id = models.IntegerField()
    checklist_type = models.CharField(max_length=500)
    section = models.CharField(max_length=500)
    subsection = models.CharField(max_length=500)
    question = models.CharField(max_length=1000)
    question_id = models.IntegerField()
    score = models.IntegerField()
    tenant = models.CharField(max_length=50)
    tenant_location = models.CharField(max_length=50)
    comment = models.CharField(max_length=2000,blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', height_field=None, width_field=None, max_length=None,blank=True)
    auditor = models.CharField(max_length=50)
    date = models.DateField(default = date.today())
    date_due = models.DateField(blank = True,null=True)
    page = models.CharField(max_length=3)

    def __str__(self):        
        return str(self.checklist_id)

class ScoreTable(models.Model):
    tenant_location = models.CharField(max_length=50)
    tenant = models.CharField(max_length=50)
    score = models.IntegerField()
    total = models.IntegerField()
    checklist_id = models.IntegerField()
    date = models.DateField(default = date.today())

    def __str__(self):        
        return str(self.checklist_id)
    
    
    
    