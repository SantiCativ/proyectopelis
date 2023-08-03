from django.contrib import admin

from django.forms import ClearableFileInput
from django import forms

#para las acciones
from django.contrib import messages
from django.utils.translation import ngettext


# Register your models here.

from .models import *


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = [ "id","nombre", "nacionalidad", "imagen"]
    
    #hipervinculo al formulario del director
    list_display_links=["nombre"]
    list_filter=["nacionalidad"]
    
    #paginacion
    list_per_page=5
    
    fieldsets = [
        ("Datos Personales:", {"fields": ["nombre"]}),
        (None, {"fields": ["añoNacimiento"]}),
        (None, {"fields": ["nacionalidad"]}),
        ("Su Resumen:", {"fields": ["resumen"]}),
        ("Foto", {"fields": ["foto"]}),
    ]
    
    search_fields = ["nombre"]
    
    def imagen(self, obj):
        return obj.image_tag()
    




@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    
    list_display = [ "id","nombre", "nacionalidad", "imagen"]
    list_editable = ["nacionalidad"]
    #hipervinculo al formulario del actor
    list_display_links=["nombre"]
    list_filter=["nacionalidad"]
    #paginacion
    list_per_page=5
    
    fieldsets = [
        ("Datos Personales:", {"fields": ["nombre"]}),
        (None, {"fields": ["añoNacimiento"]}),
        (None, {"fields": ["nacionalidad"]}),
        ("Su Resumen:", {"fields": ["resumen"]}),
        ("Foto", {"fields": ["foto"]}),
    ]
    
    search_fields = ["nombre"]
    
    def imagen(self, obj):
        return obj.image_tag()
    
    


  
  

    
    
    
@admin.register(Pelicula)

class PeliculaAdmin(admin.ModelAdmin):
        
    
    list_display=["id","nombre","categoria","ranking","imagen"]
    list_display_links=["nombre"]
    list_editable=["categoria"]
    filter_horizontal=["actores"]
    date_hierarchy="añoRealizacion"
    list_per_page=5
    list_filter = ["categoria"]
    search_fields = ["nombre"]
    # actions=["aventura","accion"]
    exclude=["ranking"]
    readonly_fields = ('image_tag',)
        
        
    fieldsets = [
            ("Datos:", {"fields": ["nombre"]}),
            (None, {"fields": ["añoRealizacion"]}),
            (None, {"fields": ["resumen"]}),
            (None, {"fields": ["foto"]}),
            (None, {"fields": ["categoria"]}),
            ("Participantes:", {"fields": ["actores"]}),
            (None, {"fields": ["directores"]}),
        ]
    
        
    
    def imagen(self, obj):
        return obj.image_tag()
  
    
    
    #acciones para peliculas

    # @admin.action()
    # def aventura(self, request, queryset):
    #     updated=queryset.update(categoria="Aventura")
    #     self.message_user(
    #         request,
    #         ngettext(
    #             "%d Categoria cambiada a Acción corretamente.",
    #             "%d Categorias cambiada a Acción corretamente.",
    #             updated,
    #         )
    #         % updated,
    #         messages.SUCCESS,
    #     )
            

    # def accion(self, request, queryset):
    #     queryset.update(categoria="Acción")
        
    
    
    
    
   
    
 
 

 


@admin.register(Critica)
class CriticaAdmin(admin.ModelAdmin):
    
    list_display=["id","Estado","reseña","puntaje","pelicula","fecha"]
    ordering=["id"]
    list_per_page=5
    list_filter = ["estado","peli"]
    actions=["aprobado","desaprobado"]
    ordering = ['-fecha', ]
    
    
    #cambiar de nombre el campo de peli en el administrador y aparezca "pelicula"
    @admin.display(description="Pelicula")
    def pelicula(self, obj):
        return obj.peli
    
    
    
    
   
    
    
    
    
#Acciones para las criticas 

    @admin.action(description="Aprobar critica/s")
    def aprobado(self, request, queryset):
            updated=queryset.update(estado="aprobado")
            self.message_user(
                request,
                ngettext(
                    "%d Critica aprobada correctamente.",
                    "%d Criticas aprobadas corretamente.",
                    updated,
                )
                % updated,
                messages.SUCCESS,
            )

    @admin.action(description="Desaprobar critica/s")
    def desaprobado(self, request, queryset):
            updated=queryset.update(estado="desaprobado")
            self.message_user(
                request,
                ngettext(
                    "%d Critica desaprobada correctamente.",
                    "%d Criticas desaprobadas corretamente.",
                    updated,
                )
                % updated,
                messages.SUCCESS,
            )





