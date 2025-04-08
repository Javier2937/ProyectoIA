from transformers import MarianMTModel, MarianTokenizer

# Modelo para traducir de inglés a español
modelo_nombre = 'Helsinki-NLP/opus-mt-en-es'

# Cargar el modelo y el tokenizer
tokenizer = MarianTokenizer.from_pretrained(modelo_nombre)
model = MarianMTModel.from_pretrained(modelo_nombre)

def traducir_texto(texto):

    texto_original = texto

    # Codificar entrada (usando tokenizer moderno)
    tokens = tokenizer([texto_original], return_tensors='pt', padding=True)

    # Generar traducción
    traduccion = model.generate(**tokens)

    # Decodificar resultado
    texto_traducido = tokenizer.decode(traduccion[0], skip_special_tokens=True)
    
    return texto_traducido
