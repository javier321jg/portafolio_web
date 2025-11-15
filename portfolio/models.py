from django.db import models
from django.utils.text import slugify


class Project(models.Model):
    """Modelo para proyectos del portafolio"""

    CATEGORY_CHOICES = [
        ('datos', 'Análisis de Datos y BI'),
        ('gestion', 'Gestión de Proyectos y Procesos'),
        ('desarrollo', 'Desarrollo Web y Software'),
        ('infra', 'Infraestructura y Soporte'),
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
    is_featured = models.BooleanField(default=False, verbose_name="¿Es destacado?")
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
        ('datos', 'Datos'),
        ('backend', 'Backend'),
        ('frontend', 'Frontend'),
        ('gestion', 'Gestión'),
    ]

    name = models.CharField(max_length=100, verbose_name="Nombre")
    icon_svg = models.TextField(
        blank=True,
        verbose_name="Ícono SVG",
        help_text="Código SVG del ícono"
    )
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        verbose_name="Categoría"
    )

    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades"
        ordering = ['category', 'name']

    def __str__(self):
        return self.name
