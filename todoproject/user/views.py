from django.shortcuts import render
from todoproject.response import Response
from .models import Users
from . import transformer


# Create your views here.
def index(request):
    user = Users.objects.all()
    user = transformer.transform(user)
    return Response.ok(values=user)

def show(request, id):
    user = Users.objects.filter(id=id).first()

    if not user:
        return Response.bad_request(message='Pengguna tidak ditemukan!')

    user = transformer.single_transform(user)
    return Response.bad_request(values=user)