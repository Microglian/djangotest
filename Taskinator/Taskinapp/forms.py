from django import forms # type: ignore
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "body", "author", "due_date"]