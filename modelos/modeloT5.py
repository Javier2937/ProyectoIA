from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Cargamos el modelo solo una vez al inicio
nombre_modelo = "t5-base"
tokenizer = AutoTokenizer.from_pretrained(nombre_modelo)
modelo = AutoModelForSeq2SeqLM.from_pretrained(nombre_modelo)

def resumir_texto(texto):
    texto = "summarize: " + texto
    vectores_entrada = tokenizer.encode(texto, return_tensors="pt", max_length=1024, truncation=True)
    vectores_salida = modelo.generate(
        vectores_entrada,
        max_length=1024,
        min_length=10,
        length_penalty=2.0,
        num_beams=4,
        early_stopping=True
    )
    resumen = tokenizer.decode(vectores_salida[0], skip_special_tokens=True)
    return resumen
