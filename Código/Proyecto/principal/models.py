from django.db import models
from urllib.request import urlopen
from bs4 import BeautifulSoup


def scrapping_stack(busqueda):
    html = urlopen("https://es.stackoverflow.com")
    bsobj = BeautifulSoup(html.read())
    return bsobj.h1