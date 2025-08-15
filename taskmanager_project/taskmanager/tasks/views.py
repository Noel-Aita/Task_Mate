from rest_framework import viewsets                         # ViewSet provides built-in support for CRUD operations.
from rest_framework.decorators import action                # Used to define custom actions like mark_complete.
from rest_framework.response import Response                # Used to send JSON responses to the client.
from rest_framework import status                           # Provides HTTP status codes like 200 OK, 404 Not Found.
from .models import Task                                     # Importing the Task model from models.py
from .serializers import TaskSerializer                      # Importing the serializer to convert Task <-> JSON

class TaskViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides:
    - list():     GET /api/tasks/
    - retrieve(): GET /api/tasks/<id>/
    - create():   POST /api/tasks/
    - update():   PUT /api/tasks/<id>/
    - destroy():  DELETE /api/tasks/<id>/
    
    It also includes custom actions to mark tasks as complete/incomplete.
    """
    
    queryset = Task.objects.all()                            # Query all tasks from the database.
    serializer_class = TaskSerializer                        # Use the TaskSerializer to handle JSON conversion.

    @action(detail=True, methods=['post'])
    def mark_complete(self, request, pk=None):
        """
        Custom POST endpoint: /api/tasks/<id>/mark_complete/
        Marks a specific task as completed.
        """
        task = self.get_object()                             # Get the task instance from the database.
        task.completed = True                                # Mark it as complete.
        task.save()                                          # Save the updated task.
        return Response(
            {'status': '✅ Task marked as complete'},
            status=status.HTTP_200_OK
        )

    @action(detail=True, methods=['post'])
    def mark_incomplete(self, request, pk=None):
        """
        Custom POST endpoint: /api/tasks/<id>/mark_incomplete/
        Marks a specific task as NOT completed.
        """
        task = self.get_object()                             # Get the task instance by ID.
        task.completed = False                               # Mark it as incomplete.
        task.save()                                          # Save the change.
        return Response(
            {'status': '🚫 Task marked as incomplete'},
            status=status.HTTP_200_OK
        )
