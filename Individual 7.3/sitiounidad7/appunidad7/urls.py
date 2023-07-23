from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.register, name='signup'),
    path('task/', views.task, name='task'),
    path('task/create/', views.task_create, name='task_create'),
    path('task/completed/', views.task_completed, name='task_completed'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('task/<int:task_id>/complete/', views.complete_task, name='complete_task'),
    path('task/<int:task_id>/delete/', views.delete_task, name='delete_task'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
]
