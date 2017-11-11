from django.db import models

# Create your models here.
class FormHeader(models.Model):
    title = models.CharField(max_length=100)
    form_description = models.TextField()

class Questions(models.Model):
    ques=models.TextField()

class Answers(models.Model):
    fieldType=models.TextField()
    ans=models.TextField()

class QuesAns(models.Model):
    ques1 = models.TextField()
    fieldType1 = models.TextField()
    ans1 = models.TextField()