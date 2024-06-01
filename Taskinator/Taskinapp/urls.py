from django.urls import path # type: ignore
from .views import task_list, task_details, task_create, task_update, task_delete

urlpatterns = [
    # List of tasks
    path('', task_list, name='task_list'),
    
    # Task details
    path('task/<int:pk>/', task_details, name='task_details'),
    
    # New Task
    path('task/new/', task_create, name='task_create'),
    
    # Update Task
    path('task/<int:pk>/edit/', task_update, name='task_update'),
    
    # Task details
    path('task/<int:pk>/delete/', task_delete, name='task_delete'),
]