#from django.shortcuts import render
from typing import Any, Dict
from django.views.generic.base import TemplateView
#F es una herramienta muy útil para realizar operaciones y filtrados directamente en la base de datos,
# lo que puede mejorar el rendimiento y la eficiencia de tus consultas en Django.
from django.db.models import F
from django.core.paginator import Paginator
from peliculas.models import *

#Utilizo para formulario
from django.shortcuts import get_object_or_404
from .forms import CriticaForm
from django.views.generic.edit import FormView


# Create your views here.
    
    
class PaginaInicio(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
       # Filtrar y ordenar películas por ranking ascendente
        pelicula_list = Pelicula.objects.all().order_by(F('ranking').desc())
        paginator=Paginator(pelicula_list,18)
        page_number= self.request.GET.get('page') # Se obtiene el número de página actual de la solicitud GET. Esto se hace accediendo al atributo GET del objeto request y obteniendo el valor del parámetro "page".
        context['page_obj']= paginator.get_page(page_number) #Se agrega al contexto un objeto page_obj que representa la página actual de la lista paginada de libros. Esto se obtiene utilizando el método get_page del objeto paginator y pasando el número de página actual.
        return context
    
    
class CriticaFormsTemplate(FormView):
    template_name = 'critica_form.html'
    form_class = CriticaForm
    success_url = 'http://127.0.0.1:8000' # Puedes redirigir a una página de agradecimiento o la URL que desees.
    http_method_names=['get','post']
    
    def form_valid(self, form):
        #obtengo el id a partir de la url
        pelicula_id = self.kwargs['pelicula_id']
        
        #similar a una api con metodo la cual me devuelve una pelicula especifica.
        #Aquí se obtiene la instancia de la película utilizando el ID que se ha pasado en la URL.
        # get_object_or_404 es una función de Django que obtiene un objeto o devuelve un error 404 si
        # el objeto no se encuentra.
        pelicula = get_object_or_404(Pelicula, pk=pelicula_id)

        #Aquí se guarda la instancia del formulario en la variable critica, pero con commit=False para evitar
        # que se guarde inmediatamente en la base de datos. Esto permite realizar cambios adicionales en la instancia
        # antes de guardarla.    
        critica = form.save(commit=False)
        #Se establece la relación entre la crítica y la película asociándola al campo peli del modelo Critica.
        critica.peli = pelicula
        #guardamos instancia
        critica.save()
      
      
        # Actualizar el ranking de la película
        
        # Obtener todos los puntajes de las críticas asociadas a la película
        #La opción flat=True se utiliza para obtener una lista plana de los valores de los puntajes en lugar de una lista de tuplas.
        puntajes = Critica.objects.filter(peli=pelicula).values_list('puntaje', flat=True)
        
        promedio_puntajes = sum(puntajes) / len(puntajes)
        pelicula.ranking = promedio_puntajes
        pelicula.save()

        return super().form_valid(form)
    
    
    
class VistaPelicula(TemplateView):
    
    template_name = 'pelicula.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pelicula_id = self.kwargs['pelicula_id']
        #obtenemos la peli a travez de la url
        pelicula = get_object_or_404(Pelicula, pk=pelicula_id)
        critica=Critica.objects.filter(peli=pelicula)
        context['comentarios']=critica
        context['peli']=pelicula
        return context


class VistaActor(TemplateView):
    
    template_name = 'actor.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        actor_id = self.kwargs['actor_id']
        #obtenemos el actor a travez de la url
        actores = get_object_or_404(Actor, pk=actor_id)
        peliculas=Pelicula.objects.filter(actores=actor_id)
        context['peli']=peliculas
        context['actor']=actores
        return context
    
    
    
class VistaDirector(TemplateView):
    
    template_name = 'director.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        director_id = self.kwargs['director_id']
        #obtenemos el director a travez de la url
        directores = get_object_or_404(Director, pk=director_id)
        peliculas=Pelicula.objects.filter(directores=director_id)
        context['peli']=peliculas
        context['director']=directores
        return context



    
    
