from django import forms
from .models import Task, Main
from django.forms import ModelForm, TextInput


class TaskForm(ModelForm):
    class Meta:
        model = Task  # указываю с какой моделью работаю
        fields = ['title', 'task']
        widgets = {'title': TextInput(attrs={'class': "form-control", "placeholder": "Введите название"}),
                   'task': TextInput(attrs={'class': "form-control", "placeholder": "Введите описание"})}


class MainForm(ModelForm):
    class Meta:
        model = Main
        fields = ['title', 'main', 'img']
        widgets = {'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'}),
                   'main': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите сообщение'})}


class DraftForm(forms.Form):
    title = forms.CharField(max_length=20,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'}))

    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите сообщение'}))
