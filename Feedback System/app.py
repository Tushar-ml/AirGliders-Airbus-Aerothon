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
    
    sentiment = 'Neutral'
    if feedback != None:
        sent = sia.polarity_scores(feedback)
        #sent.pop('compound')
        comp = sent['compound']
        if comp>0.05:
            sentiment = 'Positive'
        elif comp<-0.05:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'
    return sentiment


if __name__ == '__main__':
    app.run(debug=True)