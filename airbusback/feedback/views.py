# Create your views here.
from .models import Feedback
from django.shortcuts import render
from nltk.sentiment import SentimentIntensityAnalyzer
from rest_framework.decorators import api_view
sia = SentimentIntensityAnalyzer()

@api_view(['GET','POST'])
def add_feedback(request):

    if request.method=='POST':
        name = request.POST["fname"]
        email = request.POST["email"]
        feedback = request.POST["feedback"]
        rating = request.POST["rating"]
        f = Feedback(name=name, email=email,description=feedback,rating=rating)
        f.save()
        print(sentimentAnalyzer(feedback))
        
    return render(request,'index.html')

def sentimentAnalyzer(feedback):
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


if __name__ == '__main__':
    app.run(debug=True)