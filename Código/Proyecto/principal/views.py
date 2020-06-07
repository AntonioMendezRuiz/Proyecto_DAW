from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

def consulta(request):
    try:
        #Preparamos la query para introducirla en el buscador
        busqueda = request.GET.get('busca')
        quitaSpace = busqueda.replace(' ', '+')

        #Asignamos las búsquedas para las diferentes webs 
        busquedaStack = "http://www.google.com.co/search?hl=es&q="+quitaSpace+"+stackoverflow&btnG=Buscar&meta="
        busquedaWebProgramador = "http://www.google.com.co/search?hl=es&q="+quitaSpace+"+la+web+del+programador&btnG=Buscar&meta="
        
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
        urlWeb = urlWeb.split('&')[0]

        #Repetimos proceso para acceder a la información desde la web
        reqStackFinal = requests.get(urlStack)
        reqWebFinal = requests.get(urlWeb)
        htmlStackFinal = BeautifulSoup(reqStackFinal.text, "html.parser")
        htmlWebFinal = BeautifulSoup(reqWebFinal.text, "html.parser")

        #Extraemos información de StackOverFlow
        preguntaStack = htmlStackFinal.find_all('div', class_='post-text')[0]
        respuestaStack = htmlStackFinal.find_all('div', class_='post-text')[1]
        preguntaWeb = htmlWebFinal.find_all('div', class_='ce')[0]
        #Aquí he tenido que buscar etiquetas dentro de etiquetas debido a la estructura del web
        respuestaWeb = htmlWebFinal.find_all('div', class_='codeFormat')[0]
        respuestaWeb = respuestaWeb.find('div')
        respuestaWeb = respuestaWeb.find('div').nextSibling
        
        #Los códigos de la web del programador precisa de estos cambios para el formateo del código
        respuestaWeb = respuestaWeb.find_all('pre')
        respuestaWebFinal = []
        for element in respuestaWeb:
            respuestaWebFinal.append(element.get_text())
            respuestaWebFinal.append('<br>')

        #Añadimos la etiqueta code a la la respuestaWeb para el formato
        respuestaWebFinal.insert(0, '<code>')
        respuestaWebFinal.insert(0, '<pre>')
        respuestaWebFinal.append('</code>')
        respuestaWebFinal.append('</pre>')

        #Tenemos una lista con cada una de las etiquetas así que lo pasamos a string
        preguntaStack = ''.join(str(e) for e in preguntaStack)
        respuestaStack = ''.join(str(e) for e in respuestaStack)
        preguntaWeb = ''.join(str(e) for e in preguntaWeb)
        respuestaWebFinal = ''.join(str(e) for e in respuestaWebFinal)

        #Introducimos la clase prettyfy para los códigos
        preguntaStack = preguntaStack.replace('<code>', '<code class="prettyprint">')
        respuestaStack = respuestaStack.replace('<code>', '<code class="prettyprint">')
        preguntaWeb = preguntaWeb.replace('<code>', '<code class="prettyprint">')
        respuestaWebFinal = respuestaWebFinal.replace('<code>', '<code class="prettyprint">')

        #Asiganamos los valores que queremos pasar al front
        values = {'preguntaStack': preguntaStack, 'respuestaStack': respuestaStack, 'preguntaWeb': preguntaWeb, 'respuestaWeb': respuestaWebFinal}
        
        #Finalmente enviamos la información al front
        return render(request, "respuestas.html", values)
    except:
        #De suceder algún error o no encontrarse la respuesta deseada, se mostrará este mensaje
        values = {'preguntaStack': 'La consulta no es lo suficientemente precisa o no existe.', 'respuestaStack': '', 'preguntaWeb': 'La consulta no es lo suficientemente precisa o no existe.', 'respuestaWeb': ''}
        return render(request, "respuestas.html", values)


def PrincipalView(request):
    return render(request, "index.html")

        
        

    

