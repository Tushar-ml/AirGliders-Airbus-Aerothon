from django.urls import path,include
from .views import add_feedback

urlpatterns = [
    path('add/',add_feedback,name='add-feedback'),
]
