from django.contrib import admin
from .models import Task

# This makes the Task model appear in Django admin
admin.site.register(Task)
