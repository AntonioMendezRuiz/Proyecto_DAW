# Descripción del proyecto.
En el presente proyecto se pretende desarrollar una aplicación web que realice la función de un comparador. En este caso, el objeto 
de comparación serán las respuestas ofrecidas a una pregunta lanzada por un potencial usuario relacionada con programación. Dudas 
de dependencia, de errores en código, de cómo hacer o crear un programa que cumpla una determinada función, etc. Este proyecto 
pretende ser ademas el trabajo final de Antonio Méndez Ruíz, por lo que es posible que existan varias releases, en función del 
alcance de una y otra parte.

## Objetivos.
El objetivo principal del software es crear un comparador de busquedas sobre programación el cual facilite la labor del programador 
a la hora de realizar sus consultas. La intención es que dichas busquedas aparezcan de una forma ordenada y clara en pantalla para que el usuario, de un solo vistazo, pueda ver cual se ajusta más a su duda y por tanto resolverla.

## Arquitectura.

### Módulos.
En esta sección se describen los módulos que van a constituir el software a desarrollar. Debido a la naturaleza del proyecto, la estructura de dichos módulos puede cambiar, por lo que esto es un texto vivo. Además de su arquitectura, también debería especificarse el lenguage de programación en el que están siendo desarrollados dichos módulos. 

* Front-End: Descripción inicial(no solo a nivel de funcionalidades si no a nivel de UI/UX) ?
* Back-End: Descripción superficial. Contenedores, etc.
* Web Scrapper: Dicho módulo es el elemento principal en la búsqueda y recabado de la información solicitada por el usuario. En base a la pregunta lanzada por éste, el módulo WS (Web-Scrapper) debe reenviar la petición, (quizás, fortalecida con información extra provista por los filtros añadidos por el usuario), recorrer diversas páginas de interés donde existan potenciales respuestas, y recuperar esa información. El presente módulo debe ser llamado mediante un servicio específico y deberá devolver un tipo de dato estructurado (posiblemente JSON). Dicho módulo será desarrollado en Python, y la idea inicial es que se monte la algoritmia pertinente en un servidor de Flask, pero aún no se ha decidido.
