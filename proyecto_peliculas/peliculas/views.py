#from django.shortcuts import render
from typing import Any, Dict
from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView
import datetime

# Create your views here.


class VistaHora(View):
    def get(self,request):
        now=datetime.datetime.now()
        html="<html><body> esta es la hora %s </body></html>" %now
        return HttpResponse(html)
    

class VistaHoraTemplate(TemplateView):
    template_name='hora.html'
    def get_context_data(self, **kwargs: Any):
        context=super().get_context_data( **kwargs)
        context['hora']=datetime.datetime.now()
        return context
    
    
    
