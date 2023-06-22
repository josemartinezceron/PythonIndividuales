let luzVerde = document.getElementById("verde");
let luzAmarilla = document.getElementById("amarillo");
let luzRoja = document.getElementById("rojo");
 function encenderLuz(luz) {
  luz.style.backgroundColor = luz.id;
}
 function apagarLuz(luz) {
  luz.style.backgroundColor = "gray";
}
 function cambiarSemaforo() {
  setTimeout(function() {
    apagarLuz(luzVerde);
    encenderLuz(luzAmarilla);
    setTimeout(function() {
      apagarLuz(luzAmarilla);
      encenderLuz(luzRoja);
      setTimeout(function() {
        apagarLuz(luzRoja);
        encenderLuz(luzVerde);
        cambiarSemaforo();
      }, 3000);
    }, 1000);
  }, 3000);
}
function moverMouse(event) {
let distanciaX = Math.abs(event.clientX - (window.innerWidth / 2));
let distanciaY = Math.abs(event.clientY - (window.innerHeight / 2));
let distancia = Math.sqrt(distanciaX * distanciaX + distanciaY * distanciaY);
if (distancia > 200) {
  cambiarSemaforo();
} else if (distancia > 150 && distancia <= 200) {
  apagarLuz(luzVerde);
  apagarLuz(luzRoja);
  encenderLuz(luzAmarilla);
} else {
  apagarLuz(luzVerde);
  apagarLuz(luzAmarilla);
  encenderLuz(luzRoja);
}
}
cambiarSemaforo();