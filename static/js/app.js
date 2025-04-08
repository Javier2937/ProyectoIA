function resumenT5(event) {
    event.preventDefault();

    const texto = document.querySelector('#textoT5').value;
    const resultado = document.querySelector("#resumenT5");
    const spinner = document.getElementById("spinner");

    spinner.style.display = "block";  // Muestra spinner
    resultado.textContent = "";        // Limpia resultado anterior

    fetch('/obtenerResumen', {
        method:  'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ texto: texto })
    })
    .then(response => response.json() )
    .then(data => {
        spinner.style.display = "none";  // Oculta spinner

                if (data.resumen) {
                    resultado.textContent = data.resumen;
                } else {
                    resultado.textContent = "Error: " + data.error;
                }
        console.log(data.mensaje);
    })
    .catch(error => {
        console.log("Error: " , error)
    });

    //
    console.log(texto);
}

function traducirTexto(event) {

    event.preventDefault();

    const texto = document.querySelector('#textoTraducir').value;
    console.log(texto)
    const resultado = document.querySelector("#resultadoTraducir");
    const spinner = document.getElementById("spinnerTraducir");

    spinner.style.display = "block";  // Muestra spinner
    resultado.textContent = "";        // Limpia resultado anterior

    fetch('/traducirTexto', {
        method:  'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ textoTraducir: texto })
    })
    .then(response => response.json() )
    .then(data => {
        spinner.style.display = "none";  // Oculta spinner

                if (data.traduccion) {
                    resultado.textContent = data.traduccion;
                } else {
                    resultado.textContent = "Error: " + data.error;
                }
        console.log(data.mensaje);
    })
    .catch(error => {
        console.log("Error: " , error)
    });

    //
    console.log(texto);
}
function enviarTexto(tipo) {
  const input = document.getElementById(`${tipo}Input`).value;
  if (!input.trim()) {
    alert("Por favor escribe algo primero.");
    return;
  }

  fetch(`http://localhost:5000/${tipo}`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ texto: input })  // 👈 asegúrate que se llama "texto"
  })
    .then(res => res.json())
    .then(data => {

        
      document.getElementById(`${tipo}Output`).innerText = data.resultado;
    })
    .catch(err => {
      console.error(err);  // 👈 Aquí se imprime el error del fetch
      document.getElementById(`${tipo}Output`).innerText = "Error al procesar la solicitud.";
    });
}
