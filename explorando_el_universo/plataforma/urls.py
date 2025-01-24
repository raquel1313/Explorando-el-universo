#plataforma/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('cursos/',CursosView.as_view(), name='cursos'),
    path('progreso/',ProgresoView.as_view(), name='progreso'),
    path('profile/',PerfilView.as_view(), name='profile'),
    path('login/',login, name='login'),
    path('registro/', registro, name='registro'),
    path('crear-curso/', crear_curso, name='crear_curso'),
]