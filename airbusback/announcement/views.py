from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
# Create your views here.
from .serializers import Announcement_serializer
from .models import Announcement

@api_view(['GET'])
def get_announcements(request):

    if request.method == 'GET':
        announcements = Announcement.objects.all()

        serializer = Announcement_serializer(announcements,many=True)
        return JsonResponse(serializer.data,safe=False)

@api_view(['POST'])
def add_announcement(request):

    if request.method=='POST':

        data = JSONParser().parse(request)

        serializer = Announcement_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,safe=False)
        return JsonResponse(serializer.errors,status=400)