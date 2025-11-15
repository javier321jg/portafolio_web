from django.contrib import admin
from .models import Project, ProjectImage, Skill


class ProjectImageInline(admin.TabularInline):
    """Inline para agregar imágenes a la galería de un proyecto"""
    model = ProjectImage
    extra = 1
    fields = ('image', 'caption', 'order')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """Administrador para el modelo Project"""
    list_display = ('title', 'category', 'is_featured', 'order', 'created_at')
    list_filter = ('category', 'is_featured', 'created_at')
    search_fields = ('title', 'technologies', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('order', '-created_at')
    inlines = [ProjectImageInline]

    fieldsets = (
        ('Información básica', {
            'fields': ('title', 'slug', 'category', 'short_description')
        }),
        ('Descripción y tecnologías', {
            'fields': ('description', 'technologies')
        }),
        ('Enlaces', {
            'fields': ('github_url', 'live_url')
        }),
        ('Imagen de portada', {
            'fields': ('cover_image',)
        }),
        ('Opciones', {
            'fields': ('is_featured', 'order')
        }),
    )


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    """Administrador para el modelo ProjectImage"""
    list_display = ('project', 'caption', 'order')
    list_filter = ('project',)
    ordering = ('project', 'order')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    """Administrador para el modelo Skill"""
    list_display = ('name', 'category')
    list_filter = ('category',)
    search_fields = ('name',)
    ordering = ('category', 'name')
