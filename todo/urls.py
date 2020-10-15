from django.urls import path
from . import views

urlpatterns = [
    path('/<int:user_id>', views.view_add_todo, name='view_add_todo'),
    path('/<int:user_id>/<int:task_id>', views.up_del_todo, name='up_del_todo'),
]