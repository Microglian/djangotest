from django import forms # type: ignore
from .models import Task, User

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "body", "author", "due_date"]
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["name"]