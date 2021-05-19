from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class Feedback(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=250,null=False)
    description = models.TextField(null=False)
    created_time = models.DateTimeField(null=False,auto_now_add=True)
    screenshot = models.ImageField(upload_to='feedback/',null=True)