from flask import Flask,request
from flask import render_template
from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

app = Flask(__name__)


@app.route('/',methods =["GET", "POST"])
def home():

    if request.method=='POST':
        first_name = request.form.get("fname")
        email = request.form.get("email")
        feedback = request.form.get("feedback")
        rating = request.form.get("rating")
        result = f'Name: {first_name} \n email: {email} \n Feedback: {feedback} \n Rating: {rating}'
        print(result)
        print()
        print(sentimentAnalyzer(feedback))
        
    return render_template('index.html')

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


if __name__ == '__main__':
    app.run(debug=True)