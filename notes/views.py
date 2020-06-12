from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm
from django.contrib import messages

# Create your views here.


def home(request):
    list = Todo.objects.filter(finished=False)
    finished = Todo.objects.filter(finished=True)
    form = TodoForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get('name')
        date = form.cleaned_data.get('date')

        todo = Todo(
            name=name,
            date=date,
        )
        todo.save()
        messages.info(request, "Task was created, let's get to work")
        return redirect('notes:home')

    context = {
        'list': list,
        'form': form,
        "finished": finished
    }

    return render(request, 'index.html', context)


def done(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.finished = True
    todo.save()
    messages.info(request, 'Task was done!! YAY ')
    return redirect('notes:home')


def undo(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.finished = False
    todo.save()
    messages.info(request, 'To-do was unchecked!! Do you want to redo it?')
    return redirect('notes:home')


def delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    messages.info(request, "Task was deleted!! Let's do another")
    return redirect('notes:home')
