from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Feedback, bugReport, bugTopics

class Feedback_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Feedback
        fields = ['email','description','rating']


class BugReport_Serializer(serializers.ModelSerializer):

    class Meta:
        model = bugReport
        fields = ['user','topic','title','description','created_time','screenshot']


class BugTopics_Serializer(serializers.ModelSerializer):

    class Meta:
        model = bugTopics
        fields = ['topicname']