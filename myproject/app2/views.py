from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Task
from .forms import TaskForm, TaskEditForm


def home(request):
    tasks = Task.objects.all()
    form = TaskForm()
    return render(request, 'app2/home.html', {
        'tasks': tasks,
        'form': form,
    })


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'تمت إضافة المهمة بنجاح إلى قاعدة البيانات!')
    return redirect('app2:home')


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskEditForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, f'تم تحديث المهمة "{task.title}" بنجاح!')
            return redirect('app2:home')
    else:
        form = TaskEditForm(instance=task)
    return render(request, 'app2/edit.html', {
        'form': form,
        'task': task,
    })


def toggle_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        task.is_completed = not task.is_completed
        task.save()
        status_text = "مكتملة ✅" if task.is_completed else "قيد التنفيذ ⏳"
        messages.success(request, f'تم تغيير حالة المهمة إلى {status_text}!')
    return redirect('app2:home')


def delete_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        messages.success(request, f'تم حذف المهمة "{task.title}" بنجاح!')
    return redirect('app2:home')
