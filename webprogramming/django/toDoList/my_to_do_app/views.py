# my_to_do_app > views.py
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import * # models.py에서 생성된 객체 모두 import(class Todo)

# Create your views here.
def index(request):
     todos = Todo.objects.all() # Todo 클래스 이용해 db에 저장된 모든 레코드 select
     content = {'todos': todos} #content dict 생성
     return render(request, 'my_to_do_app/index.html', content) #index.html 파일로 전달
     # # return HttpResponse("my_to_do_app first page")
     # return render(request, 'my_to_do_app/index.html')

def createTodo(request):
     user_input_str = request.POST['todoContent']
     new_todo = Todo(content=user_input_str)
     new_todo.save()
     return HttpResponseRedirect(reverse('index'))
     # return HttpResponse("DB에 저장되었어요 =>" + user_input_str)

def doneTodo(request):
    done_todo_id = request.GET['todoNum']
    print("완료한 todo의 id",done_todo_id)
    todo = Todo.objects.get(id = done_todo_id)
    todo.isDone = True
    todo.save()
    return HttpResponseRedirect(reverse('index'))

# def deleteTodo(request):
#     done_todo_id = request.GET['todoNum']
#     print("완료한 todo의 id",done_todo_id)
#     todo = Todo.objects.get(id = done_todo_id)
#     # todo.isDone = True
#     todo.delete()
#     return HttpResponseRedirect(reverse('index'))




