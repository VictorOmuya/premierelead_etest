from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.db import models 


class Profile(models.Model):
    
    def __str__(self):
        return self.user.username
    
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    code = models.CharField(max_length=3, default="+234")
    phone = models.CharField(max_length=10, default="9999999999")
    score = models.IntegerField()
    
class Questions(models.Model):
    
    question = models.CharField(max_length=200, default= "Enter question")
    optionA = models.CharField(max_length=200, default= "Option A")
    optionB = models.CharField(max_length=200, default= "Option B")
    optionC = models.CharField(max_length=200, default= "Option C")
    optionD = models.CharField(max_length=200, default= "Option D")
    Answer = models.CharField(max_length=200, default= "Answer")