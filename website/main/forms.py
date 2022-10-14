from django import forms
from .models import Task, Main, Registration
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task  # указываю с какой моделью работаю
        fields = ['title', 'task']
        widgets = {'title': TextInput(attrs={'class': "form-control", "placeholder": "Введите название"}),
                   'task': Textarea(attrs={'class': "form-control", "placeholder": "Введите описание"})}


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


class RegistrationForm(ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'surname', 'mail', 'password', 'password_2']
        widgets = {'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя', 'style': 'width:200px'}),
                   'surname': TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия','style': 'width:200px'}),
                   'mail': TextInput(attrs={'class': 'form-control', 'placeholder': 'E-mail', 'style': 'width:400px'}),
                   'password': TextInput(attrs={'class': 'form-control', 'placeholder': '••••••••', 'style': 'width:400px'}),
                   'password_2': TextInput(attrs={'class': 'form-control', 'placeholder': '••••••••', 'style': 'width:400px'})}

