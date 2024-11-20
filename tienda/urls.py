#URLS propias de la aplicación
from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    # Paginas principales
    path('', views.index, name='index'),
    path('videojuegos', views.videojuegos, name='videojuegos'),
    path('categorias', views.categorias, name='categorias'),
    path('admin-videojuegos', views.adminVideojuegos, name='admin-videojuegos'),
    path('admin-categorias', views.adminCategorias, name='admin-categorias'),

    # Crear
    path('admin-videojuegos/crear', views.crear_videojuego, name='crear-videojuego'),
    path('admin-categorias/crear', views.crear_categoria, name='crear-categoria'),

    # Editar
    path('admin-videojuegos/editar', views.editar_videojuego, name='editar-videojuego'),
    path('admin-videojuegos/editar/<int:id>', views.editar_videojuego, name='editar-videojuego'),

    path('admin-categorias/editar', views.editar_categoria, name='editar-categoria'),
    path('admin-categorias/editar/<int:id>', views.editar_categoria, name='editar-categoria'),

    # Eliminar
    path('admin-categorias/eliminar/<int:id>', views.eliminar_categoria, name='eliminar-categoria'),
    path('admin-videojuegos/eliminar/<int:id>', views.eliminar_videojuego, name='eliminar-videojuego'),

    # Filtrar por categoria
    path('categorias/<int:id>/videojuegos/', views.videojuegos_por_categoria, name='videojuegos-por-categoria'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
