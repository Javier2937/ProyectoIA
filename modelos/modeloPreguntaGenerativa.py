from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

modelo_nombre = "google/flan-t5-base"

tokenizer = AutoTokenizer.from_pretrained(modelo_nombre)
modelo = AutoModelForSeq2SeqLM.from_pretrained(modelo_nombre)

def responder_pregunta(pregunta):
    entrada = tokenizer(pregunta, return_tensors="pt")
    salida = modelo.generate(**entrada, max_length=100)
    respuesta = tokenizer.decode(salida[0], skip_special_tokens=True)
    return respuesta
print("Modelo FLAN T5 cargado correctamente.")

