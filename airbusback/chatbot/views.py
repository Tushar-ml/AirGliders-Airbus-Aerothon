from django.shortcuts import render

# Create your views here.
import speech_recognition as sr
# from tts import female


import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate',180)
def male(audio):
   engine.setProperty('voice',voices[0].id)
   engine.say(audio)
   engine.runAndWait()
   return -1

def female(audio):
   engine.setProperty('voice',voices[1].id)
   engine.say(audio)
   engine.runAndWait()
   return -1


def rect():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please Speak")
        female("Please Speak")
        r.pause_threshold=1 
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        print(audio.__repr__())
        print("Analyzing \...") 
        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
            female("You said : {}".format(text))
            return text
        except:
            print("Sorry could not recognize what you said")
            female("Sorry could not recognize what you said")
            rect()

import os
import openai
# from speak import rect
# from tts import female

openai.api_key = "OPENAI API KEY"
q=1
while(True):
  female("enter your queries:")
  inprompt=rect()
  oprompt=str("The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nUser: Hello, who are you?\nAI: I am an AI assistant. How can I help you today?\nUser: ")
  oprompt=oprompt+inprompt+"\n"
  female("enter q:")
  q=int(rect("enter q:"))
  response = openai.Completion.create(
    engine="davinci",
    prompt=oprompt,
    temperature=0.9, 
    max_tokens=50,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=["\n", " User:", " AI:"]
  )
  female(response["choices"][0]["text"])
  print(response["choices"][0]["text"])
  if(q==1):
    break