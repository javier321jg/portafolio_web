# Portafolio Web - Nelson Javier Gutierrez Ramos

Portafolio web de alto impacto visual para Ingeniero de Sistemas Empresariales, desarrollado con Django y SQLite.

## 🎨 Características

- **Diseño Premium**: Estética moderna tipo Alche, Inc. con dark mode
- **Efectos Avanzados**: Glassmorphism, animaciones GSAP, fondo interactivo Three.js
- **Responsive**: Diseño adaptable a todos los dispositivos
- **Panel de Administración**: Sistema completo de gestión de contenido
- **Categorización**: Proyectos organizados por áreas (Datos, Gestión, Desarrollo, Infraestructura)
- **Galería de Imágenes**: Sistema de galería por proyecto
- **Formulario de Contacto**: Formulario moderno con validación

## 🚀 Tecnologías

- **Backend**: Django 4.2
- **Base de Datos**: SQLite
- **Frontend**: HTML + TailwindCSS (CDN)
- **Animaciones**: GSAP (GreenSock Animation Platform)
- **3D Graphics**: Three.js
- **Imágenes**: Pillow

## 📋 Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## 🔧 Instalación

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd portafolio_web
```

### 2. Crear entorno virtual

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Crear migraciones

```bash
python manage.py makemigrations portfolio
```

### 5. Aplicar migraciones

```bash
python manage.py migrate
```

### 6. Crear superusuario

```bash
python manage.py createsuperuser
```

Sigue las instrucciones en pantalla para crear tu usuario administrador.

### 7. Ejecutar el servidor de desarrollo

```bash
python manage.py runserver
```

El sitio estará disponible en: `http://127.0.0.1:8000/`

## 🎯 Acceso al Panel de Administración

1. Navega a: `http://127.0.0.1:8000/admin/`
2. Inicia sesión con las credenciales del superusuario
3. Desde aquí podrás:
   - Crear y gestionar proyectos
   - Agregar imágenes a la galería de cada proyecto
   - Gestionar habilidades técnicas
   - Marcar proyectos como destacados

## 📁 Estructura del Proyecto

```
portafolio_web/
│
├── mi_portafolio/          # Configuración del proyecto Django
│   ├── settings.py         # Configuración principal
│   ├── urls.py             # URLs del proyecto
│   └── wsgi.py
│
├── portfolio/              # Aplicación principal
│   ├── models.py           # Modelos: Project, ProjectImage, Skill
│   ├── views.py            # Vistas de la aplicación
│   ├── admin.py            # Configuración del admin
│   ├── forms.py            # Formulario de contacto
│   └── urls.py             # URLs de la app
│
├── templates/              # Plantillas HTML
│   └── portfolio/
│       ├── base.html       # Template base
│       ├── home.html       # Página principal
│       ├── project_list.html
│       ├── project_detail.html
│       ├── about.html
│       └── contact.html
│
├── media/                  # Archivos subidos (se crea automáticamente)
│   └── projects/
│       ├── covers/         # Imágenes de portada
│       └── gallery/        # Galería de proyectos
│
├── static/                 # Archivos estáticos (CSS, JS personalizados)
├── db.sqlite3              # Base de datos (se crea con migrate)
├── manage.py               # Script de gestión de Django
└── requirements.txt        # Dependencias del proyecto
```

## 🎨 Modelos de Datos

### Project (Proyecto)
- **title**: Título del proyecto
- **slug**: URL amigable (se genera automáticamente)
- **short_description**: Descripción corta
- **description**: Descripción completa
- **technologies**: Tecnologías utilizadas
- **category**: Categoría del proyecto
- **github_url**: URL del repositorio (opcional)
- **live_url**: URL del sitio en vivo (opcional)
- **cover_image**: Imagen de portada
- **is_featured**: Marcar como destacado
- **order**: Orden manual

### ProjectImage (Imagen de Proyecto)
- **project**: Proyecto relacionado
- **image**: Archivo de imagen
- **caption**: Descripción de la imagen
- **order**: Orden en la galería

### Skill (Habilidad)
- **name**: Nombre de la habilidad
- **icon_svg**: Código SVG del ícono (opcional)
- **category**: Categoría de la habilidad

## 📝 Uso del Sistema

### Agregar un Proyecto

1. Accede al panel de administración
2. Ve a "Proyectos" → "Agregar proyecto"
3. Completa los campos:
   - Título y descripción
   - Selecciona una categoría
   - Sube una imagen de portada
   - Añade enlaces (GitHub, sitio en vivo)
   - Marca como "destacado" si quieres que aparezca en la página principal
4. Opcionalmente, agrega imágenes a la galería usando el inline
5. Guarda el proyecto

### Agregar Habilidades

1. Ve a "Habilidades" → "Agregar habilidad"
2. Ingresa el nombre y categoría
3. Opcionalmente, pega código SVG para un ícono personalizado
4. Guarda

### Configurar Email

En `mi_portafolio/settings.py`, el backend de email está configurado para imprimir en consola (desarrollo):

```python
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
```

Para producción, configura un backend SMTP real.

## 🎬 Características Visuales

### Hero Section
- Fondo animado con partículas en Three.js
- Interactivo al movimiento del mouse
- Animaciones de entrada con GSAP

### Glassmorphism
- Efecto de vidrio esmerilado en contenedores
- Bordes que se iluminan al hacer hover

### Animaciones de Scroll
- Elementos que aparecen gradualmente al hacer scroll
- Transiciones suaves entre secciones

### Navbar Dinámico
- Transparente al inicio
- Se vuelve sólido al hacer scroll

## 🌐 URLs Disponibles

- `/` - Página principal (home)
- `/proyectos/` - Lista de todos los proyectos
- `/proyectos/<slug>/` - Detalle de un proyecto
- `/sobre-mi/` - Página "Acerca de mí"
- `/contacto/` - Formulario de contacto
- `/admin/` - Panel de administración

## 🔐 Seguridad

⚠️ **IMPORTANTE para producción:**

1. Cambia `SECRET_KEY` en `settings.py`
2. Establece `DEBUG = False`
3. Configura `ALLOWED_HOSTS`
4. Usa un servidor de producción (Gunicorn, uWSGI)
5. Configura HTTPS
6. Usa un servidor de archivos estáticos (WhiteNoise, CDN)

## 🤝 Contribuir

Si deseas contribuir o reportar un problema, por favor abre un issue o pull request.

## 📄 Licencia

Este proyecto es de uso personal para el portafolio de Nelson Javier Gutierrez Ramos.

## 👨‍💻 Autor

**Nelson Javier Gutierrez Ramos**
- Ingeniero de Sistemas Empresariales
- Universidad Científica del Sur (UCSUR)
- LinkedIn: [nelson-javier-gutierrez-ramos](https://www.linkedin.com/in/nelson-javier-gutierrez-ramos-6a5b60215)
- GitHub: [@javier321jg](https://github.com/javier321jg)

---

¡Gracias por visitar mi portafolio! 🚀
