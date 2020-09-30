from django.shortcuts import render
from .models import Todo
from . import transformer
from todoproject.response import Response
import json


# Create your views here.
def view_todo(request, user_id):
    if request.method == 'GET':
        todo = Todo.objects.filter(user_id=user_id)
        todo = transformer.transform(todo)
        return Response.ok(values=todo)

    else:
        return Response.bad_request(message='Invalid method')


def add_todo(request, user_id):
    if request.method == 'POST':
        json_data = json.loads(request.body)

        todo = Todo()

        todo.task = json_data['task']
        todo.user = user_id
        todo.save()

        return Response.ok(values=transformer.single_transform(todo),
                           message='Task added successfully!')
    else:
        return Response.bad_request(message='Invalid method!')


def up_del_todo(request, user_id, task_id):
    if request.method == 'PUT':
        json_data = json.loads(request.body)

        todo = Todo.objects.filter(id=task_id, user_id=user_id).first()

        if not todo:
            return Response.bad_request(message="Task not found!")

        todo.task = json_data['task']
        todo.user_id = user_id
        todo.save()

        return Response.ok(values=transformer.single_transform(todo),
                           message='Task updated!')

    elif request.method == 'DELETE':
        todo = Todo.objects.filter(id=task_id, user_id=user_id).first()
        todo.delete()

        if not todo:
            return Response.bad_request(message='Task not found!')

        return Response.ok(message='Task deleted!')

    else:
        return Response.bad_request(message='Invalid method!')
