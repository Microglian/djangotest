from django.shortcuts import render, get_object_or_404, redirect # type: ignore
from .models import Task
from .forms import TaskForm

# Create your views here.
def task_list(request):
    """
    Displays a list of all tasks
    """
    tasks = Task.objects.all()
    context = {
        'tasks': tasks,
        'page_title': 'List of Tasks'
    }
    
    return render(request, 'task_list.html', context)


def task_details(request, pk):
    """
    Displays details of task primary_key
    """
    
    task = get_object_or_404(Task, pk=pk)
    
    return render(request, 'task_details.html', {'task': task})


def task_create(request):
    """
    Creates a new task
    """
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form})


def task_update(request, pk):
    """
    Updates a task
    """
    
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_form.html', {'form': form})


def task_delete(request, pk):
    """
    Deletes a task
    """
    
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')