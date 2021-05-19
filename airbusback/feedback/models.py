from django.core import validators
from django.db import models
from django.core.validators import MaxLengthValidator, validate_email
# Create your models here.
from django.contrib.auth.models import User


class bugTopics(models.Model):
    topicname = models.CharField(max_length=100,unique=True,validators=[MaxLengthValidator(100)])

    def __str__(self):
        return self.topicname


class bugReport(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    topic = models.ForeignKey(bugTopics,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=250,null=False)
    description = models.TextField(null=False)
    created_time = models.DateTimeField(null=False,auto_now_add=True)
    screenshot = models.ImageField(upload_to='feedback/',null=True)

    def __str__(self):
        return self.topic.topicname + ": " + self.title + " - " + self.description[:20]

class Feedback(models.Model):
    email = models.EmailField(null=False,validators=[validate_email],default='default@gmail.com')
    description = models.TextField(null=False)
    created_time = models.DateTimeField(null=False,auto_now_add=True)
    RATING_CHOICES = [
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5)
    ]

    rating = models.IntegerField(choices=RATING_CHOICES,null=True)

    def __str__(self):
        return str(self.rating) + ": " + self.description[:20]