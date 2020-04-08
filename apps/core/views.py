from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tasks.models import Category, Task
from datetime import datetime

# Create your views here.
@login_required(login_url='/usuarios/login/')
def home(request):
    template_name = 'core/home.html'
    tasks = Task.objects.filter(owner__username=request.user, end_date=datetime.today()).exclude(status='CD')
    context = {
        'tasks': tasks
    }
    return render(request, template_name, context)

@login_required()
def search_tasks(request):
    template_name = 'core/search_tasks.html'
    query = request.GET.get('query')
    param_search = query
    tasks = Task.objects.filter(
        owner__username=request.user, 
        name__icontains=query
    )
    context = {
        'tasks': tasks,
        'param_search': param_search
    }
    return render(request, template_name, context)
