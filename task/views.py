from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

import task
from task.models import Task


# Create your views here.
def home(request):
    return render(request, 'task/index.html')

def modal_create(request):
    return render(request, 'task/modal_create.html')

def task_view(request, sms, code, css_class):
    context = {
        'deleted_count': Task.delete.all().count(),
        'done_delete_count': Task.done_delete.all().count(),
    }

    return render(request, 'task/index.html', context)

@login_required
def home_view(request):
    return task_view(request, 'Bajarilmagan', 'TODO', 'warning')

@login_required
def task_done_view(request):
    return task_view(request, 'Bajarilgan', 'DONE', 'success')

@login_required
def task_delete_view(request):
    return task_view(request, 'O`chirilgan', 'DELETE', 'danger')

@login_required
def done_delete_task_view(request):
    return task_view(request, 'Bajarilgan va O`chirilgan', 'DONE & DELETE', 'dark')

@login_required
def search(request):
    q = request.POST.get('search', '') if request.method == 'POST' else request.GET.get('search', '')

    if not q.strip():
        tasks = Task.objects.none()
    else:
        tasks = Task.objects.filter(title__icontains=q)

    task_count = tasks.count()
    paginator = Paginator(tasks, 7)
    page_number = request.GET.get('page')
    tasks = paginator.get_page(page_number)

    if task_count > 0:
        messages.success(request, f"{q} {'haqida' if q else ''} {task_count} ta malumot topildi!")
    else:
        messages.success(request, f"{q} haqida malumot topilmadi!")

    context = {
        'tasks': tasks,
        'form': TaskForm(),
        'class': 'dark',
        'sms': 'Qidirilgan',
        'todo_count': Task.todo.all().count(),
        'done_count': Task.done.all().count(),
        'deleted_count': Task.delete.all().count(),
        'done_delete_count': Task.done_delete.all().count(),
        'search': q
    }

    return render(request, 'task/index.html', context)

def custom_redirect(request):
    if task.is_done and task.is_delete:
        return redirect('done-delete-task-view')
    elif task.is_delete:
        return redirect('task-delete-view')
    elif task.is_done:
        return redirect('task-done-view')
    else:
        return redirect('home-view')

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            messages.success(request, f"{task.title} Topshiriq muvaffaqqiyatli yaratildi!")
            return custom_redirect(task)

@login_required

def edit_task(request):
    if request.method == 'POST':
        task_id = request.POST['task_id']
        task = Task.objects.get(pk=task_id)
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.is_done = request.POST['done', 'off'] == 'on'
        task.is_delete = request.POST['delete', 'off'] == 'on'
        task.save()
        messages.success(request, f"{task.title} topshiriq o`zgartirildi")
        #custom redirect

        return custom_redirect(task)

@login_required
def done_task(request):
    if request.method == 'POST':
        task_id = request.POST['task_id']
        task = Task.objects.get(pk=task_id)
        task.done = True
        task.save()
        messages.success(request, f"{task.title} Topshiriq muvaffaqqiyatli bajarildi")

        return custom_redirect(task)

@login_required

def delete_task(request):
    if request.method == 'POST':
        task_id = request.POST['task_id']
        task = Task.objects.get(pk=task_id)
        task.is_delete = True
        task.save()
        messages.success(request, f"{task.title} Topshiriq o`chirildi!")

        return custom_redirect(task)