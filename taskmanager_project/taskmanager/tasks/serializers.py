from rest_framework import serializers
from .models import Task

# This serializer converts Task model instances to JSON and vice versa
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task  # Use the Task model
        fields = '__all__'  # Include all fields from the model
