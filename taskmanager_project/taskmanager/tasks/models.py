from django.db import models
from django.conf import settings  # <-- important for custom user FK

# Custom User model
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('electrician', 'Electrician'),
        ('plumber', 'Plumber'),
        ('carpenter', 'Carpenter'),
        ('hvac', 'HVAC Technician'),
        ('solar', 'Solar Technician'),
        ('general', 'General Technician'),
    )
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='general')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    license_number = models.CharField(max_length=50, blank=True, null=True)
    certification = models.CharField(max_length=100, blank=True, null=True)
    experience_years = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"


class TaskCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    required_certification = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.name


class Task(models.Model):
    PRIORITY_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent'),
    )
    
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('assigned', 'Assigned'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='created_tasks',
        null=True,
        blank=True
    )
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_tasks'
    )
    category = models.ForeignKey(TaskCategory, on_delete=models.SET_NULL, null=True, blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(null=True, blank=True)
    estimated_hours = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    actual_hours = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    required_tools = models.TextField(blank=True, null=True)
    safety_notes = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.title


class TaskUpdate(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='updates')
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    update_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status_change = models.CharField(max_length=15, choices=Task.STATUS_CHOICES, null=True, blank=True)
    
    def __str__(self):
        return f"Update for {self.task.title} by {self.updated_by.username}"


class EducationalResource(models.Model):
    RESOURCE_TYPES = (
        ('specification', 'Specification'),
        ('standard', 'Standard'),
        ('guide', 'Guide'),
        ('safety', 'Safety Protocol'),
        ('video', 'Video Tutorial'),
    )
    
    title = models.CharField(max_length=200)
    resource_type = models.CharField(max_length=15, choices=RESOURCE_TYPES)
    description = models.TextField()
    url = models.URLField()
    category = models.ForeignKey(TaskCategory, on_delete=models.SET_NULL, null=True, blank=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    added_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
