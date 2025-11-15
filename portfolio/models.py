from django.db import models
from django.utils.text import slugify


class Project(models.Model):
    """Modelo para proyectos del portafolio"""

    CATEGORY_CHOICES = [
        ('datos', 'Análisis de Datos y BI'),
        ('gestion', 'Gestión de Proyectos y Procesos'),
        ('desarrollo', 'Desarrollo Web y Software'),
        ('infra', 'Infraestructura y Soporte'),
        ('ia', 'Inteligencia Artificial y ML'),
    ]

    title = models.CharField(max_length=200, verbose_name="Título")
    slug = models.SlugField(unique=True, max_length=200, verbose_name="Slug")
    short_description = models.CharField(max_length=300, verbose_name="Descripción corta")
    description = models.TextField(verbose_name="Descripción completa")
    technologies = models.CharField(max_length=300, verbose_name="Tecnologías")
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        verbose_name="Categoría"
    )
    github_url = models.URLField(blank=True, null=True, verbose_name="URL de GitHub")
    live_url = models.URLField(blank=True, null=True, verbose_name="URL del sitio en vivo")
    cover_image = models.ImageField(
        upload_to='projects/covers/',
        verbose_name="Imagen de portada"
    )
    video_demo = models.FileField(
        upload_to='projects/videos/',
        blank=True,
        null=True,
        verbose_name="Video de demostración"
    )
    is_featured = models.BooleanField(default=False, verbose_name="¿Es destacado?")
    views_count = models.IntegerField(default=0, verbose_name="Contador de vistas")
    order = models.IntegerField(default=0, verbose_name="Orden")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ['order', '-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    """Modelo para galería de imágenes de un proyecto"""

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name="Proyecto"
    )
    image = models.ImageField(
        upload_to='projects/gallery/',
        verbose_name="Imagen"
    )
    thumbnail = models.ImageField(
        upload_to='projects/thumbnails/',
        blank=True,
        null=True,
        verbose_name="Miniatura"
    )
    caption = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Descripción"
    )
    order = models.IntegerField(default=0, verbose_name="Orden")

    class Meta:
        verbose_name = "Imagen de proyecto"
        verbose_name_plural = "Imágenes de proyectos"
        ordering = ['order']

    def __str__(self):
        return f"{self.project.title} - Imagen {self.order}"


class Skill(models.Model):
    """Modelo para habilidades profesionales"""

    CATEGORY_CHOICES = [
        ('datos', 'Datos y BI'),
        ('backend', 'Backend'),
        ('frontend', 'Frontend'),
        ('gestion', 'Gestión'),
        ('cloud', 'Cloud & DevOps'),
    ]

    name = models.CharField(max_length=100, verbose_name="Nombre")
    icon_svg = models.TextField(
        blank=True,
        verbose_name="Ícono SVG",
        help_text="Código SVG del ícono"
    )
    icon_image = models.ImageField(
        upload_to='skills/icons/',
        blank=True,
        null=True,
        verbose_name="Imagen del ícono"
    )
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        verbose_name="Categoría"
    )
    proficiency = models.IntegerField(
        default=50,
        verbose_name="Nivel de profundidad",
        help_text="0-100 para la barra de progreso"
    )
    order = models.IntegerField(default=0, verbose_name="Orden")

    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades"
        ordering = ['order', 'category', 'name']

    def __str__(self):
        return self.name


class Achievement(models.Model):
    """Modelo para logros, certificaciones y reconocimientos"""

    TYPE_CHOICES = [
        ('competition', 'Competencia'),
        ('certification', 'Certificación'),
        ('award', 'Premio'),
        ('recognition', 'Reconocimiento'),
    ]

    title = models.CharField(max_length=200, verbose_name="Título")
    slug = models.SlugField(unique=True, max_length=200, verbose_name="Slug")
    description = models.TextField(verbose_name="Descripción")
    organization = models.CharField(max_length=200, verbose_name="Organización")
    achievement_type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        verbose_name="Tipo"
    )
    position = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Posición",
        help_text="Ej: 3er Puesto, Gold Badge, etc."
    )
    date_achieved = models.DateField(verbose_name="Fecha de logro")
    certificate_image = models.ImageField(
        upload_to='achievements/certificates/',
        blank=True,
        null=True,
        verbose_name="Imagen del certificado"
    )
    badge_image = models.ImageField(
        upload_to='achievements/badges/',
        blank=True,
        null=True,
        verbose_name="Imagen del badge"
    )
    url = models.URLField(blank=True, null=True, verbose_name="URL de verificación")
    is_featured = models.BooleanField(default=False, verbose_name="¿Es destacado?")
    order = models.IntegerField(default=0, verbose_name="Orden")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    class Meta:
        verbose_name = "Logro"
        verbose_name_plural = "Logros"
        ordering = ['-date_achieved', 'order']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Logo(models.Model):
    """Modelo para gestión centralizada de logos"""

    LOGO_TYPE_CHOICES = [
        ('company', 'Empresa'),
        ('technology', 'Tecnología'),
        ('client', 'Cliente'),
        ('partner', 'Partner'),
    ]

    name = models.CharField(max_length=100, verbose_name="Nombre")
    logo_type = models.CharField(
        max_length=20,
        choices=LOGO_TYPE_CHOICES,
        verbose_name="Tipo de logo"
    )
    logo_image = models.ImageField(
        upload_to='logos/',
        verbose_name="Imagen del logo"
    )
    logo_svg = models.TextField(
        blank=True,
        verbose_name="Logo SVG",
        help_text="Versión SVG optimizada del logo"
    )
    url = models.URLField(blank=True, null=True, verbose_name="URL relacionada")
    order = models.IntegerField(default=0, verbose_name="Orden")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    class Meta:
        verbose_name = "Logo"
        verbose_name_plural = "Logos"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name
