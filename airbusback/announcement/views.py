from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
# Create your views here.
from .serializers import Announcement_serializer
from .models import Announcement
import requests

@api_view(['GET'])
def get_announcements(request):
    '''
    Returns all the announcements in a list of JSON Objects

    :return: JSON Object {
        "title" : string,
        "description" : string,
        "created_time" : time,
        "last_update_time" : time
    }
    '''


    if request.method == 'GET':
        announcements = Announcement.objects.all()

        serializer = Announcement_serializer(announcements,many=True)
        return JsonResponse(serializer.data,safe=False)

@api_view(['POST'])
def add_announcement(request):
    '''
    Adds a Announcement Record

    :params: Request Object {
        "title" : string,
        "description" : string
    }
    '''


    if request.method=='POST':

        data = JSONParser().parse(request)

        serializer = Announcement_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,safe=False)
        return JsonResponse(serializer.errors,status=400)

def announcement(request):

    announcements = requests.get('http://127.0.0.1:8000/announcement/get')
    announceresponse = announcements.json()
    context = {
        'announcements' : announceresponse
    }
    print(context)
    return render(request,'announcement.html',context=context)