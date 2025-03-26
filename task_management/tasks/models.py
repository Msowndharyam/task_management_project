from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    """
    Custom user model extending Django's AbstractUser
    Adds mobile field and allows for additional user-related information
    """
    mobile = models.CharField(max_length=15, blank=True, null=True)
    
    def __str__(self):
        return self.username

class Task(models.Model):
    """
    Task model representing tasks in the system
    """
    TASK_TYPES = [
        ('PERSONAL', 'Personal'),
        ('WORK', 'Work'),
        ('STUDY', 'Study'),
        ('OTHER', 'Other')
    ]

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled')
    ]

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    task_type = models.CharField(max_length=20, choices=TASK_TYPES, default='OTHER')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    
    # Many-to-Many relationship with users
    assigned_users = models.ManyToManyField(User, related_name='tasks')

    def __str__(self):
        return self.name

    def mark_completed(self):
        """
        Helper method to mark task as completed
        """
        self.status = 'COMPLETED'
        self.completed_at = timezone.now()
        self.save()