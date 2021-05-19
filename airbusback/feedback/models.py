from django.db import models
from django.core.validators import validate_email
# Create your models here.
from django.contrib.auth.models import User
class bugReport(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=250,null=False)
    description = models.TextField(null=False)
    created_time = models.DateTimeField(null=False,auto_now_add=True)
    screenshot = models.ImageField(upload_to='feedback/',null=True)


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
        return str(self.rating) + " " + self.description[:20]