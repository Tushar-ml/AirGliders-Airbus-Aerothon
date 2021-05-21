from django.urls import path,include
from .views import main_app

urlpatterns = [
    path('',main_app,name='main-page')
]