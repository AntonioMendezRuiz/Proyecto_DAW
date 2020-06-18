# CodePass

**Realizado por**: Antonio Méndez Ruiz

**Tutor**: Paco Ávila

**Curso**: 2019/20

## Índice

1. Descripción e introducción
2. Objetivos
3. Arquitectura
4. Realización del Proyecto
5. Problemas encontrados
6. Posibles mejoras y próximos pasos
7. Bibliografía



## 1. Descripción del proyecto

En el presente proyecto se pretende desarrollar una aplicación web que realice la función de un comparador. En este caso, el objeto de comparación serán las respuestas ofrecidas a una pregunta lanzada por un potencial usuario relacionada con programación. Dudas de dependencia, de errores en código, de cómo hacer o crear un programa que cumpla una determinada función, etc. Este proyecto pretende ser además el trabajo final de Antonio Méndez Ruiz, por lo que es posible que existan varias releases, en función del alcance de una y otra parte.

## 2. Objetivos

El objetivo principal del software es crear un comparador de búsquedas sobre programación el cual facilite la labor del programador a la hora de realizar sus consultas. La intención es que dichas búsquedas aparezcan de una forma ordenada y clara en pantalla para que el usuario, de un solo vistazo, pueda ver cual se ajusta más a su duda y por tanto resolverla.

## 3. Arquitectura

Para la arquitectura del proyecto usaremos Django con la ayuda de algunas librerías de JavaScript como "Prettyfy" el cual sirve para el formateo de códigos en la web.

### Módulos

En esta sección se describen los módulos que van a constituir el software a desarrollar. Debido a la naturaleza del proyecto, la estructura de dichos módulos puede cambiar, por lo que esto es un texto vivo. Además de su arquitectura, también debería especificarse el lenguaje de programación en el que están siendo desarrollados dichos módulos.

- **<u>Front-End</u>**: El front se basará estrictamente en HTML y CSS a través de la utilización de plantillas que ofrece Django. Dichas plantillas se modularizarán de forma que cada componente (Véase el footer, header o el body) sean independientes y se puedan usar en cada una de las páginas de la web. Es posible la implementación de JavaScript.

  

- <u>**Back-End**</u>: El back será desarrollado en su totalidad en Python con las herramientas de las que nos provee Django y alguna librería adicional para realizar las funciones de web scrapping, que es en lo que se basará el proyecto.

  

## 4. Realización del proyecto

En este apartado se detallará el proceso de aprendizaje del framework así como del lenguaje, además de los pasos que hemos seguidos para alcanzar el punto en el que hoy se encuentra el software y los problemas que han ido surgiendo, tanto los que se han solucionado como los que no.



### Primeros pasos

En los primeros compases me dediqué a aprender como funcionaba Django mediante la realización de numerosas pruebas y ejercicios de prueba. Este proceso fue bastante largo debido a que casi empezaba de 0, tanto con Django como con Python, y a que tenía que adaptar los manuales de los cuales disponía para que sirvieran a mi aplicación.

Después de estas pruebas comencé con la búsqueda de información para la realización directa de mi aplicación. Esta búsqueda no la hice de manera completa en un principio debido a que conforme iba desarrollando el software me iba dando cuenta que necesitaba más cosas. En un primer lugar la búsqueda se centró en la parte del web scrapper, teniendo como primer resultado (y definitivo) la librería "BeautifulSoup" de Python cuya documentación aparece en el apartado de la bibliografía.

En el siguiente apartado se explicará la funcionalidad de la aplicación y el desarrollo (este último de una manera simplificada). Comenzaremos por la funcionalidad.

### Funcionalidad 

La funcionalidad del proyecto es bastante sencilla. Básicamente se trata de un buscador y comparador de consultas de programación las cuales vienen dadas en un formato "Consulta/Respuesta" para que el usuario pueda comparar de un solo vistazo las consultas y ver cual se ajusta mejor a sus necesidades.

El funcionamiento del software al realizar la consulta es el siguiente:

	- Usuario introduce en el campo de texto de la Main Page la consulta que quiere obtener.
	- La aplicación utiliza el motor de búsqueda de Google para encontrar la consulta, lo que hace que se ajuste el idioma de la consulta de manera automática.
	- Accedemos a las webs y extraemos los datos (Detallaremos esto más adelante).
	- Tratamos los datos en el back y los formateamos para enviarlos al front.
	- Mostramos los datos al usuario.
	- El usuario puede volver a la Main Page o realizar otra consulta desde esta misma ventana.

### Desarrollo

En este apartado detallaremos como ha sido el desarrollo de la aplicación y qué hemos usado para la realización del mismo. Comenzaremos con Django y sus peculiaridades. Todo el desarrollo ha sido realizado en Linux, concretamente en ubuntu.

![Django_logo](https://github.com/AntonioMendezRuiz/Proyecto_DAW/blob/master/img/Django_logo.png)

Después de la instalación de Django nos lanzamos a la creación del proyecto con el comando:

```
$ django-admin startproject CodePass
```

Lo que nos deja la siguiente estructura de carpetas:

```
CodePass/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

Por último, el comando que nos permitirá lanzar un servidor y observar nuestro trabajo:

```
$ python manage.py runserver
```

Este es nuestro punto de partida  en el desarrollo de la aplicación. Ahora entraremos en materia y veremos los diferentes achivos que entran en juego.

El archivo **settings.py** es aquel que se encarga de configurar todos los paramentros de la aplicación, desde usuarios hasta rangos de IPs que tienen acceso cuando está en despliegue. Este archivo no lo tocaremos mucho durante el desarrollo ya que no ha sido necesario modificar ninguno de estos parametros debido a que la aplicación no ha sido desplegueada aún, así que pasaremos al siguiente.

![settings](https://github.com/AntonioMendezRuiz/Proyecto_DAW/blob/master/img/settings.png)

El archivo **urls.py** detalla los diferentes paths de los que consta la aplicación, es decir, aquellas partes de la web donde puede acceder el usuario y cual es su url. Nuestra aplicación en este caso solo tiene un par paths, uno para la Main Page y otro para las consultas.

![urls](https://github.com/AntonioMendezRuiz/Proyecto_DAW/blob/master/img/urls.png)

El archivo **views.py** es el último que detallaremos y el mas importante pues es el que contiene la lógica del programa. En el se encuentran las vistas de las diferentes partes de la web. Vease la Main Page: 

![codigo_main](https://github.com/AntonioMendezRuiz/Proyecto_DAW/blob/master/img/codigo_main.png)

Y esta es la parte importante del programa, la view de consultas: 

![codigo_consultas](https://github.com/AntonioMendezRuiz/Proyecto_DAW/blob/master/img/codigo_consultas.png)

Haremos un resumen de esta última sin ahondar en cada detalle del código para no extendernos demasiado. En primer lugar la cosulta realizada en el usuario desde el front viene recogida por la función de Python "request.get("identificador HTML")" y una vez la tenemos, empezamos a trabajar con ella.

En primer lugar creamos la URL con la búsqueda del usuario. Aquí crearemos dos búsqueda, primero la de Google de la cual extraemos la URL de la web a la que queremos entrar y la asignamos a otra variable y usamos esta URL para entrar en la web deseada.

Acto seguido traemos el código HTML el cual necesitamos para la extracción de información de manera adecuada. Esta parte es la mas compleja porque cada web tiene un formato distinto y hay queda adaptar el código para cada una de ellas.

Una vez tenemos la información seleccionamos las etiquetas que nos interesan con la función de Python ".find("Etiqueta que queremos")"  la cual nos da una lista de las etiquetas encontradas que cumplan los requisitos que hemos impuesto.

El siguiente paso que tomamos es la de formatear el código que nos puede traer la consulta, todo ello para que quede bien indentado y bonito. Aqui hacemos uso de una librería de JavaScript llamada "PrettyFy".

Y por ultimo pasamos la respuesta del servidor al front. En caso de que no exisitiese dicha respuesta por parte de alguna de las webs, se mostraria un mensaje comunicandole al usuario que no existe dicha consulta.

Parte Importante del desarrollo son las **Templates**. Es una carpeta creada por el desarrollador dentro de Django que te permite establecer plantillas para modularizar el código HTML de la web.

![templates](https://github.com/AntonioMendezRuiz/Proyecto_DAW/blob/master/img/templates.png)

Estas son las diferentes templates que he creado para el proyecto.

- **Index**:

![index](https://github.com/AntonioMendezRuiz/Proyecto_DAW/blob/master/img/index.png)

- **Respuestas**:

![respuestas](https://github.com/AntonioMendezRuiz/Proyecto_DAW/blob/master/img/respuestas.png)

- **Header**:

![header](https://github.com/AntonioMendezRuiz/Proyecto_DAW/blob/master/img/header.png)

- **Footer**:

![footer](https://github.com/AntonioMendezRuiz/Proyecto_DAW/blob/master/img/footer.png)

- **Form**:

![form](https://github.com/AntonioMendezRuiz/Proyecto_DAW/blob/master/img/form.png)

## 5. Problemas encontrados

Los problemas encontrados no han sido pocos, desde problemas con windows a la hora de intentar portar el proyecto entre mis propios PCs, hasta problemas con las librerías externas por no entender muy bien su funcionamiento.

El problema con windows es sencillo pero dificil de solucionar, o mas bien caro, dado que un windows que no tenga clave de verificacion, es decir, que no tenga licencia, no puede ejectuar maquinas virtuales y por tanto Django no funciona en él.

Uno de los quebraderos de cabeza más grandes que he tenido durante el proyecto no ha sido otro que el formato de la respuesta que quiero mostrar al usuario. El por qué de esto es debido a que dependemos de información del exterior y esto hace que la cantidad de posibles combinaciones de formatos que podamos recibir sea inabarcable. He intentado cubrir el mayor número de ellas que he podido pero nada asegura que en futuras búsquedas pueda venir algo "feo" que no pueda tratar mi programa, por lo que uno de los siguentes pasos sería el testeo masivo de consultas y ver que tipo de excepciones podemos encontrar.

No obstante detallaré alguno de ellos con los que más me he "peleado".

- Problemas con el código de la web "LaWebDelProgramador": Esta web es un poco "rebelde" dado que no solo es un foro sino que también contiene artículos cuyo formato es diferente al de una consulta. ¿El problema? que si solo nos centramos en las consultas, estas también tiene formatos distintos por algun criterio que no llego a entender. No he encontrado ningún patrón que me haga poder discernir entre los diferentes formatos de la web, cosa que hace muy dificil trabajar con ella. Pensé en cambiar de web dado que me estaba llevando mucho tiempo pero ya era demasiado tarde.

 - Problemas con las views de Django: Este problema fue un quebradero de cabeza al principio y me llevo tiempo solucionar porque aún no entiendia muy bien como funcionaba Django. Basicamente no sabía como establecer las diferentes views y poder acceder a ellas sin tener un menú, es decir, cambiar de views al hacer una búsqueda.

   

## 6.Posibles mejoras y siguientes pasos

Este apartado es un poco subjetivo pero hay algunas mejoras que están claras y que atañen al funcionamiento directo de la aplicación. La principal de ellas es continuar con el testeo y descubrir todos los posibles formatos de páginas que puede llegar y controlarlos todos. Esto más que dificil es laborioso y largo.

Tenia planeado, de haber tenido más tiempo o no haber estado en las prácticas, haber implementado algunas cosas más como:

- Realizar un loco acorde con la temática de la web.
- Haber introducido una o dos webs más donde realizar las búsquedas. El problema de este apartado no es otro que eso hubiera multiplicado el trabajo x4 al tener que hacer todo lo que he detallado al menos dos veces más en el mejor de los casos y sin contar con complicaciones derivadas de estas webs.
- Enlaces directos a las webs donde están las consultas. Esto, básicamente, ha sido por falta de tiempo.
- Bot de twitter. Estuve un par de días mirando como hacer un bot te twitter el cual cuando se realizara una búsqueda la twitteara. Lo dejé para el final y por falta de tiempo no se ha podido hacer.

Todo esto anterior se pueden considerar próximos pasos para las releases y además se aceptan sugerencias.

Dentro del proyecto hay un archivo el cual se denomina "changelog" en el cual se detallan las releases que hemos tenido hasta fecha de hoy y los posibles cambios venideros.

![changelog](https://github.com/AntonioMendezRuiz/Proyecto_DAW/blob/master/img/changelog.png)

## 7. Bibliografía

A parte de los métodos convencionales de ayuda tales como StackOverFlow, GitHub, W3School,... la bibliografía usada es extensa e interesante.

He adjuntado una carpeta al proyecto llamada "Bibliografía" la cual recopila los libros que me han servido para la realización del proyecto. Son los siguientes:

- *Aidas Bendoraitis, Jake Kronika - Django 3 Web Development Cookbook_ Actionable solutions to common problems in Python web development-Packt Publishing (2020*
- *Daniel Roy Greenfield, Audrey Roy Greenfield - Django Crash Course (2020)*
- *La guía definitiva de Django*
- *Ryan Mitchell - Web Scraping with Python_ Collecting Data from the Modern Web-O'Reilly Media (2015)*

