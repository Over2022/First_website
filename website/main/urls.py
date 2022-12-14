from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name='about'),
    path('create/', views.create, name='create'),
    path('draft/', views.draft, name='draft'),
    path('registration/', views.registration, name='registration'),
]