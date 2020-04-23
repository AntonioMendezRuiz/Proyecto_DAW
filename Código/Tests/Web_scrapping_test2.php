<?php
    //Esta libreria nos permite acceder a las etiquetas HTML 
    require 'simple_html_dom.php';

    //Obtenemos la busqueda del usuario
    $busqueda = $_POST["busqueda"];

    if(!empty($busqueda)){
        $sentencia = "http://www.google.com.co/search?hl=es&q=".$busqueda."stackoverflow&btnG=Buscar&meta=";
        
        //Realizamos primera busqueda en google
        $google = file_get_html($sentencia);

        //Accedemos a las etiquetas para obtener la url
        $contenedor = $google->find('div[class="kCrYT"]', 0);
        $cadena = $contenedor->find("a",0)->href;
        $url = substr($cadena, 7);

        //Accedemos a la web que deseamos y buscamos las etiquetas
        $html = file_get_html($url);
        $question = $html->find("div[class='post-text']", 0);
        $answer = $html->find("div[class='post-text']", 1);

        echo $question;
        echo $answer;

        //Enviamos en formato JSON la pregunta y la respuesta
        //$respuesta = array('pregunta' => $question, 'respuesta' => $answer);
        
        //echo json_encode($respuesta);
       
    }else{
        echo "Por favor introduzca una búsqueda";
    }
?>