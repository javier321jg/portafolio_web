from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('proyectos/', views.project_list, name='project_list'),
    path('proyectos/<slug:slug>/', views.project_detail, name='project_detail'),
    path('sobre-mi/', views.about, name='about'),
    path('contacto/', views.contact, name='contact'),
]
