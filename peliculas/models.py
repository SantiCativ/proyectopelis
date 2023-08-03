from django.db import models
from django.utils.html import format_html
from django.core.exceptions import *
from datetime import datetime

#para que me muestre la imagen en la interfaz admin, como imagen previa.
from django.utils.safestring import mark_safe




# Create your models here.


class Director(models.Model):
    nombre=models.CharField(max_length=200)
    nacionalidad=models.CharField(max_length=200)
    añoNacimiento=models.DateField(null=True)
    resumen=models.CharField(max_length=300)
    foto=models.ImageField(upload_to='static/images/director')
    
    def __str__(self):
        return self.nombre
    
     #mostrar foto en el admin
    def image_tag(self):
        if self.foto:
            return mark_safe('<img src="%s" style="width: 75px; height:75px;" />' % self.foto.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Foto'
    
class Actor(models.Model):
    
    nombre=models.CharField(max_length=200)
    nacionalidad=models.CharField(max_length=200)
    añoNacimiento=models.DateField(null=True)
    resumen=models.CharField(max_length=300)
    foto=models.ImageField(upload_to='static/images/actor')
    
    def __str__(self):
        return self.nombre
    
      #mostrar foto en el admin
    def image_tag(self):
        if self.foto:
            return mark_safe('<img src="%s" style="width: 75px; height:75px;" />' % self.foto.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Foto'

    
    
    

    
    
class Pelicula (models.Model):
    nombre=models.CharField(max_length=200)
    añoRealizacion=models.DateField(null=True)
    resumen=models.TextField()
    foto=models.ImageField(upload_to='static/images/pelicula') 
    directores=models.ForeignKey(Director,on_delete=models.CASCADE)
    actores=models.ManyToManyField(Actor)
    ranking=models.DecimalField(max_digits=2, decimal_places=1,null=True,default=None) #ejemplos:= 4.3 - 3.9 - 2.3 - .1.7 
    actions=["aventura","accion"]
    tipo_categoria = [
        ('Acción', 'Acción'),
        ('Aventura', 'Aventura'),
        ('Ciencia Ficción', 'Ciencia Ficción'),
        ('Comedia', 'Comedia'),
        ('No-Ficción/Documental', 'No-Ficción/Documental'),
        ('Drama', 'Drama'),
        ('Fantasía', 'Fantasía'),  
        ('Musical','Musical'), 
        
    ]
    categoria = models.CharField(
        max_length=200,
        choices=tipo_categoria,
        default='',
    )
    
    
    def __str__(self):
        return self.nombre
    
    #mostrar foto en el admin
    def image_tag(self):
        if self.foto:
            return mark_safe('<img src="%s" style="width: 50px; height:75px;" />' % self.foto.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Foto'



    
    
    
        
  

class Critica (models.Model):
    nombre= models.CharField(max_length=200)
    email= models.EmailField(max_length=254)
    reseña=models.TextField("comentario") # no sabemos cuanto se va a explayar el usuario
    fecha = models.DateTimeField("Fecha", default=datetime.now)
    SCORE_CHOICES = [
    #Cada opción es una tupla que consiste en dos elementos: el valor almacenado en la base de datos y la representación legible para los usuarios.
    (1, '1'), 
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    ]
    puntaje = models.IntegerField(choices=SCORE_CHOICES)
    peli=models.ForeignKey(Pelicula,on_delete=models.CASCADE,related_name='criticas')
    
    
    
    ESTADO_COMENTARIO_CHOICES = [
        ("inicio", "inicio"),
        ("aprobado", "aprobado"),
        ("desaprobado", "desaprobado"), 
    ]
    estado = models.CharField("Estado", 
        max_length = 20,
        choices = ESTADO_COMENTARIO_CHOICES,
        default = "inicio",
    )
    
    
    def Estado(self):
        if self.estado == 'desaprobado':
            return format_html(
                '<span style="color:red;">{}</span>',
                self.estado,
                
            )
        elif self.estado == 'inicio':
            return format_html(
                '<span style="color:yellow;">{} </span>',
                self.estado,
               
            )
        else:  # Cuando el estado es "aprobado"
            return format_html(
                '<span style="color:green;">{}</span>',
                self.estado,
                
            )
        
        
    
    
    
   

    


