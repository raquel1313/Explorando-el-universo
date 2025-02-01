from django.contrib import admin
from .models import Usuario, Curso, Contenido, Evaluacion, Inscripcion, Comentario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'role')  # Campos que se mostrarán en la lista
    search_fields = ('username',)         # Campo de búsqueda

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'profesor')  # Campos en la lista
    search_fields = ('nombre', 'descripcion')              # Campo de búsqueda
    list_filter = ('profesor',)                            # Filtros laterales

class ContenidoAdmin(admin.ModelAdmin):
    list_display = ('curso', 'video_url', 'fecha_subida')  # Campos en la lista
    search_fields = ('video_url',)                          # Campo de búsqueda

class EvaluacionAdmin(admin.ModelAdmin):
    list_display = ('curso',)                              # Campos en la lista
    search_fields = ('curso__nombre',)                     # Campo de búsqueda por nombre del curso

class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'curso')                    # Campos en la lista
    search_fields = ('usuario__username', 'curso__nombre') # Campo de búsqueda por usuario y curso

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'contenido_asociado', 'fecha')  # Campos en la lista
    search_fields = ('contenido',)                             # Campo de búsqueda

# Registro de modelos en el panel de administración
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Contenido, ContenidoAdmin)
admin.site.register(Evaluacion, EvaluacionAdmin)
admin.site.register(Inscripcion, InscripcionAdmin)
admin.site.register(Comentario, ComentarioAdmin)
