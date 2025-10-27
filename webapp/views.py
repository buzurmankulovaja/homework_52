from django.http import HttpResponseRedirect
from django.shortcuts import render

from webapp.models import Task, status_choices

def task_list_view(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'task_list.html', context)

def task_create_view(request):
    if request.method == 'GET':
        return render(request, 'task_create.html', {'status_choices': status_choices})
    elif request.method == 'POST':
        description = request.POST.get('description')
        status = request.POST.get('status')
        due_date = request.POST.get('due_date')
        Task.objects.create(description=description, status=status, due_date=due_date)
        return HttpResponseRedirect('/')