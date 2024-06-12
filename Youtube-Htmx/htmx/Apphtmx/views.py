from django.shortcuts import render
from .models import *
def index(request):
    todos = Todo.objects.all()
    return render(request, "index.html",{"todos":todos})


def todo_add(request):

    if request.method == "POST":
        text = request.POST.get("text")
        todo = Todo.objects.create(text=text)
        todo.save()
        todos = Todo.objects.all()
        return render(request, "todo_list.html",{"todos":todos})
    
def todo_update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == "POST":
        text = request.POST.get("text")
        todo.text = text
        todo.save()
        todos = Todo.objects.all()
        return render(request, "todo_list.html",{"todos":todos})
    else:
        return render(request, "todo_update_input.html",{"todo":todo})

def todo_delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    todos = Todo.objects.all()
    return render(request, "todo_list.html",{"todos":todos})