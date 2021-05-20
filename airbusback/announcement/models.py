from django.db import models

# Create your models here.

class Announcement(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    created_time = models.TimeField(auto_now_add=True)
    last_update_time = models.TimeField(auto_now=True)
