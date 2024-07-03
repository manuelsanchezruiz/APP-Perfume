from django.contrib import admin
from django.urls import path, include
from perfumes.admin import admin_site  # Importa tu admin personalizado

urlpatterns = [
    path('admin/', admin_site.urls),  # Usa tu admin personalizado
    path('', include('perfumes.urls')),  # Incluye las URLs de tu aplicación
]
