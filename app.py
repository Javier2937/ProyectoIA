from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_cors import CORS  
from modelos.modeloT5 import resumir_texto
from modelos.modeloTraductor import traducir_texto
from modelos.modeloPreguntaGenerativa import responder_pregunta
from modelos.modeloGenerarPreguntas import generar_pregunta


app = Flask(__name__)
CORS(app)  


@app.route('/')
def index():
    return render_template('loading.html')

@app.route('/obtenerResumen', methods=['POST'])
def resumenT5():
    data = request.get_json()
    texto = data.get('texto')
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
    traduccion = traducir_texto(texto)
    return jsonify({'traduccion': traduccion})

@app.route('/pregunta', methods=['POST'])
def responder():
    data = request.get_json()
    pregunta = data.get('texto')

    if not pregunta:
        return jsonify({'error': 'No se envió ninguna pregunta'}), 400

    try:
        print("Pregunta recibida:", pregunta)
        respuesta = responder_pregunta(pregunta)
        print("Respuesta generada:", respuesta)
        return jsonify({'resultado': respuesta})
    except Exception as e:
        print("ERROR:", e)
        return jsonify({'error': str(e)}), 500

@app.route('/generar_pregunta', methods=['POST'])
def generar():
    data = request.get_json()
    texto = data.get('texto')

    if not texto:
        return jsonify({'error': 'No se envió texto'}), 400

    try:
        preguntas = generar_pregunta(texto)
        return jsonify({'resultado': "\n".join(preguntas)})
    except Exception as e:
        print("ERROR:", e)
        return jsonify({'error': str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True)

