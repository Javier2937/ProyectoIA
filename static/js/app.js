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