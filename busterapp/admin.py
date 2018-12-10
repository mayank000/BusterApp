from django.contrib import admin
from .models import Task , Project 
from users.models import UserProfile

admin.site.register(Task)
admin.site.register(Project)
admin.site.register(UserProfile)
