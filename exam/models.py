from django.db import models

# Create your models here.
class Questions(models.Model):
    
    question = models.CharField(max_length=200, default= "Enter question")
    optionA = models.CharField(max_length=200, default= "Option A")
    optionB = models.CharField(max_length=200, default= "Option B")
    optionC = models.CharField(max_length=200, default= "Option C")
    optionD = models.CharField(max_length=200, default= "Option D")
    Answer = models.CharField(max_length=200, default= "Answer")