from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

def consulta(request):
    #Preparamos la query para introducirla en el buscador
    busqueda = request.GET.get('busca')
    quitaSpace = busqueda.replace(' ', '+')

    #Asignamos las búsquedas para las diferentes webs 
    busquedaStack = "http://www.google.com.co/search?hl=es&q="+quitaSpace+"+stackoverflow&btnG=Buscar&meta="
    busquedaWebProgramador = "http://www.google.com.co/search?hl=es&q="+quitaSpace+"+lawebdelprogramador&btnG=Buscar&meta="
    
    #Hacemos las peticiones
    reqStack = requests.get(busquedaStack)
    reqWeb = requests.get(busquedaWebProgramador)

    #Extrae el html de cada uno
    htmlStack = BeautifulSoup(reqStack.text, "html.parser")
    htmlWeb = BeautifulSoup(reqWeb.text, "html.parser")

    #Entramos en google en busca de las urls
    #StackOverFlow
    bsobj = htmlStack.find_all('div', class_= 'kCrYT')
    stack = bsobj[0].find_all('a', href=True)
    #LaWebDelProgramador
    bsobj1 = htmlWeb.find_all('div', class_= 'kCrYT')
    web = bsobj1[0].find_all('a', href=True)

    #Una vez tenemos las urls vamos a las webs en búsqueda de la información
    urlStack = stack[0].get_attribute_list('href')[0][7:]
    urlWeb = web[0].get_attribute_list('href')[0][7:]

    #Repetimos proceso para acceder a la información desde la web
    reqStackFinal = requests.get(urlStack)
    reqWebFinal = requests.get(urlWeb)
    htmlStackFinal = BeautifulSoup(reqStackFinal.text, "html.parser")
    htmlWebFinal = BeautifulSoup(reqWebFinal.text, "html.parser")

    #Extraemos información de StackOverFlow
    preguntaStack = htmlStackFinal.find_all('div', class_='post-text')[0]
    respuestaStack = htmlStackFinal.find_all('div', class_='post-text')[1]

    #Asiganamos los valores que queremos pasar al front
    values = {'preguntaStack': preguntaStack, 'respuestaStack': respuestaStack, 'preguntaWeb': urlWeb, 'respuestaWeb': 'WIP'}
    
    #Finalmente enviamos la información al front
    return render(request, "respuestas.html", values)


def PrincipalView(request):
    return render(request, "index.html")

        
        

    

