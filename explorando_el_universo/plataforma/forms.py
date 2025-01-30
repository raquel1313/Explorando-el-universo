# forms.py
from django import forms
from .models import Usuario, Contenido, Comentario

class RegistroForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput,
    )

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'role']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user



class ContenidoForm(forms.ModelForm):
    class Meta:
        model = Contenido
        fields = ['video_url', 'informacion']  # Campos que deseas mostrar en el formulario
        widgets = {
            'video_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la URL del video'}),
            'informacion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese la información del contenido'}),
        }
        
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']  # Aquí incluyes solo el campo de contenido
        widgets = {
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe tu comentario aquí...', 'rows': 3}),
        }