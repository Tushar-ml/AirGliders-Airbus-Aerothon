from django.urls import path,include
from .views import chatbot,get_bot_response

urlpatterns = [
    path('',chatbot,name='chatbot'),
    path('get',get_bot_response,name='get-bot-response')
]