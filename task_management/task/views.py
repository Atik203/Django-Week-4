from django.shortcuts import redirect, render

from .forms import TaskForm
from .models import Task

# Create your views here.

def add_task(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:    
        return render(request, 'add_task.html', {'form': form})


def edit_task(request, id):
    task = Task.objects.get(pk=id)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        return render(request, 'edit_task.html', {'form': form})

def delete_task(request, id):
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect('home')