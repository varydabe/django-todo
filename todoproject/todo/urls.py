from django.urls import path
from . import views

urlpatterns = [
    path('<int:user_id>', views.view_todo, name='view_todo'),
    path('<int:user_id>/add', views.add_todo, name='add_todo'),
    path('<int:user_id>/edit/<int:task_id>', views.up_del_todo, name='up_del_todo'),
]