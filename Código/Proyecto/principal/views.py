from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from urllib.request import urlopen
from bs4 import BeautifulSoup

@csrf_exempt

def scrapping(request):
    if request.method == 'POST':
        busqueda = request.POST.get('busca')
        html = urlopen("https://google.com/" + busqueda)
        bsobj = BeautifulSoup(html.read())
        bsobj1 = bsobj.title
        template = loader.get_template("respuestas.html")

        return HttpResponse(template.render(bsobj1, request))



class RespuestasView(TemplateView):
    template_name = 'respuestas.html'


class PrincipalView(TemplateView):
    template_name = 'index.html'

        
        

    

