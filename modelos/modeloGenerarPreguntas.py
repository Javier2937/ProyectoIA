from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

nombre_modelo = "iarfmoose/t5-base-question-generator"
tokenizer = AutoTokenizer.from_pretrained(nombre_modelo)
modelo = AutoModelForSeq2SeqLM.from_pretrained(nombre_modelo)

def generar_pregunta(texto):
    entrada = "generate questions: " + texto.strip()
    entrada_tokenizada = tokenizer(entrada, return_tensors="pt", truncation=True, max_length=512)
    salida = modelo.generate(**entrada_tokenizada, max_length=128, num_return_sequences=3, num_beams=5)
    preguntas = [tokenizer.decode(q, skip_special_tokens=True) for q in salida]
    return preguntas
