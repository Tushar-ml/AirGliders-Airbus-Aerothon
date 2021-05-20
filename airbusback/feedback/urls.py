from django.urls import path,include
from .views import get_bugReport, add_feedback, get_topics,add_bugReport

urlpatterns = [
    path('add/',add_feedback,name='add-feedback'),
    path('bug/get/',get_bugReport,name='get-bugreport'),
    path('bug/add/',add_bugReport,name="add-bugreport"),
    path('bug/topics/get/',get_topics,name='get-bugTopics'),
    # path('bug/topics/reports/get/',get_bugReportTopicwise,name='get-bugReportTopicwise'),
]