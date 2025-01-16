# plataforma/urls.py
from django.urls import path
from .views import index 

urlpatterns = [
    path('', index, name='index'),  # Ruta para la página de inicio
    # Puedes agregar más rutas aquí para otras vistas (e.g., registro, inicio de sesión)
]
