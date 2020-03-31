from django.shortcuts import render, get_object_or_404, redirect
from .forms import CategoryForm, TaskForm
from django.contrib import messages
from .models import Category, Task

# Create your views here.

def add_category(request):
    template_name = 'tasks/add_category.html'
    context = {}
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.owner = request.user
            f.save()
            messages.success(request, 'Adicionado com sucesso!')
    form = CategoryForm()
    context['form'] = form
    return render(request, template_name, context)

def list_categories(request):
    template_name = 'tasks/list_categories.html'
    categories = Category.objects.filter(owner=request.user)
    context = {
        'categories': categories
    }
    return render(request, template_name, context)

def edit_category(request, id_category):
    template_name = 'tasks/add_category.html'
    context = {}
    category = get_object_or_404(Category, id=id_category, owner=request.user)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            f = form.save(commit=False)
            f.owner = request.user
            f.save()
            messages.success(request, 'Modificado com sucesso!')
            return redirect('tasks:list_categories')
    form = CategoryForm(instance=category)
    context['form'] = form
    return render(request, template_name, context)

def delete_category(request, id_category):
    template_name = 'tasks/add_category.html'
    context = {}
    category = get_object_or_404(Category, id=id_category, owner=request.user)
    if category.delete():
        messages.success(request, 'Removido com sucesso!')
        return redirect('tasks:list_categories')
    else:
        messages.warning(request, 'Houve um problema e não foi possível executar a ação.')
        return redirect('tasks:list_categories')


def add_task(request):
    template_name = 'tasks/add_task.html'
    context = {}
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.owner = request.user
            f.save()
            form.save_m2m()
            messages.success(request, 'Adicionado com sucesso!')
    form = TaskForm()
    context['form'] = form
    return render(request, template_name, context)

def list_tasks(request):
    template_name = 'tasks/list_tasks.html'
    tasks = Task.objects.filter(owner=request.user)
    context = {
        'tasks': tasks
    }
    return render(request, template_name, context)

def edit_task(request, id_task):
    template_name = 'tasks/add_task.html'
    context = {}
    task = get_object_or_404(Task, id=id_task, owner=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            f = form.save(commit=False)
            f.owner = request.user
            f.save()
            messages.success(request, 'Modificado com sucesso!')
            return redirect('tasks:list_tasks')
    form = TaskForm(instance=task)
    context['form'] = form
    return render(request, template_name, context)

def delete_task(request, id_task):
    template_name = 'tasks/add_task.html'
    context = {}
    task = get_object_or_404(Task, id=id_task, owner=request.user)
    if task.delete():
        messages.success(request, 'Removido com sucesso!')
        return redirect('tasks:list_tasks')
    else:
        messages.warning(
            request, 'Houve um problema e não foi possível executar a ação.')
        return redirect('tasks:list_tasks')
