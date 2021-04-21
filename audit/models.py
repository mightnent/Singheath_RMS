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
    # pending = 0
    # rejected = -1
    # approved = 1
    appeal_status = models.IntegerField(null=True)
    rect_status = models.IntegerField(null=True)

    def __str__(self):        
        return str(self.checklist_id)

class ScoreTable(models.Model):
    tenant_location = models.CharField(max_length=50)
    tenant = models.CharField(max_length=50)
    checklist_type = models.CharField(max_length=50)
    score = models.IntegerField()
    total = models.IntegerField()
    checklist_id = models.IntegerField()
    date = models.DateField(default = date.today())
    num_visited = models.IntegerField()
    page_num = models.IntegerField()
    non_compliance = models.BooleanField(default=False)

    def __str__(self):        
        return str(self.checklist_id)

class RectificationTable(models.Model):
    date_created = models.DateField(default = date.today())
    date_due = models.DateField()
    comment = models.CharField(max_length=1000)
    tenant = models.CharField(max_length=50)
    update = models.CharField(max_length=1000)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', height_field=None, width_field=None, max_length=None,blank=True)
    row_id = models.IntegerField()
    checklist_type = models.CharField(max_length=50)
    # pending = 0
    # rejected = -1
    # approved = 1
    status = models.IntegerField()
    
    
    
    