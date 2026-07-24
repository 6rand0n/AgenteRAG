from app.services.rag_service import RAG

rag = RAG()

while True:

    pregunta = input("\nPregunta: ")

    if pregunta.lower() == "salir":
        break

    print()

    resultado = rag.preguntar(pregunta)

    print("\nRespuesta:\n")
    print(resultado["respuesta"])
    
    print("\nFuentes:")
    for pagina in resultado["fuentes"]:
        print(f"- Página {pagina}")