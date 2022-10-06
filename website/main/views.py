from django.shortcuts import render
from django.http import HttpResponse
from .models import Task, Main


def index(request):
    tasks = Task.objects.all()
    mains = Main.objects.all()
    context = {'title': 'Главная страница', 'tasks': tasks, 'mains': mains}
    return render(request, 'main/index.html', context)


def about(request):
    return render(request, 'main/about.html')


def draft(request):
    return render(request, 'draft.html')
