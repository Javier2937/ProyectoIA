from flask import Flask, render_template, request, redirect, url_for, jsonify
from modelos.modeloT5 import resumir_texto
from modelos.modeloTraductor import traducir_texto
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('loading.html')


@app.route('/obtenerResumen', methods=['POST'])
def resumenT5():
    data = request.get_json()
    texto = data.get('texto')

    # mensaje = f"Este mensaje fue recibido y procesado por fetch y servidor flask {texto}"

    if not texto:
        return jsonify({'error': 'No se envió ningún texto'}), 400

    resumen = resumir_texto(texto)

    return jsonify({'resumen': resumen })


@app.route('/traducirTexto', methods=['POST'])
def traducir():
    data = request.get_json()
    texto = data.get('textoTraducir')

    if not texto:
        return jsonify({'error': 'No se envio ningun texto'}), 400

    traduccion =  traducir_texto(texto)

    return jsonify({'traduccion': traduccion})


if __name__ == '__main__':
    app.run(debug=True)