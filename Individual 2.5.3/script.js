const $lucesDelCirculo = document.querySelectorAll('.luces-circulo');
let contadorDeLuz = 0;

const mostrarLuz = () =>{
    $lucesDelCirculo[contadorDeLuz].className = 'luces-circulo';
    contadorDeLuz++;

    if(contadorDeLuz > 2) contadorDeLuz = 0;
    const luzActual = $lucesDelCirculo[contadorDeLuz];
     luzActual.classList.add(luzActual.getAttribute('color'))
}
setInterval(mostrarLuz,2000)

const semaforo = document.querySelector('.semaforo');

const cambiarLuces = (event) => {
  const distanciaX = Math.abs(event.clientX - semaforo.offsetLeft - semaforo.offsetWidth / 2);
  const distanciaY = Math.abs(event.clientY - semaforo.offsetTop - semaforo.offsetHeight / 2);
  const distancia = Math.sqrt(distanciaX ** 2 + distanciaY ** 2);

  if (distancia > 20) {
    // Operar según lo descrito en el punto 3
    mostrarLuz();
  } else if (distancia >= 15 && distancia <= 200) {
    // Activar luz amarilla fijamente
    $lucesDelCirculo[0].className = 'luces-circulo';
    $lucesDelCirculo[1].className = 'luces-circulo';
    $lucesDelCirculo[2].className = 'luces-circulo yellow';
  } else if (distancia < 15) {
    // Activar luz roja fijamente
    $lucesDelCirculo[0].className = 'luces-circulo red';
    $lucesDelCirculo[1].className = 'luces-circulo';
    $lucesDelCirculo[2].className = 'luces-circulo';
  }
};

document.addEventListener('mousemove', cambiarLuces);