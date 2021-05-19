import os
import openai
from speak import rect
from tts import female

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