function mostrarTexto() {
    let input = document.getElementById("inputTexto").value;
    let texto = input.replace(/[0-9]/g, ''); // elimina números
    texto = texto.charAt(0).toUpperCase() + texto.slice(1, -1) + texto.slice(-1).toUpperCase(); // primera y última letra en mayúscula
    document.getElementById("textoMostrado").innerHTML = texto;
    document.getElementById("textoMostrado").style.color = "blue";
    document.getElementById("textoMostrado").style.fontSize = "25px";
  }