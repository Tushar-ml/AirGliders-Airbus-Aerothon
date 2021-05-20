from django.core import validators
from django.db import models
from django.core.validators import MaxLengthValidator, validate_email
# Create your models here.
from django.contrib.auth.models import User

class Feedback(models.Model):
    name = models.TextField(null=False,default='default')
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