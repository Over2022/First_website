from .models import Task, Main
from django.forms import ModelForm


class TaskForm(ModelForm):
    class Meta:
        model = Task #указываю с какой моделью работаю
        fields = ['title', 'task']


class MainForm(ModelForm):
    class Meta:
        model = Main
        fields = ['title', 'main', 'img']
