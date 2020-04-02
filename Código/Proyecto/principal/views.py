from django.views.generic import TemplateView
from urllib.request import urlopen
from bs4 import BeautifulSoup

class PrincipalView(TemplateView):
    template_name = 'index.html'

def scrapping_stack(busqueda):
    html = urlopen("https://google.com")
    bsobj = BeautifulSoup(html.read())
    print(bsobj.h1)


