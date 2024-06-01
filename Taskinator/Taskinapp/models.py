from django.db import models # type: ignore

# Create your models here.
class User(models.Model):
    """
    Model representing a User.
    
    Fields:
    - name: CharField for User name, max 15 characters.
    """
    name = models.CharField(max_length=15, unique=True)

class Task(models.Model):
    """
    Model representing a Task.
    
    Fields:
    - title: CharField for task title, max 100 characters.
    - body: TextField for task body text.
    - due_date: DateTimeField for when the task needs to be completed.
    
    Relationships:
    - author: ForeignKey representing task author.
    """
    
    title = models.CharField(max_length=100)
    body = models.TextField()
    due_date = models.DateTimeField()
    
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="+")
