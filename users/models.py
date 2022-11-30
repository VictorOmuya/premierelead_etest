from django.db import models
from django.contrib.auth.models import User
from django.db import models 


class Profile(models.Model):
    
    def __str__(self):
        return self.user.username
    
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    auth_token = models.CharField(max_length=100, default="")
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=4, default="")
    phone = models.CharField(max_length=10, default="")
    score = models.IntegerField(default=0)
    exam_taken = models.BooleanField(default=False)
    

    

    