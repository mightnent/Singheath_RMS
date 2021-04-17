from django.db import models
from datetime import datetime

# Create your models here.
#https://github.com/s-block/django-nested-inline

class CheckList(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title
    

class Section(models.Model):
    title = models.CharField(max_length=200)
    level = models.ForeignKey("Checklist", on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    

class Subsection(models.Model):
    title = models.CharField(max_length=200)
    level = models.ForeignKey('Section',on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

class Question(models.Model):
    qn_text = models.TextField(max_length=2000)
    level = models.ForeignKey('Subsection',on_delete=models.CASCADE)

    def __str__(self):
        return self.qn_text
    

