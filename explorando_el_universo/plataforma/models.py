from django.db import models

class Usuario(models.Model):
    ROLE_CHOICES = (
        ('profesor', 'Profesor'),
        ('alumno', 'Alumno'),
        ('admin', 'Admin'),
    )
    
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)  
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username


class Curso(models.Model):
    id = models.AutoField(primary_key=True) 
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    profesor = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'role': 'profesor'})

    def __str__(self):
        return self.nombre


class Contenido(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    video_url = models.CharField(max_length=255)
    informacion = models.TextField()
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Contenido de {self.curso.nombre}'


class Evaluacion(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    preguntas = models.TextField()  # Puedes considerar usar JSONField para preguntas

    def __str__(self):
        return f'Evaluación de {self.curso.nombre}'


class Inscripcion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.usuario.username} inscrito en {self.curso.nombre}'


class Comentario(models.Model):
    contenido = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    contenido_asociado = models.ForeignKey(Contenido, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario de {self.usuario.username} en {self.contenido_asociado}'
