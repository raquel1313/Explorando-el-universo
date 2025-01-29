#views.html
from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth import authenticate, login  
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm


class HomeView(TemplateView):
    template_name = 'home.html'
    
class RegistroView(TemplateView):
    template_name = 'registro.html'
    
class ProgresoView(TemplateView):
    template_name = 'progreso.html'
    
class PerfilView(LoginRequiredMixin, TemplateView):
    template_name = 'registration/profile.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        form.fields['username'].widget.attrs.update({'class': 'form-control'})
        form.fields['password'].widget.attrs.update({'class': 'form-control'})
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("profile")
    else:
        form = AuthenticationForm()
        form.fields['username'].widget.attrs.update({'class': 'form-control'})
        form.fields['password'].widget.attrs.update({'class': 'form-control'})
    return render(request, "registration/login.html", {"form": form})



def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige a la página de inicio de sesión después del registro
    else:
        form = RegistroForm()
    return render(request, 'registration/registro.html', {'form': form})

@login_required  # Asegúrate de que solo los usuarios autenticados puedan acceder
def crear_curso(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        
        # Aquí usamos request.user para guardar el ID del usuario conectado como profesor
        curso = Curso.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            profesor=request.user  # Almacena el usuario conectado en el campo profesor
        )

        return redirect('adm_curso')  # Redirige a la lista de cursos

    return render(request, 'cursos/crear_cursos.html', {})

@login_required
def eliminar_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)

    if request.method == 'POST':  
        curso.delete()
        return redirect('adm_curso')  

    return render(request, 'cursos/confirmar_eliminar_curso.html', {'curso': curso}) 



def lista_cursos(request):
    cursos = Curso.objects.all()  # Obtiene todos los cursos
    return render(request, 'cursos.html', {'cursos': cursos})

@login_required
def cursos_inscritos(request):
    inscripciones = Inscripcion.objects.filter(usuario=request.user)
    cursos = [inscripcion.curso for inscripcion in inscripciones]
    
    context = {
        'cursos': cursos,
    }
    
    return render(request, 'cursos/cursos_inscritos.html', context)

def contenido_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    contenido = Contenido.objects.filter(curso=curso)

    # Modificar la URL del video para que sea compatible con iframe
    for item in contenido:
        if 'youtube.com/watch?v=' in item.video_url:
            video_id = item.video_url.split('v=')[1]
            ampersand_position = video_id.find('&')
            if ampersand_position != -1:
                video_id = video_id[:ampersand_position]
            item.video_url = f"https://www.youtube.com/embed/{video_id}"  # Cambia la URL para el iframe

    context = {
        'curso': curso,
        'contenido': contenido,
    }
    return render(request, 'cursos/contenido_curso.html', context)

@login_required
def inscribir_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    
    # Verifica si el usuario ya está inscrito en el curso
    if Inscripcion.objects.filter(usuario=request.user, curso=curso).exists():
        # Aquí podrías redirigir o mostrar un mensaje
        return redirect('cursos')  # Cambia 'cursos' a la URL donde quieras redirigir

    # Crea una nueva inscripción
    Inscripcion.objects.create(usuario=request.user, curso=curso)
    return redirect('cursos_inscritos')  # Cambia 'cursos' a la URL donde quieras redirigir

@login_required
def eliminar_inscripcion(request, curso_id):
    inscripcion = get_object_or_404(Inscripcion, usuario=request.user, curso_id=curso_id)
    inscripcion.delete()
    return redirect('cursos_inscritos')  

@login_required
def adm_curso(request):
    cursos = Curso.objects.filter(profesor=request.user)
    context = {
        'cursos': cursos
    }
    return render(request, 'cursos/adm_curso.html', context)

@login_required
def agregar_contenido(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)

    if request.method == 'POST':
        form = ContenidoForm(request.POST)
        if form.is_valid():
            contenido = form.save(commit=False)
            contenido.curso = curso  # Asocia el contenido con el curso
            contenido.save()
            return redirect('contenido_curso', curso_id=curso.id)  # Redirigir a la página de contenido
    else:
        form = ContenidoForm()

    return render(request, 'agregar_contenido.html', {'form': form, 'curso': curso})

@login_required
def agregar_contenido(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)

    if request.method == 'POST':
        form = ContenidoForm(request.POST)
        if form.is_valid():
            contenido = form.save(commit=False)
            contenido.curso = curso  # Asociar el contenido con el curso
            contenido.save()
            return redirect('contenido_curso', curso_id=curso.id)  # Redirigir a la página de contenido
    else:
        form = ContenidoForm()

    return render(request, 'cursos/agregar_contenido.html', {'form': form, 'curso': curso})