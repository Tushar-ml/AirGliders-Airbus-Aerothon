from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Announcement

class Announcement_serializer(serializers.ModelSerializer):

    class Meta:
        model = Announcement
        fields = ['title','description']