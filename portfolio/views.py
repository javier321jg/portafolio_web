from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.core.mail import send_mail
from .models import Project, Skill
from .forms import ContactForm


def home(request):
    """Vista de la página principal con proyectos destacados"""
    featured_projects = Project.objects.filter(is_featured=True)[:6]
    context = {
        'featured_projects': featured_projects,
    }
    return render(request, 'portfolio/home.html', context)


def project_list(request):
    """Vista de listado de todos los proyectos con filtros"""
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
    """Vista de detalle de un proyecto"""
    project = get_object_or_404(Project, slug=slug)
    gallery_images = project.images.all()

    context = {
        'project': project,
        'gallery_images': gallery_images,
    }
    return render(request, 'portfolio/project_detail.html', context)


def about(request):
    """Vista de la página Acerca de mí"""
    skills = Skill.objects.all()

    # Organizar skills por categoría
    skills_by_category = {}
    for skill in skills:
        cat = skill.get_category_display()
        if cat not in skills_by_category:
            skills_by_category[cat] = []
        skills_by_category[cat].append(skill)

    context = {
        'skills_by_category': skills_by_category,
    }
    return render(request, 'portfolio/about.html', context)


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
