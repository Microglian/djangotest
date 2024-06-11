from django import forms # type: ignore
from .models import Task, User

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "body", "author", "due_date"]
        # Override default widget to include date picker
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["name"]