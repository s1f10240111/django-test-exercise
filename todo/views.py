from django.shortcuts import render, get_object_or_404
from .models import Task
from django.utils.dateparse import parse_datetime
from django.utils.timezone import make_aware

def index(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        due_str = request.POST.get('due_at', '')
        due = make_aware(parse_datetime(due_str)) if due_str else None

        if title:
            Task.objects.create(title=title, due_at=due)

    order = request.GET.get('order')
    if order == 'due':
        tasks = Task.objects.order_by('due_at')
    else:
        tasks = Task.objects.order_by('-posted_at')

    return render(request, 'todo/index.html', {'tasks': tasks})

def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'todo/detail.html', {'task': task})
