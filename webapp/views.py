from django.shortcuts import render, get_object_or_404, redirect

from webapp.models import Task, status_choices

def task_list_view(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'task_list.html', context)

def task_detail_view(request, pk,):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_detail.html', {'task': task})


def task_create_view(request):
    if request.method == 'GET':
        return render(request, 'task_create.html', {'status_choices': status_choices})
    elif request.method == 'POST':
        description = request.POST.get('description')
        detailed_description = request.POST.get('detailed_description')
        status = request.POST.get('status')
        due_date = request.POST.get('due_date') or None
        task = Task.objects.create(description=description, detailed_description=detailed_description, status=status, due_date=due_date)
        return redirect('task_detail', pk=task.id)