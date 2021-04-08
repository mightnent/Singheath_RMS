from django.db import models

# Create your models here.
class Notification(models.Model):
    date_created = models.DateField(blank = True)
    content = models.CharField(max_length = 250)