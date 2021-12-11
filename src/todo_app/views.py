from django.shortcuts import redirect, render

from .forms import TodoForm
from .models import Todo


def todo_list(request):
    todos = Todo.objects.all()
    context = {
        'todo_list': todos
    }
    return render(request, 'todo_app/todo_list.html', context)


def todo_detail(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        'todo': todo
    }
    return render(request, 'todo_app/todo_detail.html', context)


def todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {'form': form}
    return render(request, 'todo_app/todo_create.html', context)


def todo_update(request, id):
    todo = Todo.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {'form': form}
    return render(request, 'todo_app/todo_update.html', context)


def todo_delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('/')
