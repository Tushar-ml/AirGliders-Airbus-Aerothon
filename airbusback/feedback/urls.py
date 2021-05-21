from django.urls import path,include
from .views import get_bugReport, add_feedback, get_topics,add_bugReport,feedback_page
urlpatterns = [
    path('',feedback_page,name='feedback-page'),
    path('add/',add_feedback,name='add-feedback'),
    path('bug/get/',get_bugReport,name='get-bugreport'),
    path('bug/add/',add_bugReport.as_view(),name="add-bugreport"),
    path('bug/topics/get/',get_topics,name='get-bugTopics'),
    # path('bug/topics/reports/get/',get_bugReportTopicwise,name='get-bugReportTopicwise'),
]