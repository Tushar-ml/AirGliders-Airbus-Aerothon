
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)


import os
import openai

openai.api_key = "OPEN_API_KEY"
completion = openai.Completion()

start_chat_log = '''Human: Hello, who are you?
AI: I am doing great. How can I help you today?
'''
chat_log = start_chat_log


def ask(question, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log
    prompt = f'{chat_log}Human: {question}\nAI:'
    response = completion.create(
        prompt=prompt, engine="davinci", stop=['\nHuman'], temperature=0.9,
        top_p=1, frequency_penalty=0, presence_penalty=0.6, best_of=1,
        max_tokens=150)
    answer = response.choices[0].text
    return answer
def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log
    return f'{chat_log}Human: {question}\nAI: {answer}\n'

@app.route("/")
def home():    
    return render_template("chatbot.html") 
@app.route("/get")
def get_bot_response():
    global chat_log
    userText = request.args.get('msg')
    answer = ask(userText)
    chat_log = append_interaction_to_chat_log(userText, answer, chat_log)  
    return str(answer)
if __name__ == "__main__":    
    app.run(debug=True)
