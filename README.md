# Explorando-el-universo
## 1. Descripción del Proyecto
"Explorando el Universo" es una plataforma de aprendizaje en línea diseñada para ofrecer cursos de astronomía a estudiantes de niveles básico y medio.  Este proyecto es de la asignatura Arquitectura 2024.
 Nuestro objetivo es fomentar la curiosidad y el interés por la astronomía a través de contenido interactivo, evaluaciones, foros de discusión y recursos multimedia. La plataforma está estructurada para facilitar el acceso a información relevante y proporcionar a los usuarios una experiencia de aprendizaje enriquecedora.
**agregar explicacion de que base de datos uso, de que componentes se deben descargar para acceder a mi app

## 2. Características
- Registro y autenticación de usuarios (estudiantes y profesores).
- Gestión de cursos incluyendo creación, edición<span style="color:red">(falta implementar)</span> y eliminación<span style="color:red">(falta implementar)</span>.
- Evaluaciones manuales y automáticas.<span style="color:red">(falta implementar)</span>
- Foros de discusión para interacción entre estudiantes y profesores.<span style="color:red">(falta implementar)</span>
- Visualización del progreso y certificaciones al finalizar cursos.<span style="color:red">(falta implementar)</span>

## 3. Tecnologías
- **Backend**: Django (Python)
- **Base de Datos**: PostgreSQL
- **Frontend**: HTML, CSS, JavaScript
- **Herramientas**: PlantUML (para diagramas), Git (control de versiones)

## 4. Requisitos
- Python 3.x
- PostgreSQL
- Dependencias del proyecto: 
  - Django
  - psycopg2
  - crispy-bootstrap5
  - pillow

## 5. Instalación
1. Clona el repositorio:
   ```bash
   git clone https://github.com/raquel1313/Explorando-el-universo
   cd explorando_el_universo
2. Crea y activa un entorno virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate   # Para Windows: venv\Scripts\activate
3. Instala las dependencias:

    ```bash
    pip install django psycopg2
4. Configura la base de datos:

    - Abre `settings.py` y ajusta la configuración de la base de datos para utilizar PostgreSQL.

5. Ejecuta las migraciones:

    ```bash
    python manage.py migrate
6. Inicia el servidor de desarrollo:

    ```bash
    python manage.py runserver
7. Accede a la aplicación:

    - Abre tu navegador web y dirígete a http://127.0.0.1:8000/ para ver la plataforma en funcionamiento


## 6. Uso

- **Acceso a la plataforma**: 
  - Una vez que el servidor de desarrollo esté en funcionamiento, abre tu navegador y ve a `http://127.0.0.1:8000/`. Aquí podrás acceder a la página de inicio de la plataforma.

- **Registro de Usuarios**:
  - Los nuevos usuarios (estudiantes y profesores) pueden registrarse haciendo clic en el enlace de registro en la página de inicio. Completa el formulario con la información solicitada y presiona "Registrarse".

- **Inicio de Sesión**:
  - Si ya tienes una cuenta, puedes iniciar sesión ingresando tu correo y contraseña. Después de iniciar sesión, serás redirigido a tu panel principal.

- **Gestión de Cursos**:<span style="color:red">(falta implementar)</span>
  - Los administradores tienen acceso a la sección de gestión de cursos, donde pueden agregar, editar o eliminar cursos. Los profesores pueden acceder a sus cursos y actualizar el contenido según sea necesario.

- **Interacción en Cursos**:
  - Los estudiantes pueden inscribirse en los cursos disponibles, participar en evaluaciones y revisar su progreso a través de su panel.
  - La plataforma incluye foros de discusión donde estudiantes y profesores pueden interactuar, hacer preguntas y dejar comentarios.<span style="color:red">(falta implementar)</span>

- **Recuperación de Contraseña**:
  - Si olvidaste tu contraseña, puedes solicitar una recuperación a través de la opción "¿Olvidaste tu contraseña?" en la página de inicio de sesión. Recibirás un correo con instrucciones para restablecerla.<span style="color:red">(falta implementar)</span>


## 7. Contacto
- Autor: Raquel Rehbein 
- Email: raquelpfrb@gmail.com
- Github: https://github.com/raquel1313

## 8. Agradecimientos


Quiero expresar mi agradecimiento a todas las personas que han contribuido al desarrollo de la plataforma "Explorando el Universo". En particular, queremos reconocer:

- **Profe Gio**: Por su orientación y apoyo durante el desarrollo del proyecto, brindando valiosas recomendaciones sobre la arquitectura y la implementación.
  
- **Compañeros de clases**: Por su compañerismo, ayuda y retroalimentación de mi plataforma.

- **Herramientas y Recursos**: Agradecimiento especial a herramientas como Django, PostgreSQL y PlantUML, que han sido fundamentales para llevar a cabo este proyecto.

- **Los videitos de youtube**: Agradezco a las plataformas de educación en línea y a todos los materiales de aprendizaje que nos ayudaron a adquirir conocimientos valiosos sobre programación y desarrollo web.

- **Mi mamita**: Agradezco a la sra Ester por aguantarme, alimentarme y despertarme en las mañanas <3.

Gracias a todos por su apoyo en este viaje educativo. Su contribución ha sido esencial para el éxito de este proyecto.
