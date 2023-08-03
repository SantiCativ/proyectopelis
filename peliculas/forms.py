from django import forms
from django.forms import ModelForm 

from.models import Critica



class CriticaForm(ModelForm):
    
     # Establecer meta información del modelo del formulario
    class Meta:
       model = Critica
       fields = ["nombre", "email", "reseña", "puntaje"]

    
    # SCORE_CHOICES = [
    #     (1, '1'), 
    #     (2, '2'),
    #     (3, '3'),
    #     (4, '4'),
    #     (5, '5'),
    # ]
    # puntaje = forms.ChoiceField(choices=SCORE_CHOICES)
