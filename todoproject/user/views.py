from django.contrib.auth.hashers import make_password
from django.core.serializers import json
from django.shortcuts import render
from todoproject.response import Response
from .models import Users
from . import transformer


# Create your views here.
def index(request):
    if request.method == 'GET':
        user = Users.objects.all()
        user = transformer.transform(user)
        return Response.ok(values=user)

    elif request.method == 'POST':
        json_data = json.loads(request.body)

        user = Users()
        user.name = json_data['name']
        user.email = json_data['email']
        user.password = make_password(password=json_data['password'])
        user.save()

        return Response.ok(
            values=transformer.single_transform(user),
            message="Added!"
        )

def show(request, id):
    if request.method == 'GET':
        user = Users.objects.filter(id=id).first()

        if not user:
            return Response.bad_request(message='Pengguna tidak ditemukan!')

        user = transformer.single_transform(user)
        return Response.bad_request(values=user)
    elif request.method == 'PUT':
        json_data = json.loads(request.body)
        user = Users.objects.filter(id=id).first()

        if not user:
            return Response.bad_request(message='Pengguna tidak ditemukan!')

        user.name = json_data['name']
        user.email = json_data['email']
        user.password = make_password(password=json_data['password'])
        user.save()

        return Response.ok(
            values=transformer.single_transform(user),
            message="Updated!"
        )
    elif request.method == 'DELETE':
        user = Users.objects.filter(id=id).first()
        if not user:
            return Response.bad_request(message='Pengguna tidak ditemukan')

        user.delete()
        return Response.ok(message='Deleted!')
    else:
        return Response.bad_request(message='Invalid Method!')