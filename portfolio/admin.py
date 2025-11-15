from django.contrib import admin
from .models import Project, ProjectImage, Skill, Achievement, Logo


class ProjectImageInline(admin.TabularInline):
    """Inline para agregar imágenes a la galería de un proyecto"""
    model = ProjectImage
    extra = 1
    fields = ('image', 'thumbnail', 'caption', 'order')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """Administrador para el modelo Project"""
    list_display = ('title', 'category', 'is_featured', 'order', 'views_count', 'created_at')
    list_filter = ('category', 'is_featured', 'created_at')
    search_fields = ('title', 'technologies', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('order', '-created_at')
    inlines = [ProjectImageInline]
    readonly_fields = ('views_count', 'created_at', 'updated_at')

    fieldsets = (
        ('Información básica', {
            'fields': ('title', 'slug', 'category', 'short_description')
        }),
        ('Descripción y tecnologías', {
            'fields': ('description', 'technologies')
        }),
        ('Media', {
            'fields': ('cover_image', 'video_demo')
        }),
        ('Enlaces', {
            'fields': ('github_url', 'live_url')
        }),
        ('Opciones y estadísticas', {
            'fields': ('is_featured', 'order', 'views_count')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
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
    list_display = ('name', 'category', 'proficiency', 'order')
    list_filter = ('category',)
    search_fields = ('name',)
    ordering = ('order', 'category', 'name')

    fieldsets = (
        ('Información básica', {
            'fields': ('name', 'category', 'order')
        }),
        ('Iconos', {
            'fields': ('icon_svg', 'icon_image')
        }),
        ('Nivel de profundidad', {
            'fields': ('proficiency',),
            'description': 'Escala 0-100'
        }),
    )


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    """Administrador para el modelo Achievement"""
    list_display = ('title', 'organization', 'achievement_type', 'position', 'date_achieved', 'is_featured')
    list_filter = ('achievement_type', 'is_featured', 'date_achieved')
    search_fields = ('title', 'organization', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-date_achieved', 'order')
    readonly_fields = ('created_at',)

    fieldsets = (
        ('Información básica', {
            'fields': ('title', 'slug', 'description', 'organization')
        }),
        ('Detalles del logro', {
            'fields': ('achievement_type', 'position', 'date_achieved')
        }),
        ('Media', {
            'fields': ('certificate_image', 'badge_image')
        }),
        ('Enlace de verificación', {
            'fields': ('url',)
        }),
        ('Opciones', {
            'fields': ('is_featured', 'order')
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )


@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    """Administrador para el modelo Logo"""
    list_display = ('name', 'logo_type', 'order')
    list_filter = ('logo_type',)
    search_fields = ('name',)
    ordering = ('order', 'name')

    fieldsets = (
        ('Información básica', {
            'fields': ('name', 'logo_type', 'order')
        }),
        ('Archivos', {
            'fields': ('logo_image', 'logo_svg')
        }),
        ('URL relacionada', {
            'fields': ('url',)
        }),
    )
