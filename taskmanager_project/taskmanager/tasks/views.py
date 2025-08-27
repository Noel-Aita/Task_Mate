# views.py
from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth import get_user_model
from .models import Task, TaskCategory, TaskUpdate, EducationalResource
from .serializers import (
    UserSerializer, UserRegistrationSerializer, TaskSerializer, 
    TaskCategorySerializer, TaskUpdateSerializer, EducationalResourceSerializer
)
from .permissions import IsOwnerOrAdmin, IsTechnician

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_permissions(self):
        if self.action == 'create':
            return []  # No auth needed for registration
        elif self.action in ['update', 'partial_update', 'destroy']:
            return [IsOwnerOrAdmin()]
        return [IsAdminUser()]  # Only admin can list users

    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'user': UserSerializer(user).data,
                'message': 'User created successfully'
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Filters tasks based on users role, 
        - admins can see all tasks while 
        technicians only see tasks assigned to them"""
        user = self.request.user
        if user.is_staff or user.role == 'admin':
            return Task.objects.all()
        return Task.objects.filter(assigned_to=user) | Task.objects.filter(created_by=user)

    def perform_create(self, serializer):
        """sets the created-by field to the current user when creating a task"""
        serializer.save(created_by=self.request.user)

    @action(detail=True, methods=['post'])
    def toggle_completion(self, request, pk=None):
        """custom action to change completion status"""
        task = self.get_object()
        
        # Check if user has permission to update this task
        if not (request.user.is_staff or task.assigned_to == request.user or task.created_by == request.user):
            return Response({'error': 'You do not have permission to update this task'}, 
                           status=status.HTTP_403_FORBIDDEN)
        
        # Toggle completion status
        if task.status == 'completed':
            task.status = 'in_progress'
        else:
            task.status = 'completed'
        
        task.save()
        
        # Create an update record
        TaskUpdate.objects.create(
            task=task,
            updated_by=request.user,
            update_text=f"Status changed to {task.status}",
            status_change=task.status
        )
        
        return Response({'status': 'task status updated', 'new_status': task.status})
    @action(detail=True, methods=['get'])
    def updates(self, request, pk=None):
        """
        Custom action to get all updates for a specific task
        """
        task = self.get_object()
        updates = task.updates.all()
        serializer = TaskUpdateSerializer(updates, many=True)
        return Response(serializer.data)

class TaskCategoryViewSet(viewsets.ModelViewSet):
    """ to see the category model"""
    queryset = TaskCategory.objects.all()
    serializer_class = TaskCategorySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['name', 'description']
    search_fields = ['name', 'id']
    ordering = ['name']

class TaskUpdateViewSet(viewsets.ModelViewSet):
    """to see taskupdate model"""
    queryset = TaskUpdate.objects.all()
    serializer_class = TaskUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """filters task update based on user roles,
        - admins can see all updates'
        - tchnicians can see updates made by them only"""
        user = self.request.user
        if user.is_staff:
            return TaskUpdate.objects.all()
        return TaskUpdate.objects.filter(updated_by=user)

    def perform_create(self, serializer):
        serializer.save(updated_by=self.request.user)

class EducationalResourceViewSet(viewsets.ModelViewSet):
    queryset = EducationalResource.objects.all()
    serializer_class = EducationalResourceSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)