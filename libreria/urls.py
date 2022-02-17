from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('nosotros', views.nosotros, name='Nosotros'),
    
    path('libros', views.libros, name='Libros'),
    path('libros/crear', views.crear, name='Crear'),
    path('eliminar/<int:id>', views.eliminar, name='Eliminar'),
    path('libros/editar/<int:id>', views.editar, name='Editar'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
