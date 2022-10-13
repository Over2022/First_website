from django.shortcuts import render
from django.http import HttpResponse
from .models import Task, Main
from .forms import TaskForm
from .forms import MainForm
from .forms import DraftForm


def index(request):
    # tasks = Task.objects.order_by('tasks')
    tasks = Task.objects.all()
    mains = Main.objects.all()
    context = {'title': 'Главная страница', 'tasks': tasks, 'mains': mains}
    return render(request, 'main/index.html', context)


def about(request):
    return render(request, 'main/about.html')


def create(request):
    form = TaskForm()
    context = {'form': form}
    return render(request, 'main/create.html', context)


def draft(request):
    form = MainForm()
    form_2 = DraftForm()
    context = {'form': form, 'form_2': form_2}
    return render(request, 'draft.html', context)