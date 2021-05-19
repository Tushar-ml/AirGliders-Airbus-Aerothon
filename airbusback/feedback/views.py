from .serializers import Feedback_Serializer
from django.contrib.auth.models import AnonymousUser, User
from django.shortcuts import render
from rest_framework import serializers
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser 
# Create your views here.
from .models import Feedback

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET','POST'])
def add_feedback(request):

    if request.method == 'GET':
        feedbacks = Feedback.objects.all()

        serializer = Feedback_Serializer(feedbacks,many=True)
        return JsonResponse(serializer.data,safe=False)

    if request.method=='POST':
        
        # username = request.POST.get('username')
        data = JSONParser().parse(request)
        serializer = Feedback_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,safe=False)
        return JsonResponse(serializer.errors, status=400)