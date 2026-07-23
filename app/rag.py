from langchain_cohere import ChatCohere
from langchain_core.prompts import ChatPromptTemplate

from app.config import COHERE_API_KEY
from app.vectorstore import cargar_vectorstore


# Prompt del sistema
PROMPT = """
Eres un asistente de Recursos Humanos.

Responde únicamente utilizando la información del contexto.

Si la respuesta no aparece en el contexto responde exactamente:

"No encontré esa información en el reglamento."

Contexto:
{context}

Pregunta:
{question}
"""

prompt = ChatPromptTemplate.from_template(PROMPT)


def responder(pregunta: str):

    vectorstore = cargar_vectorstore()

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 4}
    )

    documentos = retriever.invoke(pregunta)

    contexto = "\n\n".join(
        doc.page_content
        for doc in documentos
    )

    llm = ChatCohere(
        model="command-a-03-2025",
        cohere_api_key=COHERE_API_KEY,
        temperature=0
    )

    chain = prompt | llm

    respuesta = chain.invoke(
        {
            "context": contexto,
            "question": pregunta
        }
    )

    return respuesta.content