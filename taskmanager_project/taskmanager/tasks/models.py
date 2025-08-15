from django.db import models

# Task model represents a technician's task in the database
class Task(models.Model):
    # Predefined technician types (dropdown choices)
    TECHNICIAN_CHOICES = [
        ('electrician', 'Electrician'),
        ('solar', 'Solar Technician'),
        ('cctv', 'CCTV Installer'),
    ]

    title = models.CharField(max_length=255)
    # A short title or name of the task (e.g., "Install inverter")

    description = models.TextField(blank=True)
    # Detailed explanation of what the task involves (can be left empty)

    is_complete = models.BooleanField(default=False)
    # A checkbox to indicate if the task has been completed

    technician_type = models.CharField(
        max_length=20,
        choices=TECHNICIAN_CHOICES
    )
    # Dropdown for technician type — e.g., Electrician, Solar Tech, etc.

    created_at = models.DateTimeField(auto_now_add=True)
    # Automatically records the date and time when the task was created

    def __str__(self):
        # This makes Django show the task title in the admin panel
        return self.title
