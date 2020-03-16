<?php
header('Content-Type: application/json');
require 'simple_html_dom.php';

$stackCheck = $_POST["stackoverflow"];
$webProgramadorCheck = $_POST["lawebprogramador"];
$busqueda = $_POST["busqueda"];

function web_scrapper($check1, $Check2){
    $busqueda = $_POST["busqueda"];
    $stackoverflow = "http://www.google.com.co/search?hl=es&q=".$busqueda."stackoverflow&btnG=Buscar&meta=";
    $webProgramador = "http://www.google.com.co/search?hl=es&q=".$busqueda."lawebdelprogramador&btnG=Buscar&meta=";
    $iterador = 0;
    if($check1 == 1){
        //Realizamos primera busqueda en google
        $google = file_get_html($stackoverflow);

        //Accedemos a las etiquetas para obtener la url
        $contenedor = $google->find('div[class="kCrYT"]', 0);
        $cadena = $contenedor->find("a",0)->href;
        $url = substr($cadena, 7);

        //Accedemos a la web que deseamos y buscamos las etiquetas
        $html = file_get_html($url);
        $question = $html->find("div[class='post-text']", 0);
        $answer = $html->find("div[class='post-text']", 1);

        //Escapamos comillas para que no de error
        $questionClean1 = str_replace('"', '\"', $question);
        $answerClean1 = str_replace('"', '\"', $answer);

        //$questionClean2 = str_replace('<code>&lt;', '<code class =\"prettyprint\">', $questionClean1);
        //$answerClean2 = str_replace('<code>&lt;', '<code class =\"prettyprint\">', $answerClean1);

        //$questionClean3 = str_replace('&lt;</code>', '</code>', $questionClean2);
        //$answerClean3 = str_replace('&lt;</code>', '</code>', $answerClean2);

        $questionClean2 = str_replace('<code>', '<pre class =\"prettyprint\"><xmp>', $questionClean1);
        $answerClean2 = str_replace('<code>', '<pre class =\"prettyprint\"><xmp>', $answerClean1);

        $questionClean3 = str_replace('</code>', '</xmp></pre>', $questionClean2);
        $answerClean3 = str_replace('</code>', '</xmp></pre>', $answerClean2);
    }
    if($Check2 == 1){
        //Realizamos primera busqueda en google
        $google2 = file_get_html($webProgramador);

        //Accedemos a las etiquetas para obtener la url
        $contenedor2 = $google2->find('div[class="kCrYT"]', 0);
        $cadena2 = $contenedor2->find("a",0)->href;
        $url2 = substr($cadena2, 7);
        $urlFinal = explode('&', $url2);
        //Accedemos a la web que deseamos y buscamos las etiquetas
        $html2 = file_get_html($urlFinal[0]);
        //echo $html2;
        $questionWebProgramador = $html2->find('div[class="ml0"]', 0);
        $answerWebProgramador = $html2->find('div[class="ml10"]', 0);

        //Escapamos comillas para que no de error
        $questionWebClean = str_replace('"', '\"', $questionWebProgramador);
        $answerWebClean = str_replace('"', '\"', $answerWebProgramador);
    }
    //Creamos un archivo JSON para pasar los datos dado que la memoria del server puede no se suficiente para albergar los datos
    $fp = fopen("datos.json", "w");
    fwrite($fp,'[{"preguntaStack":' . '"' . $questionClean3 . '"' . ',"respuestaStack":'. '"' . $answerClean3 . '"' . '}, {"preguntaWeb":' . '"' . $questionWebClean . '"' . ',"respuestaWeb":'. '"' . $answerWebClean . '"' . '}]');
    fclose($fp);
}




if(!empty($busqueda)){
    web_scrapper($stackCheck, $webProgramadorCheck);
}else{
    echo "Por favor introduzca una búsqueda";
}

?>