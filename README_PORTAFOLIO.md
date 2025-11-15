# Portafolio Web Inmersivo - Nelson Javier Gutierrez Ramos

Portafolio web de alto impacto visual para **Nelson Javier Gutierrez Ramos**, Ingeniero de Sistemas Empresariales. Construido con Django y SQLite, con un diseño moderno, tech e inmersivo inspirado en agencias digitales premium.

## 🎨 Características Principales

### Diseño y Estética
- **Modo Oscuro Predominante**: Paleta de colores moderna (#0a0a0f, #1a1a2e)
- **Acentos Vibrantes**: Azul eléctrico (#00d4ff) y verde neón (#00ff88)
- **Glassmorphism**: Efectos de vidrio translúcido con blur en contenedores
- **Animaciones Avanzadas**: Transiciones 3D, scroll-triggered con GSAP, parallax suave
- **Gráficos 3D**: Hero interactivo con partículas flotantes usando Three.js
- **Responsive Design**: Totalmente adaptado a dispositivos móviles

### Funcionalidades de Contenido
- 📁 **Gestión de Proyectos**: Categorización, filtrado y paginación
- 🖼️ **Galería Multimedia**: Soporte para imágenes y videos de demostración
- 🏆 **Sistema de Logros**: Certificaciones, premios y reconocimientos
- 💼 **Base de Datos de Habilidades**: Organización por categoría con niveles de profundidad
- 🎯 **Gestión de Logos**: Tecnologías, empresas, clientes y partners
- 📊 **Analytics Básico**: Contador de vistas por proyecto
- 📧 **Formulario de Contacto**: Con validación y notificaciones

### Panel de Administración
- Panel completo y personalizado en Django
- Inlines para agregar imágenes a proyectos
- Fieldsets organizados por secciones
- Búsqueda y filtrado avanzados
- Ordenamiento personalizable de contenidos

## 🛠️ Tecnologías y Stack

### Backend
- **Django 5.2+**: Framework web Python
- **SQLite**: Base de datos ligera
- **Pillow**: Procesamiento y optimización de imágenes
- **python-dotenv**: Gestión de variables de entorno
- **Gunicorn**: Servidor WSGI para producción
- **WhiteNoise**: Servicio de archivos estáticos optimizado

### Frontend
- **HTML5 Semántico**: Markup accesible
- **TailwindCSS 3**: Framework de utilidades CSS via CDN
- **GSAP 3 + ScrollTrigger**: Animaciones avanzadas y scroll-triggered
- **Three.js r160**: Gráficos 3D y WebGL
- **Swiper 11**: Carruseles responsivos e intuitivos

## 📦 Instalación y Configuración

### 1. Clonar el Repositorio
```bash
git clone <repository-url>
cd portafolio_web
```

### 2. Crear Entorno Virtual
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 4. Crear Estructura de Carpetas de Media
```bash
mkdir -p media/projects/{covers,gallery,thumbnails,videos}
mkdir -p media/skills/icons
mkdir -p media/achievements/{certificates,badges}
mkdir -p media/logos
```

### 5. Ejecutar Migraciones
```bash
python manage.py migrate
```

### 6. Crear Superusuario
```bash
python manage.py createsuperuser
```

### 7. Ejecutar Servidor de Desarrollo
```bash
python manage.py runserver
```

Acceso:
- **Sitio web**: http://127.0.0.1:8000/
- **Panel admin**: http://127.0.0.1:8000/admin/
- **Proyectos**: http://127.0.0.1:8000/proyectos/
- **Sobre mí**: http://127.0.0.1:8000/sobre-mi/
- **Contacto**: http://127.0.0.1:8000/contacto/

## 📝 Estructura del Proyecto

```
portafolio_web/
├── mi_portafolio/          # Configuración de Django
│   ├── settings.py         # Configuración global
│   ├── urls.py            # Rutas principales
│   ├── wsgi.py            # Configuración WSGI
│   └── asgi.py            # Configuración ASGI
├── portfolio/             # App principal
│   ├── models.py          # Modelos: Project, ProjectImage, Skill, Achievement, Logo
│   ├── views.py           # Vistas del portafolio
│   ├── admin.py           # Configuración del panel admin
│   ├── forms.py           # Formularios (ContactForm)
│   ├── urls.py            # Rutas de portfolio
│   ├── utils.py           # Utilidades (optimización de imágenes)
│   └── templatetags/
│       └── portfolio_tags.py  # Filtros de template
├── templates/             # Templates HTML
│   └── portfolio/
│       ├── base.html      # Template base
│       ├── home.html      # Página principal
│       ├── project_list.html   # Listado de proyectos
│       ├── project_detail.html # Detalle de proyecto
│       ├── about.html     # Sobre mí
│       └── contact.html   # Formulario de contacto
├── static/               # Archivos estáticos
│   ├── css/
│   ├── js/
│   └── images/
├── media/                # Archivos subidos por usuarios
├── requirements.txt      # Dependencias Python
└── manage.py            # Script de gestión de Django
```

## 🗂️ Modelos de Base de Datos

### Project
- Título, slug, descripción corta y larga
- Tecnologías, categoría (datos, gestión, desarrollo, infra, IA)
- Imagen de portada, video de demostración
- URLs de GitHub y sitio en vivo
- Destaque, contador de vistas, orden
- Timestamps (creado, actualizado)

### ProjectImage
- Relación con Project (Foreign Key)
- Imagen de galería y miniatura automática
- Descripción opcional
- Orden de visualización

### Skill
- Nombre, categoría (datos, backend, frontend, gestión, cloud)
- Icono SVG e imagen de icono
- Nivel de profundidad (0-100) con barra de progreso
- Orden personalizable

### Achievement
- Título, slug, descripción
- Organización, tipo (competencia, certificación, premio, reconocimiento)
- Posición/rango (Ej: 3er puesto)
- Fecha de logro
- Imágenes de certificado y badge
- URL de verificación
- Destaque, orden, timestamps

### Logo
- Nombre, tipo (empresa, tecnología, cliente, partner)
- Imagen PNG/JPG
- SVG optimizado
- URL relacionada
- Orden personalizable

## 🎛️ Panel de Administración

El panel está completamente personalizado con:

### ProjectAdmin
- Lista de visualización: título, categoría, destaque, orden, vistas, fecha
- Filtros por categoría, destaque y fecha
- Búsqueda en título, tecnologías y descripción
- Fieldsets organizados por secciones
- Inlines para agregar imágenes de galería
- Campos readonly para vistas y timestamps

### AchievementAdmin
- Lista de visualización: título, organización, tipo, posición, fecha, destaque
- Filtros por tipo, destaque y fecha
- Búsqueda en título, organización y descripción
- Fieldsets: información, detalles, media, verificación, opciones

### SkillAdmin y LogoAdmin
- Organizados por tipo y orden
- Búsqueda rápida

## 🚀 Despliegue en Producción

### Configuración para Producción

1. **Editar settings.py**:
```python
DEBUG = False
ALLOWED_HOSTS = ['tu-dominio.com']
SECRET_KEY = 'tu-clave-secreta-generada'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Cambiar a PostgreSQL
        'NAME': 'nombre_bd',
        'USER': 'usuario',
        'PASSWORD': 'contraseña',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

2. **Collectar archivos estáticos**:
```bash
python manage.py collectstatic
```

3. **Crear variables de entorno** (`.env`):
```
SECRET_KEY=tu-clave-secreta
DEBUG=False
ALLOWED_HOSTS=tu-dominio.com,www.tu-dominio.com
DATABASE_URL=postgresql://usuario:password@localhost/bd
```

4. **Ejecutar con Gunicorn**:
```bash
gunicorn mi_portafolio.wsgi:application --bind 0.0.0.0:8000
```

5. **Configurar con Nginx/Apache**: Reverse proxy hacia Gunicorn

## 🎨 Customización

### Colores
Editar en `templates/portfolio/base.html` la sección `Tailwind Config`:
```javascript
tailwind.config = {
    theme: {
        extend: {
            colors: {
                'electric-blue': '#00d4ff',
                'neon-green': '#00ff88',
            }
        }
    }
}
```

### CDNs
Cambiar versiones de librerías en `base.html`:
- Tailwind CSS
- GSAP y ScrollTrigger
- Three.js
- Swiper

### Información Personal
1. Editar nombre en `base.html` navbar
2. Cambiar email de contacto en `views.py` (función contact)
3. Actualizar URLs de redes sociales en `footer`

## 📊 Optimización de Imágenes

Utilidades automáticas en `portfolio/utils.py`:
- **optimize_image()**: Redimensiona y comprime imágenes
- **create_thumbnail()**: Genera miniaturas automáticas
- **convert_to_webp()**: Convierte a WebP para mejor compresión

Llamadas en modelos mediante `save()` personalizado.

## ✨ Características Premium

- ✅ Gestión multimedia completa con optimización automática
- ✅ Sistema de logros visuales con badges y certificados
- ✅ Timeline animada de achievements
- ✅ Slider infinito de logos de tecnologías
- ✅ Lazy loading e imágenes responsivas
- ✅ Analytics básico (contador de vistas)
- ✅ Formulario de contacto funcional
- ✅ Navegación tipo SPA con transiciones suaves
- ✅ Animaciones scroll-triggered con GSAP
- ✅ Hero 3D interactivo con Three.js
- ✅ Glassmorphism en toda la UI
- ✅ Totalmente responsive

## 🔐 Seguridad

- ✅ CSRF Protection activado
- ✅ XSS Protection activado
- ✅ SQL Injection prevention (ORM de Django)
- ✅ Secret key segura en variables de entorno
- ✅ DEBUG desactivado en producción
- ✅ ALLOWED_HOSTS configurado
- ✅ Validación de formularios en backend

## 📞 Soporte y Mantenimiento

### Tareas Comunes

**Agregar un nuevo proyecto**:
1. Ir a `/admin/`
2. Seleccionar "Proyectos"
3. Hacer clic en "Agregar Proyecto"
4. Completar formulario
5. Agregar imágenes en la sección inline
6. Guardar

**Crear una certificación/logro**:
1. Ir a `/admin/`
2. Seleccionar "Logros"
3. Agregar título, organización, tipo, fecha
4. Subir imagen de badge/certificado
5. Guardar

**Gestionar habilidades**:
1. Ir a `/admin/`
2. Seleccionar "Habilidades"
3. Agregar nombre, categoría, nivel (0-100)
4. Opcionalmente agregar icono SVG o imagen
5. Guardar

## 🐛 Troubleshooting

**Problema: Las imágenes no se cargan**
- Solución: Ejecutar `python manage.py collectstatic`

**Problema: CSRF token inválido**
- Solución: Verificar que `DEBUG=True` en desarrollo

**Problema: Errores de permiso al cargar archivos**
- Solución: Verificar permisos en carpeta `media/`

**Problema: El servidor no inicia**
- Solución: Ejecutar migraciones: `python manage.py migrate`

## 📄 Licencia

Este proyecto es propiedad de Nelson Javier Gutierrez Ramos.

## 👨‍💻 Autor

**Nelson Javier Gutierrez Ramos**
- Ingeniero de Sistemas Empresariales
- LinkedIn: [Ver perfil](https://www.linkedin.com/in/nelson-javier-gutierrez-ramos-6a5b60215)
- GitHub: [@javier321jg](https://github.com/javier321jg)
- Email: nelson@ejemplo.com

---

Desarrollado con ❤️ usando Django y tecnologías web modernas.
