from .models import Task
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        filds = ["title", "task"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
                }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder':'Введите описание'
                }),
        }