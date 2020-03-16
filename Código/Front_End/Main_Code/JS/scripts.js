var busqueda = () => {
    let resultado = document.getElementById("resultado");
    //let divPregunta = document.getElementById("pregunta");
    let xhttp = new XMLHttpRequest();
    var entrada =  document.getElementById("busqueda").value;
    var res = entrada.replace(/ /g, "")
    //var google = "http://www.google.com.co/search?hl=es&q=" + res + "+stackoverflow&btnG=Buscar&meta=";
    xhttp.onreadystatechange = function () {
        if (xhttp.readyState == 4 && xhttp.status == 200) {
            var respuestas = xhttp.responseText;
            resultado.innerHTML = respuestas;
        }
    }
    xhttp.open("POST", "../../../Web_Scrapper/Test/Web_scrapping_test2.php", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send("busqueda=" + res);
}

var borrar = () =>{
    document.getElementById("resultado").innerHTML = "";
    document.getElementById("busqueda").value = "";
}