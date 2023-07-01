from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields= [ 'title','description', 'created', 'important' ]
        #fields = '__all__' para llamar todos los campos