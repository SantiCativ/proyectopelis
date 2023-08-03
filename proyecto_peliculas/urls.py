"""
URL configuration for proyecto_peliculas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import peliculas.views as view


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',view.PaginaInicio.as_view(),name='home'),
    path('actor/<int:actor_id>/',view.VistaActor.as_view(),name='actor'),
    path('director/<int:director_id>/',view.VistaDirector.as_view(),name='director'),
    path('pelicula/<int:pelicula_id>/',view.VistaPelicula.as_view(),name='pelicula'),
    path('pelicula/critica/<int:pelicula_id>/', view.CriticaFormsTemplate.as_view(), name='critica'),
    
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
