from django.http.response import JsonResponse
from django.shortcuts import render
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import os
import openai

openai.api_key = "sk-0LtZ6txoWVSBeK27yVXYfeSwLksdtDZ2CsnwBMKf"
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


def chatbot(request):    
    return render(request,"chatbot/chatbot.html")


def get_bot_response(request):
	global chat_log
	print(request)
	print(request.GET)
	userText = dict(request.GET.items())['msg']
	answer = ask(userText)
	chat_log = append_interaction_to_chat_log(userText, answer, chat_log)
	res = {
		'answer':answer
	}
	return JsonResponse(res)