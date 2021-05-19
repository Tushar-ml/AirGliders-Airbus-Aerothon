from django.contrib import admin

# Register your models here.
from .models import Feedback,bugReport

admin.site.register(Feedback)
admin.site.register(bugReport)