from django.forms import ModelForm
from .models import Task

class TaskForm(ModelForm):
    class Nota:
        model = Task
        fields = {'title', 'description', 'important'}
        
