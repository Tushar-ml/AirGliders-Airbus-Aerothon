import requests
from rest_framework.views import APIView
from .serializers import BugReport_Serializer, BugTopics_Serializer, Feedback_Serializer, BugReportAdd_Serializer
from django.contrib.auth.models import AnonymousUser, User
from django.shortcuts import render
from rest_framework import serializers
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
# Create your views here.
from .models import Feedback, bugReport,bugTopics

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

@api_view(['GET','POST'])
def add_feedback(request):
    '''
    Handles both the GET and POST requests

    GET Request returns all the Feedback Records

    POST Request process the sentiment from the description provided and predict "Sentiment" and "Score" add the received object to database 

    :param: Request Object {
        "name" : string (Username),
        "email" : string (Email Address),
        "description" : string,
        "rating" : int
    }
    '''

    if request.method == 'GET':
        feedbacks = Feedback.objects.all()

        serializer = Feedback_Serializer(feedbacks,many=True)
        return JsonResponse(serializer.data,safe=False)

    if request.method=='POST':
        data = dict(request.POST.items())
        sentiment,score = sentimentAnalyzer(data['description'])
        data['sentiment'],data['score'] = sentiment,score
        serializer = Feedback_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            context = {
                'success' : "Feedback is Successfully Submitted"
            }
            return render(request,'feedback/index.html',context=context)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET','POST'])
def get_bugReport(request):
    '''
    Returns all the Bug Reports in JSON Format
    '''
    

    if request.method == 'GET':
        bugReports = bugReport.objects.all()

        serializer = BugReport_Serializer(bugReports,many=True)
        return JsonResponse(serializer.data,safe=False)

    if request.method == 'POST':
        bugReports = JSONParser().parse(request)

        serializer = BugReport_Serializer(bugReports)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,safe=False)
        return JsonResponse(serializer.errors,safe=False)


# @api_view(['POST'])
class add_bugReport(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def post(self,request):

        '''
        Handles POST request to add BugReport

        :param: Request Object {
            "user" : string, (email address)
            "topic" : string, (topic name)
            "title" : string,
            "description" : string,
            "screenshot" : imagefile
        }

        :return: JSON object (which is stored in the database)
        '''
        
        # print(request.data)
        # data = JSONParser().parse(request)
        # data = MultiPartParser()
        # useremailtmp = User.objects.filter(email=request.get('user'))
        # topicnametmp = bugTopics.objects.filter(topicname=request.get('topic'))
        # if len(useremailtmp)>0:
        #     request.set['user'] = useremailtmp[0].pk
        # if len(topicnametmp)>0:
        #     request.data['topic'] = topicnametmp[0].pk
        # print(request.POST.set('user'))
        print(request.data)
        serializer = BugReportAdd_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            context = {
                "successful" : "Bug Successfully Submitted"
            }
            return render(request,'feedback/bugreport.html',context=context)
        
        return Response(serializer.errors,status=400)

@api_view(['GET'])
def get_topics(request):
    '''
    Returns list of the topics for Bugs

    :param: topicname : string

    '''

    if request.method == 'GET':
        topics = bugTopics.objects.all()

        serializer = BugTopics_Serializer(topics,many=True)
        return JsonResponse(serializer.data,safe=False)

def feedback_page(request):
    '''
    Return HTML Page for taking Feedback from user

    '''


    return render(request,'feedback/index.html')

# @api_view(['GET'])
# def get_bugReportTopicwise(request):

#     if request.method == 'GET':
#         topics = bugTopics.objects.all()

#         serializer = BugTopics_Reports_Serializers(topics,many=True)
#         return JsonResponse(serializer.data,safe=False)

def sentimentAnalyzer(feedback):
    '''
    Analyses the Sentiment from the string

    :params: feedback : string

    :return: sentiment("Postive","Neutral","Negative")

    '''


    score = 0
    sentiment = 'Neutral'
    if feedback != None:
        sent = sia.polarity_scores(feedback)
        sent.pop('compound')
        sent = list(sent.items())
        sent.sort(key=lambda x:x[1],reverse=True)
        score = sent[0][1]
        sentiment = sent[0][0]
    if sentiment == 'pos':
        sentiment = 'Positive'
    elif sentiment == 'neg':
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    return sentiment,score

def bugreport(request):

    topics = requests.get('http://127.0.0.1:8000/feedback/bug/topics/get/')
    topics = topics.json()
    print(topics)

    context = {
        "topics" : topics
    }
    return render(request,'feedback/bugreport.html',context=context)