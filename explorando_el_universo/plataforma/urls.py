#plataforma/urls.py
from django.urls import path
from .views import *


urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('cursos/', lista_cursos, name='cursos'),
    path('progreso/',ProgresoView.as_view(), name='progreso'),
    path('accounts/profile/',PerfilView.as_view(), name='profile'),
    path('login/',login, name='login'),
    path('registro/', registro, name='registro'),
    path('crear-curso/', crear_curso, name='crear_curso'),
    path('cursos-inscritos/', cursos_inscritos, name='cursos_inscritos'),
    path('curso/<int:curso_id>/', contenido_curso, name='contenido_curso'),
    path('inscribir-curso/<int:curso_id>/', inscribir_curso, name='inscribir_curso'),
    path('eliminar-inscripcion/<int:curso_id>/', eliminar_inscripcion, name='eliminar_inscripcion'),
    path('adm-cursos/', adm_curso, name='adm_curso'),
    path('agregar-contenido/<int:curso_id>/', agregar_contenido, name='agregar_contenido'),
    path('eliminar-curso/<int:curso_id>/', eliminar_curso, name='eliminar_curso'),
    
]