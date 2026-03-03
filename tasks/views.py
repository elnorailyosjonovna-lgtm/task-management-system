from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm
from .forms import TaskForm
from django.shortcuts import redirect
from .models import Task, Project
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Task


@login_required
def home(request):
    projects = Project.objects.filter(owner=request.user)
    return render(request, 'tasks/home.html', {'projects': projects})

@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            return redirect('home')
    else:
        form = ProjectForm()

    return render(request, 'tasks/create_project.html', {'form': form})

@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk, owner=request.user)
    tasks = Task.objects.filter(project=project)

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            form.save_m2m()
            return redirect('project_detail', pk=project.pk)
    else:
        form = TaskForm()

    return render(request, 'tasks/project_detail.html', {
        'project': project,
        'tasks': tasks,
        'form': form
    })
@login_required
def toggle_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk, project__owner=request.user)
    
    if task.status == 'pending':
        task.status = 'completed'
    else:
        task.status = 'pending'
        
    task.save()
    return redirect('project_detail', pk=task.project.pk)


@login_required
def delete_task(request, pk):
    task = get_object_or_404(
        Task,
        pk=pk,
        project__owner=request.user  # Security check
    )

    project_pk = task.project.pk
    task.delete()

    return redirect('project_detail', pk=project_pk)



@login_required
def edit_task(request, pk):
    task = get_object_or_404(
        Task,
        pk=pk,
        project__owner=request.user
    )

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('project_detail', pk=task.project.pk)
    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/edit_task.html', {'form': form})




@login_required
def toggle_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)

    # toggle logic
    if task.status == "COMPLETED":
        task.status = "PENDING"
    else:
        task.status = "COMPLETED"

    task.save()

    return redirect('project_detail', pk=task.project.pk)