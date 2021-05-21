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
        fields = ['name','email','description','rating','sentiment','score']


class BugReport_Serializer(serializers.ModelSerializer):
    topic = serializers.StringRelatedField(read_only=True)
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = bugReport
        fields = ['user','topic','title','description','created_time','screenshot']

class UserFilterPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):

    def to_internal_value(self, data):
        return User.objects.get(email=data)

class TopicFilterPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):

    def to_internal_value(self, data):
        return bugTopics.objects.get(topicname=data)

class BugTopics_Serializer(serializers.ModelSerializer):

    class Meta:
        model = bugTopics
        fields = ['topicname']

class UserToString_Serializer(serializers.StringRelatedField):
    
    def to_internal_value(self, data):
        print("data: ",data)
        return data

class BugReportAdd_Serializer(serializers.ModelSerializer):
    topic = TopicFilterPrimaryKeyRelatedField(queryset=bugTopics.objects.all(),many=False)
    user = UserFilterPrimaryKeyRelatedField(queryset=User.objects.all(),many=False)
    class Meta:
        model = bugReport
        fields = ['user','topic','title','description','created_time','screenshot']

    def create(self, validated_data):
        return bugReport.objects.create(
            **validated_data
        )


# class BugTopics_Reports_Serializers(serializers.ModelSerializer):
#     reports = serializers.RelatedField(source=bugReport,read_only=True)
#     class Meta:
#         model = bugTopics
#         fields = ['topicname','reports']