function agregarValor() {
    var valor = document.getElementById("inputValue").value;
    var lista = document.getElementById("valores");
    var elemento = document.createElement("li");
    elemento.appendChild(document.createTextNode(valor));
    elemento.onclick = function() {
      this.parentNode.removeChild(this);
    };
    lista.appendChild(elemento);
  }