from django.shortcuts import render, redirect  # Asegúrate de importar redirect
from django.contrib.auth import authenticate, login  # Asegúrate de importar authenticate y login
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(TemplateView):
    template_name = 'home.html'
    
class CursosView(TemplateView):
    template_name = 'cursos.html'
    
class ProgresoView(TemplateView):
    template_name = 'progreso.html'
    
class PerfilView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
    
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirige a la página de inicio (definido en urls.py)
        else:
            return render(request, 'login.html', {'error': 'Credenciales incorrectas.'})
    
    return render(request, 'login.html')
