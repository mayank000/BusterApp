# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render , redirect , get_object_or_404
from django.http import *
from users.models import UserProfile 
from django.http import HttpResponseRedirect

from .models import Project
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm , ProjectForm , TaskForm
from django.core.urlresolvers import reverse

from django.contrib.auth import authenticate, login
from .models import Project, Task
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login')
def home(request):
    users_data = UserProfile.objects.all()
    projects = Project.objects.filter(added_by = request.user)
    return render(request, 'busterapp/home.jinja', {'users_data' : users_data , 'projects' : projects})


def registration(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login')
    return render(request, 'busterapp/registration.jinja', { 'form': form})   

@login_required(login_url='/login')
def project(request):
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'busterapp/project.jinja', { 'form': form , })

@login_required(login_url='/login')
def update_project(request,project_id):
    child = Task.objects.filter(parent=None)
    alltask = Task.objects.all()
    projects = get_object_or_404(Project, id = project_id)
    tasks = Task.objects.filter(added_by = projects)
    form = ProjectForm(request.POST or None, instance = projects)
    if request.method == "POST":
        if form.is_valid():
            form_partial = form.save(commit=False)
            form_partial.added_by = request.user
            form_partial.save()
            return HttpResponseRedirect('/')
    return render (request,'busterapp/project_update.jinja', {'form' : form , 'projects' : projects , 'tasks' : tasks, 'alltask' :  alltask , 'child' : child } )        

@login_required(login_url='/login')
def task(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render (request, 'busterapp/task.jinja' , {'form' : form }) 

@login_required(login_url='/login')
def update_task(request,task_id):
    url_link = reverse('update_task' , kwargs={'task_id': task_id})
    tasks = get_object_or_404(Task, id=task_id)
    childs = Task.objects.filter(parent = tasks)
    task_name = tasks.added_by
    form = TaskForm(request.POST or None, instance = tasks)
    if request.method == "POST":
        if form.is_valid():
            form_partial = form.save(commit=False)
            form_partial.added_by = task_name
            form_partial.save()
            return HttpResponseRedirect(url_link)
    return render (request,'busterapp/task_update.jinja', {'form' : form , 'tasks' : tasks , 'childs' : childs } )   

@login_required(login_url='/login')
def taskchild(request,parent_id):
    url_link = reverse('taskchild' , kwargs={'parent_id': parent_id})
    tasks = get_object_or_404(Task, id=parent_id)
    childs = Task.objects.filter(parent = tasks)
    form = TaskForm(request.POST or None)
    if request.method == "POST":
        form_partial = form.save(commit=False)
        form_partial.parent = tasks
        form_partial.save()
        return HttpResponseRedirect(url_link)
    return render (request,'busterapp/taskchild.jinja', {'form' : form , 'tasks' : tasks, 'childs' : childs  } ) 


