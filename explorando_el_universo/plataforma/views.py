#views.html
from django.shortcuts import render, redirect  
from django.contrib.auth import authenticate, login  
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import RegistroForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm


class HomeView(TemplateView):
    template_name = 'home.html'
    
class RegistroView(TemplateView):
    template_name = 'registro.html'
    
class CursosView(TemplateView):
    template_name = 'cursos.html'
    
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
        form =AuthenticationForm(data=request.POST)
        if form.is_valid():
            
            return redirect("profile")
    else:
        form = AuthenticationForm()
    return render(request, "registration/login.html", {"form" : form})



def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige a la página de inicio de sesión después del registro
    else:
        form = RegistroForm()
    return render(request, 'registration/registro.html', {'form': form})

def crear_curso(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        curso = Curso.objects.create(nombre=nombre, descripcion=descripcion)
        profesor= request.POST['profesor']
        return redirect('cursos')
    return render(request, 'cursos/crear_cursos.html', {})

def lista_cursos(request):
    cursos = Curso.objects.all()  # Obtiene todos los cursos
    return render(request, 'cursos.html', {'cursos': cursos})