from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.register, name='signup'),
    path('task/', views.task, name='task'),
    path('task/create', views.task_create, name='task_create'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
]
