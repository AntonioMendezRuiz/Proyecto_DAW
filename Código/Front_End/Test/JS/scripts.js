var busqueda = () => {
    let resultado = document.getElementById("resultado");
    //let divPregunta = document.getElementById("pregunta");
    let xhttp = new XMLHttpRequest();
    var entrada =  document.getElementById("busqueda").value;
    var stackoverflow = document.getElementById("primero");
    var webProgramador = document.getElementById("segundo");
    var res = entrada.replace(/ /g, "")
    
    if(stackoverflow.checked){
        stackoverflow.value = 1;
    }
    else{
        stackoverflow.value  = 0;
    }
    if(webProgramador.checked){
        webProgramador.value = 1;
    }
    else{
        webProgramador.value  = 0;
    }
    xhttp.onreadystatechange = function () {
        if (xhttp.readyState == 4 && xhttp.status == 200) {
            var respuestas = xhttp.responseText;
            resultado.innerHTML = respuestas;
            console.log(xhttp.responseText)
        }
    }
    xhttp.open("POST", "../../../Back_End/Main_Code/Web_Scrapping.php", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send("busqueda=" + res + "&stackoverflow=" + stackoverflow.value + "&lawebprogramador=" + webProgramador.value);
}

var borrar = () =>{
    document.getElementById("resultado").innerHTML = "";
    document.getElementById("busqueda").value = "";
}