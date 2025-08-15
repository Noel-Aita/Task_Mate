# tasks/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet  # Import the viewset we just created

# Create a router and register the TaskViewSet
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

# Include the router's URLs
urlpatterns = [
    path('', include(router.urls)),  # This will create /tasks/ and related endpoints
]
