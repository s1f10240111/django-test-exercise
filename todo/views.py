from django.shortcuts import render, redirect
from django.http import Http404
from django.utils.timezone import make_aware
from django.utils.dateparse import parse_datetime
from .models import Task

def index(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        due_str = request.POST.get('due_at', '')
        due = make_aware(parse_datetime(due_str)) if due_str else None

        if title:
            Task.objects.create(title=title, due_at=due)
            return redirect('index')  # ←これがないと更新されない！

    order = request.GET.get('order')
    if order == 'due':
        tasks = Task.objects.order_by('due_at')
    else:
        tasks = Task.objects.order_by('-posted_at')
    return render(request, 'todo/index.html', {'tasks': tasks})

def detail(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task. DoesNotExist:
        raise Http404("Task does not exist")

    context = {
    'task': task,
    }
    return render(request, 'todo/detail.html', context)
