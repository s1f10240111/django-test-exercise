from django.shortcuts import render
from .models import Task
from django.utils.dateparse import parse_datetime
from django.utils.timezone import make_aware

def index(request):
    if request.method == 'POST':
        task = Task(
            title=request.POST['title'],
            due_at=make_aware(parse_datetime(request.POST['due_at']))
        )
        task.save()
    if request.GET.get('order') == 'due':
        tasks = Task. objects. order_by('due_at' )
    else:
        tasks = Task. objects. order_by('-posted_at')    
    # POSTの後もGETでも共通でタスクリストを取得して表示
    context = {
        'tasks': tasks
    }
    return render(request, 'todo/index.html', context)
