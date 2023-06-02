from django.db import models
from django.db.models import Avg


# Create your models here.


class Director(models.Model):
    nombre=models.CharField(max_length=200)
    nacionalidad=models.CharField(max_length=200)
    añoNacimiento=models.DateField(null=True)
    resumen=models.CharField(max_length=300)
    foto=models.ImageField(upload_to='images/director')
    
    
class Actor(models.Model):
    
    nombre=models.CharField(max_length=200)
    nacionalidad=models.CharField(max_length=200)
    añoNacimiento=models.DateField(null=True)
    resumen=models.CharField(max_length=300)
    foto=models.ImageField(upload_to='images/actor')
    

    
    
class Pelicula (models.Model):
    nombre=models.CharField(max_length=200)
    añoRealizacion=models.DateField(null=True)
    resumen=models.TextField()
    foto=models.ImageField(upload_to='images/pelicula') 
    directores=models.ForeignKey(Director,on_delete=models.CASCADE)
    actores=models.ManyToManyField(Actor)
    categoria=models.CharField(max_length=200)
    ranking=models.DecimalField(max_digits=2, decimal_places=1,null=True) #ejemplos:= 4.3 - 3.9 - 2.3 - .1.7 
    
    @property
    def ranking(self):
        promedio_puntajes = self.criticas.aggregate(promedio=Avg('puntaje'))['promedio']
        if promedio_puntajes is not None:
            return round(promedio_puntajes, 1)
        else:
            return None
        

class Critica (models.Model):
    nombre= models.CharField(max_length=200)
    email= models.EmailField(max_length=254)
    reseña=models.TextField() # no sabemos cuanto se va a explayar el usuario
    
    SCORE_CHOICES = [
    (1, '1'), #Cada opción es una tupla que consiste en dos elementos: el valor almacenado en la base de datos y la representación legible para los usuarios.
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    ]
    puntaje = models.IntegerField(choices=SCORE_CHOICES)
    peli=models.ForeignKey(Pelicula,on_delete=models.CASCADE,related_name='criticas')
    
    
   

    


