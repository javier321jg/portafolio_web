from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.core.mail import send_mail
from django.views.decorators.http import require_http_methods
from .models import Project, Skill, Achievement, Logo
from .forms import ContactForm


def home(request):
    """Vista de la página principal con proyectos destacados, logros y tecnologías"""
    featured_projects = Project.objects.filter(is_featured=True).order_by('order')[:6]
    featured_achievements = Achievement.objects.filter(is_featured=True).order_by('order')[:3]
    technology_logos = Logo.objects.filter(logo_type='technology').order_by('order')

    context = {
        'featured_projects': featured_projects,
        'featured_achievements': featured_achievements,
        'technology_logos': technology_logos,
    }
    return render(request, 'portfolio/home.html', context)


def project_list(request):
    """Vista de listado de todos los proyectos con filtros y paginación"""
    projects = Project.objects.all()

    # Filtrar por categoría si se especifica
    category = request.GET.get('categoria')
    if category:
        projects = projects.filter(category=category)

    # Paginación
    paginator = Paginator(projects, 9)  # 9 proyectos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Obtener todas las categorías para los filtros
    categories = Project.CATEGORY_CHOICES

    context = {
        'page_obj': page_obj,
        'categories': categories,
        'current_category': category,
    }
    return render(request, 'portfolio/project_list.html', context)


def project_detail(request, slug):
    """Vista de detalle de un proyecto con galería"""
    project = get_object_or_404(Project, slug=slug)
    gallery_images = project.images.all()

    # Incrementar contador de vistas
    project.views_count += 1
    project.save(update_fields=['views_count'])

    context = {
        'project': project,
        'gallery_images': gallery_images,
    }
    return render(request, 'portfolio/project_detail.html', context)


def about(request):
    """Vista de la página Acerca de mí con skills, logros y empresas"""
    skills = Skill.objects.all().order_by('order', 'category')
    achievements = Achievement.objects.all().order_by('-date_achieved')
    company_logos = Logo.objects.filter(logo_type='company').order_by('order')

    # Organizar skills por categoría
    skills_by_category = {}
    for skill in skills:
        cat = skill.get_category_display()
        if cat not in skills_by_category:
            skills_by_category[cat] = []
        skills_by_category[cat].append(skill)

    context = {
        'skills_by_category': skills_by_category,
        'achievements': achievements,
        'company_logos': company_logos,
    }
    return render(request, 'portfolio/about.html', context)


@require_http_methods(["GET", "POST"])
def contact(request):
    """Vista del formulario de contacto"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            correo = form.cleaned_data['correo']
            asunto = form.cleaned_data['asunto']
            mensaje = form.cleaned_data['mensaje']

            # Enviar email (en desarrollo se imprime en consola)
            full_message = f"Mensaje de: {nombre} <{correo}>\n\n{mensaje}"

            try:
                send_mail(
                    subject=f"Portafolio - {asunto}",
                    message=full_message,
                    from_email=correo,
                    recipient_list=['nelson@ejemplo.com'],  # Cambiar por el email real
                    fail_silently=False,
                )
                messages.success(request, '¡Mensaje enviado con éxito! Te responderé pronto.')
                return redirect('contact')
            except Exception as e:
                messages.error(request, 'Hubo un error al enviar el mensaje. Por favor, intenta nuevamente.')
    else:
        form = ContactForm()

    context = {
        'form': form,
    }
    return render(request, 'portfolio/contact.html', context)
