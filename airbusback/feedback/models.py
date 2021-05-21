from django.core import validators
from django.db import models
from django.core.validators import MaxLengthValidator, validate_email
# Create your models here.
from django.contrib.auth.models import User

def get_email(self):
    return self.email

User.add_to_class('__str__',get_email)

class bugTopics(models.Model):
    topicname = models.CharField(max_length=100,unique=True,validators=[MaxLengthValidator(100)])

    def __str__(self):
        return self.topicname


class bugReport(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    topic = models.ForeignKey(bugTopics,on_delete=models.DO_NOTHING,related_name='topic')
    title = models.CharField(max_length=250,null=False)
    description = models.TextField(null=False)
    created_time = models.DateTimeField(null=False,auto_now_add=True)
    screenshot = models.ImageField(upload_to='feedback/',null=True)

    def __str__(self):
        return self.topic.topicname + ": " + self.title + " - " + self.description[:20]

class Feedback(models.Model):
    name = models.CharField(null=False,default='default',max_length=30)
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
    sentiment = models.CharField(null=False,max_length=20,default='Neutral')
    score = models.FloatField(null=False,default=0)

    def __str__(self):
        return str(self.rating) + ": " + self.description[:20]