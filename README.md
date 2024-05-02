# Sistema de Gestión Académica con Django

Bienvenido al Sistema de Gestión Académica con Django.
Este proyecto, desarrollado con Django, facilita la gestión de
estudiantes, profesores, cursos y módulos.

## Funcionalidades Principales

- **Registro de Usuarios**: Permite a los nuevos usuarios registrarse proporcionando su correo electrónico y contraseña.
- **Autenticación de Usuarios**: Los usuarios pueden iniciar y cerrar sesión de manera segura.
- **Administración de Estudiantes**: Los administradores pueden gestionar los perfiles de los estudiantes, incluyendo la
  creación, actualización y eliminación de registros. Cada estudiante está asociado con varios cursos y módulos.
- **Administración de Profesores**: Los administradores pueden gestionar los perfiles de los profesores, incluyendo la
  creación, actualización y eliminación de registros. Cada profesor está asociado con varios cursos y módulos. Además,
  los profesores pueden ser designados como tutores.
- **Administración de Cursos**: Los administradores pueden crear, actualizar y eliminar cursos. Cada curso tiene un
  nombre y descripción.
- **Administración de Módulos**: Los administradores pueden crear, actualizar y eliminar módulos. Cada módulo tiene un
  nombre, descripción, duración, y está asociado con un curso.

## Tecnologías Implementadas

- **Python**: El núcleo de la aplicación está desarrollado en Python.
- **Django**: Utilizamos Django, un framework web de alto nivel en Python, para un desarrollo rápido y un diseño limpio
  y pragmático.
- **JavaScript**: Implementado para proporcionar funcionalidades dinámicas en el frontend.
- **HTML/CSS**: Utilizado para estructurar y estilizar las páginas web.
- **Tailwind CSS**: Un framework CSS de utilidad primero que se utiliza para estilizar la aplicación.

## Guía de Instalación y Configuración

1. Clona el repositorio en tu máquina local.
2. Instala las dependencias requeridas usando pip: `pip install -r requirements.txt`
3. Ejecuta las migraciones: `python manage.py migrate`
4. Inicia el servidor de desarrollo: `python manage.py runserver`
5. Abre tu navegador web y navega a `http://localhost:8000/`

## Cómo Utilizar el Sistema

Una vez que los usuarios inician sesión, pueden acceder a su perfil, que incluye su nombre, correo electrónico, y los
cursos y módulos con los que están asociados. Los usuarios con privilegios de administrador tienen la capacidad de
crear, actualizar y eliminar registros de estudiantes, profesores, cursos y módulos.