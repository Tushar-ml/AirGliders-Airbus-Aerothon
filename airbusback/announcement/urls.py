from django.urls import path,include
from .views import get_announcements,add_announcement

urlpatterns = [
    path('get/',get_announcements,name='get-announcements'),
    path('add/',add_announcement,name='add-announcement'),
]