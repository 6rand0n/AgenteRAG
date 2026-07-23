from app.rag import responder

while True:

    pregunta = input("\nPregunta: ")

    if pregunta.lower() == "salir":
        break

    respuesta = responder(pregunta)

    print("\nRespuesta:\n")
    print(respuesta)