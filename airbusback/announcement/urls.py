from django.urls import path,include
from .views import get_announcements,add_announcement,announcement

urlpatterns = [
    path('',announcement,name='announcement'),
    path('get/',get_announcements,name='get-announcements'),
    path('add/',add_announcement,name='add-announcement'),
]