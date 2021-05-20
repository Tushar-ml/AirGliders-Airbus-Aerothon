from .serializers import BugReport_Serializer, BugTopics_Serializer, Feedback_Serializer
from django.contrib.auth.models import AnonymousUser, User
from django.shortcuts import render
from rest_framework import serializers
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser 
# Create your views here.
from .models import Feedback, bugReport,bugTopics
from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET','POST'])
def add_feedback(request):

    '''if request.method == 'GET':
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
        return JsonResponse(serializer.errors, status=400)'''
    if request.method=='POST':
        first_name = request.POST.get("fname")
        email = request.POST.get("email")
        feedback = request.POST.get("feedback")
        rating = request.POST.get("rating")
        result = f'Name: {first_name} \n email: {email} \n Feedback: {feedback} \n Rating: {rating}'
        print(result)
        print()
        print(sentimentAnalyzer(feedback))
        
    return render(request,'feedback.html')

def sentimentAnalyzer(feedback):
    score = 0
    sentiment = 'Neutral'
    if feedback != None:
        sent = sia.polarity_scores(feedback)
        sent.pop('compound')
        sent = list(sent.items())
        sent.sort(key=lambda x:x[1],reverse=True)
        score = sent[0][1]
        sentiment = sent[0][1]
    if sentiment == 'pos':
        sentiment = 'Positive'
    elif sentiment == 'neg':
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    return sentiment,score

@api_view(['GET'])
def get_bugReport(request):

    if request.method == 'GET':
        bugReports = bugReport.objects.all()

        serializer = BugReport_Serializer(bugReports,many=True)
        return JsonResponse(serializer.data,safe=False)

@api_view(['POST'])
def add_bugReport(request):

    if request.method == 'POST':
        # print(request.data)
        data = JSONParser().parse(request)
        serializer = BugReport_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,safe=False)
        
        return JsonResponse(serializer.errors,status=400)

@api_view(['GET'])
def get_topics(request):

    if request.method == 'GET':
        topics = bugTopics.objects.all()

        serializer = BugTopics_Serializer(topics,many=True)
        return JsonResponse(serializer.data,safe=False)

# @api_view(['GET'])
# def get_bugReportTopicwise(request):

#     if request.method == 'GET':
#         topics = bugTopics.objects.all()

#         serializer = BugTopics_Reports_Serializers(topics,many=True)
#         return JsonResponse(serializer.data,safe=False)