# Proyecto Django Backend - LiquiScan

Este proyecto es el backend desarrollado en Django para la aplicación LiquiScan.

## Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- virtualenv (entorno virtual para Python)

## Instalación y Configuración

1. Clonar el repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd BackEnd-Barchek
   ```

2. Crear y activar un entorno virtual:
   - En Windows:
     ```bash
     python -m venv env
     .\env\Scripts\activate
     ```
   - En macOS/Linux:
     ```bash
     python3 -m venv env
     source env/bin/activate
     ```

3. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Configurar la base de datos:
   - Por defecto, el proyecto usa SQLite.
   - Si usas otra base de datos, configura `DATABASES` en `LiquiScan/settings.py`.

5. Aplicar migraciones:
   ```bash
   python manage.py migrate
   ```

6. Crear un superusuario para acceder al admin de Django:
   ```bash
   python manage.py createsuperuser
   ```

7. Ejecutar el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

8. Acceder a la aplicación:
   - Backend API: `http://localhost:8000/api/`
   - Admin de Django: `http://localhost:8000/admin/`

## Notas

- El frontend se ejecuta por separado (por ejemplo, Expo React Native).
- Asegúrate de configurar CORS en `LiquiScan/settings.py` para permitir la comunicación entre frontend y backend.

## Dependencias Principales

- Django
- Django REST Framework
- django-cors-headers

## Contacto

Para cualquier duda o soporte, contacta con el equipo de desarrollo.
