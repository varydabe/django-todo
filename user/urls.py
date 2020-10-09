from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.show, name='show'),
    path('auth', views.auth, name='auth'),
    # path('login', views.login, name='login'),
]