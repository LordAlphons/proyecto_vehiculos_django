## 🚗 Proyecto Vehículos Django

Este es un proyecto desarrollado como entrega final del Módulo 6, utilizando el framework **Django**. La aplicación permite gestionar información de vehículos mediante una interfaz web, integrando funcionalidades CRUD y una base de datos relacional.

---

## 📦 Características principales

- Registro, edición y eliminación de vehículos
- Visualización de lista de vehículos
- Uso de base de datos SQLite
- Interfaz web con HTML y Django templates
- Estructura modular con apps separadas

---

## 🧰 Tecnologías utilizadas

| Tecnología | Descripción |
|------------|-------------|
| Django     | Framework web en Python para desarrollo rápido y seguro |
| SQLite     | Base de datos ligera y embebida |
| HTML       | Plantillas para la interfaz web |
| Python     | Lenguaje principal del backend |

---

## 🚀 Instalación y ejecución

- **Clona el repositorio**  
   ```bash
   git clone https://github.com/LordAlphons/proyecto_vehiculos_django.git
   cd proyecto_vehiculos_django

- Crea un entorno virtual (opcional pero recomendado)
   ```bash
   python -m venv env
   source env/bin/activate  # En Linux/macOS
   .\env\Scripts\activate    # En Windows
   ```
- Instala dependencias
   ```bash
   pip install -r requirements.txt
   ```
- Ejecuta migraciones
   ```bash
   python manage.py migrate
   ```
- Inicia el servidor
   ```bash
   python manage.py runserver
   ```

- Accede a la app
Abre tu navegador en http://127.0.0.1:8000

## 📁 Estructura del proyecto
   ```
   proyecto_vehiculos_django/
   ├── config/           # Configuración principal del proyecto Django
   ├── vehiculo/         # App que gestiona los vehículos
   ├── db.sqlite3        # Base de datos local
   ├── manage.py         # Script de administración de Django
   └── requirements.txt  # Dependencias del proyecto
   ```

## 🧪 Próximas mejoras
- Autenticación de usuarios
- Paginación y filtros en la lista de vehículos
- Integración con Bootstrap para mejorar la UI
- Exportación de datos en CSV o PDF

## 📜 Licencia
Este proyecto está bajo la licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente.

## ✍️ Autor
Alfonso Garrido
Profesional en transición hacia DevOps y Cloud, enfocado en automatización y excelencia técnica.
