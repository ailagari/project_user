from tkinter import CASCADE
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=255)
    assigned = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    
    def __str__(self):
        return self.name


class Worktime(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='Worktimes')
    start_time = models.DateTimeField(unique=True)
    end_time = models.DateTimeField(unique=True)

    def __str__(self):
        return self.project
