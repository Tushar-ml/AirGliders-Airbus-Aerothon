from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Feedback, bugReport, bugTopics
from rest_framework.fields import EmailField
from rest_framework.utils import field_mapping


from django.contrib.auth.models import User

class User_Serializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email']

class Feedback_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Feedback
        fields = ['email','description','rating']


class BugReport_Serializer(serializers.ModelSerializer):
    topic = serializers.CharField(source='bugTopics.topicname',read_only=True)
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = bugReport
        fields = ['user','topic','title','description','created_time','screenshot']


class BugReportAdd_Serializer(serializers.ModelSerializer):
    topic = serializers.PrimaryKeyRelatedField(queryset=bugTopics.objects.all(),many=False)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),many=False)
    class Meta:
        model = bugReport
        fields = ['user','topic','title','description','created_time','screenshot']

class BugTopics_Serializer(serializers.ModelSerializer):

    class Meta:
        model = bugTopics
        fields = ['topicname']

# class BugTopics_Reports_Serializers(serializers.ModelSerializer):
#     reports = serializers.RelatedField(source=bugReport,read_only=True)
#     class Meta:
#         model = bugTopics
#         fields = ['topicname','reports']