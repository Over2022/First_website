from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h4>Hello<h4>')


def detail(request):
    return HttpResponse('<BLOCKQUOTE>My first project<BLOCKQUOTE>'
                        '<p>My first project<p>')