from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Feedback

class Feedback_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Feedback
        fields = ['email','description','rating']

