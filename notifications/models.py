from django.db import models
from datetime import date
# Create your models here.
class Notification(models.Model):
    date_created = models.DateField(default=date.today())
    content = models.CharField(max_length = 250)

class AppealAlert(models.Model):
    date_created = models.DateField(default = date.today())
    original_date = models.DateField()
    new_date = models.DateField()
    comment = models.CharField(max_length=1000)
    tenant = models.CharField(max_length=50)
    reason = models.CharField(max_length=1000)
    row_id = models.IntegerField()
    checklist_type = models.CharField(max_length=50)

class RectificationAlert(models.Model):
    date_created = models.DateField(default = date.today())
    row_id = models.IntegerField()
  
