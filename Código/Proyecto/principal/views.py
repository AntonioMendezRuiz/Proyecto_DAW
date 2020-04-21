from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

def consulta(request):
    busqueda = request.GET.get('busca')
    quitaSpace = busqueda.replace(' ', '+')
    busquedaFinal = "https://google.com/search?q="+quitaSpace
    req = requests.get(busquedaFinal)
    html = BeautifulSoup(req.text, "html.parser")
    #htmlStack = urlopen(busquedaFinal)
    #bsobj = BeautifulSoup(htmlStack.read())
 

    values = {'prueba': html, 'busca': busquedaFinal}
    
    
    return render(request, "respuestas.html", values)


def PrincipalView(request):
    return render(request, "index.html")

        
        

    

