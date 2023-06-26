$(document).ready(function() {
    $("#addValue").click(function() {
      var valor = $("#inputValue").val();
      var elemento = $("<li>").text(valor);
      elemento.click(function() {
        $(this).remove();
      });
      $("#valores").append(elemento);
    });
  });