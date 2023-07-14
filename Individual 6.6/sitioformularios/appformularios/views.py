from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


# Create your views here.
def usuarios(request):
    users = User.objects.all()
    context = {
        'usuarios':users,

    }
    return render(request, 'usuarios.html',context=context)

def home(request):
    return render(request, 'index.html')


def register(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('noticias')
            except IntegrityError:
                return render(request, 'signup.html', {'form': UserCreationForm, "error": 'Username already exists'})
        return render(request, 'signup.html', {'form': UserCreationForm, "error": 'Password not match'})

@login_required
def noticias(request):
    return render(request, 'noticias.html')

def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
        'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect '
                })
        else:
            login(request, user)
            return redirect('noticias')

def tu_vista(request):
    es_staff = request.user.groups.filter(name='Staff').exists()
    return render(request, 'base_layout.html', {'es_staff': es_staff})
   
def adminfront(request):
    if request.method == 'POST':
        if 'create_user' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            group_id = request.POST['group']

            user = User.objects.create_user(username=username, password=password)
            group = Group.objects.get(id=group_id)
            user.groups.add(group)

        elif 'update_user' in request.POST:
            user_id = request.POST['user_id']
            username = request.POST['username']
            password = request.POST['password']
            group_id = request.POST['group']

            user = User.objects.get(id=user_id)
            user.username = username
            if password:
                user.set_password(password)
            user.groups.clear()
            group = Group.objects.get(id=group_id)
            user.groups.add(group)
            user.save()

        elif 'delete_user' in request.POST:
            user_id = request.POST['user_id']
            user = User.objects.get(id=user_id)
            user.delete()

        elif 'create_group' in request.POST:
            name = request.POST['group_name']
            group = Group.objects.create(name=name)

        elif 'update_group' in request.POST:
            group_id = request.POST['group_id']
            name = request.POST['group_name']

            group = Group.objects.get(id=group_id)
            group.name = name
            group.save()

        elif 'delete_group' in request.POST:
            group_id = request.POST['group_id']
            group = Group.objects.get(id=group_id)
            group.delete()

        elif 'create_permission' in request.POST:
            name = request.POST['permission_name']
            
           
            
        elif 'update_permission' in request.POST:
            permission_id = request.POST['permission_id']
            name = request.POST['permission_name']
            content_type_id = request.POST['content_type']
            

            permission = Permission.objects.get(id=permission_id)
            permission.name = name
            permission.content_type = ContentType.objects.get(id=content_type_id)
            
            permission.save()

        elif 'delete_permission' in request.POST:
            permission_id = request.POST['permission_id']
            permission = Permission.objects.get(id=permission_id)
            permission.delete()

        return redirect('adminfront')

    users = User.objects.all()
    groups = Group.objects.all()
    permissions = Permission.objects.all()
    content_types = ContentType.objects.all()

    return render(request, 'adminfront.html', {
        'users': users,
        'groups': groups,
        'permissions': permissions,
        
    })
