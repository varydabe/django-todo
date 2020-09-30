from django.urls import path
from . import views

urlpatterns = [
    path('<int:user_id>', views.view_todo, name='view_todo'),
    path('add', views.add_todo, name='add_todo'),
]