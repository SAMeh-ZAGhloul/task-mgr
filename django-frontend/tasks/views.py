from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
import requests
from requests.exceptions import RequestException
from datetime import datetime
from .forms import TaskForm

def task_list(request):
    """Main view for displaying tasks in a Kanban board layout"""
    try:
        response = requests.get(f"{settings.FLASK_BACKEND_URL}/tasks", timeout=5)
        response.raise_for_status()
        tasks = response.json()
    except RequestException as e:
        tasks = []
        messages.error(request, f"Could not connect to the backend server: {str(e)}")
    
    todo_tasks = [task for task in tasks if task['status'] == 'todo']
    inprogress_tasks = [task for task in tasks if task['status'] == 'inprogress']
    completed_tasks = [task for task in tasks if task['status'] == 'completed']
    
    context = {
        'todo_tasks': todo_tasks,
        'inprogress_tasks': inprogress_tasks,
        'completed_tasks': completed_tasks,
        'today': datetime.now().date()
    }
    
    return render(request, 'tasks/kanban.html', context)

def task_create(request):
    """View for creating a new task"""
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task_data = form.cleaned_data
            task_data['id'] = f"task-{int(datetime.now().timestamp()*1000)}-{datetime.now().strftime('%Y%m%d')}"
            task_data['status'] = 'todo'
            
            try:
                # Get current tasks
                response = requests.get(f"{settings.FLASK_BACKEND_URL}/tasks", timeout=5)
                response.raise_for_status()
                tasks = response.json()
                
                # Add new task
                tasks.append(task_data)
                
                # Save updated tasks
                response = requests.post(
                    f"{settings.FLASK_BACKEND_URL}/tasks",
                    json=tasks,
                    timeout=5
                )
                response.raise_for_status()
                
                messages.success(request, "Task created successfully!")
                return redirect('task_list')
            except RequestException as e:
                messages.error(request, f"Could not connect to the backend server: {str(e)}")
    else:
        form = TaskForm()
    
    return render(request, 'tasks/task_form.html', {'form': form, 'action': 'Create'})

def task_edit(request, task_id):
    """View for editing an existing task"""
    try:
        response = requests.get(f"{settings.FLASK_BACKEND_URL}/tasks", timeout=5)
        response.raise_for_status()
        tasks = response.json()
        task = next((t for t in tasks if t['id'] == task_id), None)
        
        if not task:
            messages.error(request, "Task not found")
            return redirect('task_list')
        
        if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                updated_task = form.cleaned_data
                updated_task['id'] = task_id
                updated_task['status'] = task['status']
                
                # Update task in list
                tasks = [updated_task if t['id'] == task_id else t for t in tasks]
                
                # Save updated tasks
                response = requests.post(
                    f"{settings.FLASK_BACKEND_URL}/tasks",
                    json=tasks,
                    timeout=5
                )
                response.raise_for_status()
                
                messages.success(request, "Task updated successfully!")
                return redirect('task_list')
        else:
            form = TaskForm(initial=task)
        
        return render(request, 'tasks/task_form.html', {
            'form': form,
            'action': 'Edit',
            'task': task
        })
        
    except RequestException as e:
        messages.error(request, f"Could not connect to the backend server: {str(e)}")
        return redirect('task_list')

def task_delete(request, task_id):
    """View for deleting a task"""
    if request.method == 'POST':
        try:
            response = requests.get(f"{settings.FLASK_BACKEND_URL}/tasks", timeout=5)
            response.raise_for_status()
            tasks = response.json()
            
            # Remove task from list
            tasks = [t for t in tasks if t['id'] != task_id]
            
            # Save updated tasks
            response = requests.post(
                f"{settings.FLASK_BACKEND_URL}/tasks",
                json=tasks,
                timeout=5
            )
            response.raise_for_status()
            
            messages.success(request, "Task deleted successfully!")
        except RequestException as e:
            messages.error(request, f"Could not connect to the backend server: {str(e)}")
    
    return redirect('task_list')

def task_move(request, task_id, direction):
    """View for moving tasks between columns"""
    if request.method == 'POST':
        try:
            response = requests.get(f"{settings.FLASK_BACKEND_URL}/tasks", timeout=5)
            response.raise_for_status()
            tasks = response.json()
            task = next((t for t in tasks if t['id'] == task_id), None)
            
            if task:
                # Update task status based on direction
                if direction == 'next':
                    if task['status'] == 'todo':
                        task['status'] = 'inprogress'
                    elif task['status'] == 'inprogress':
                        task['status'] = 'completed'
                elif direction == 'prev':
                    if task['status'] == 'completed':
                        task['status'] = 'inprogress'
                    elif task['status'] == 'inprogress':
                        task['status'] = 'todo'
                
                # Save updated tasks
                response = requests.post(
                    f"{settings.FLASK_BACKEND_URL}/tasks",
                    json=tasks,
                    timeout=5
                )
                response.raise_for_status()
            else:
                messages.error(request, "Task not found")
        except RequestException as e:
            messages.error(request, f"Could not connect to the backend server: {str(e)}")
    
    return redirect('task_list')
