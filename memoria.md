# CodePass

Realizado por: Antonio Méndez Ruiz

Tutor: Paco Ávila

Curso: 2019/20



- Índice

1. Descripción e introducción
2. Objetivos
3. Arquitectura
4. Realización del Proyecto
5. Problemas encontrados
6. Posibles mejoras y próximos pasos
7. Bibliografía



## 1. Descripción del proyecto.

En el presente proyecto se pretende desarrollar una aplicación web que realice la función de un comparador. En este caso, el objeto de comparación serán las respuestas ofrecidas a una pregunta lanzada por un potencial usuario relacionada con programación. Dudas de dependencia, de errores en código, de cómo hacer o crear un programa que cumpla una determinada función, etc. Este proyecto pretende ser además el trabajo final de Antonio Méndez Ruiz, por lo que es posible que existan varias releases, en función del alcance de una y otra parte.

## 2. Objetivos.

El objetivo principal del software es crear un comparador de búsquedas sobre programación el cual facilite la labor del programador a la hora de realizar sus consultas. La intención es que dichas búsquedas aparezcan de una forma ordenada y clara en pantalla para que el usuario, de un solo vistazo, pueda ver cual se ajusta más a su duda y por tanto resolverla.

## 3. Arquitectura.

Para la arquitectura del proyecto usaremos Django con la ayuda de algunas librerías de JavaScript como "Prettyfy" el cual sirve para el formateo de códigos en la web.

### Módulos.

En esta sección se describen los módulos que van a constituir el software a desarrollar. Debido a la naturaleza del proyecto, la estructura de dichos módulos puede cambiar, por lo que esto es un texto vivo. Además de su arquitectura, también debería especificarse el lenguaje de programación en el que están siendo desarrollados dichos módulos.

- Front-End: El front se basará estrictamente en HTML y CSS a través de la utilización de plantillas que ofrece Django. Dichas plantillas se modularizarán de forma que cada componente (Véase el footer, header o el body) sean independientes y se puedan usar en cada una de las páginas de la web. Es posible la implementación de JavaScript.

  

- Back-End: El back será desarrollado en su totalidad en Python con las herramientas de las que nos provee Django y alguna librería adicional para realizar las funciones de web scrapping, que es en lo que se basará el proyecto.

  

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

En este apartado detallaremos como ha sido el desarrollo de la aplicación y qué hemos usado para la realización del mismo. Comenzaremos con Django y sus peculiaridades.

![1_HVKOLLX7wprRbHTl2IPDcQ](C:\Users\mende\Desktop\Proyecto_DAW\img\1_HVKOLLX7wprRbHTl2IPDcQ.png)

