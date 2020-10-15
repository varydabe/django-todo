from django.contrib.auth.hashers import make_password, check_password
import json
from django.shortcuts import render
from todoproject.jwt import JWTAuth
from todoproject.response import Response
from todoproject.middleware import jwt_required
from .models import Users
from . import transformer


# Create your views here.

def register(request):
    # Add user (Register)
    if request.method == 'POST':
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

    else:
        return Response.bad_request(message='Invalid Method!')


def login(request):
    # User login
    if request.method == 'POST':
        json_data = json.loads(request.body) #request.POST
        email = json_data['email']

        user = Users.objects.filter(email=email).first()

        if not user:
            return Response.bad_request(message='User not found!')

        if not check_password(json_data['password'], user.password):
            return Response.bad_request('Invalid email or password!')

        user = transformer.single_transform(user)

        jwt = JWTAuth()
        user['token'] = jwt.encode({"id": user['id']})
        return Response.ok(values=user, message='Login success!')

    else:
        return Response.bad_request(message='Invalid Method!')


@jwt_required
def index(request):
    # Show all user
    if request.method == 'GET':
        user = Users.objects.all()
        user = transformer.transform(user)
        return Response.ok(values=user)

    else:
        return Response.bad_request(message='Invalid Method!')


@jwt_required
def show(request, id):
    # Read user
    if request.method == 'GET':
        user = Users.objects.filter(id=id).first()

        if not user:
            return Response.bad_request(message='User not found!')

        user = transformer.single_transform(user)
        return Response.ok(values=user)

    # Update user
    elif request.method == 'PUT':
        json_data = json.loads(request.body)
        user = Users.objects.filter(id=id).first()

        if not user:
            return Response.bad_request(message='User not found!')

        user.name = json_data['name']
        user.email = json_data['email']
        user.password = make_password(password=json_data['password'])
        user.save()

        return Response.ok(
            values=transformer.single_transform(user),
            message="Updated!"
        )

    # Delete user
    elif request.method == 'DELETE':
        user = Users.objects.filter(id=id).first()
        if not user:
            return Response.bad_request(message='User not found!')

        user.delete()
        return Response.ok(message='Deleted!')
    else:
        return Response.bad_request(message='Invalid Method!')