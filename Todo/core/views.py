from django.shortcuts import render, HttpResponse
from .models import Todo
from django.views.decorators.http import require_http_methods


# Create your views here.
def todos(request):
    todos = Todo.objects.all()

    context={'todos':todos}
    return render(request,'core/main.html', context)



@require_http_methods(['POST'])
def add_todo(request):
    todo = None
    title = request.POST.get('title', '')

    if title:
        todo = Todo.objects.create(title=title)

    context={'todo':todo}
    return render (request, 'core/partials/todo.html', context)

@require_http_methods(['PUT'])
def update_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.completed=True
    todo.save()
    context={'todo':todo}
    return render (request, 'core/partials/todo.html', context)

@require_http_methods(['DELETE'])
def delete_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return HttpResponse()


    