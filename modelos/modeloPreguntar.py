from transformers import pipeline

# Carga del pipeline de preguntas y respuestas
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

def responder_pregunta(pregunta, contexto):
    resultado = qa_pipeline(question=pregunta, context=contexto)
    return resultado["answer"]
