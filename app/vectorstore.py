from pathlib import Path

from langchain_cohere import CohereEmbeddings
from langchain_community.vectorstores import FAISS

from app.config import COHERE_API_KEY, VECTOR_DB_PATH
from app.loader import cargar_documentos, dividir_documentos


def crear_vectorstore():

    documentos = cargar_documentos()

    chunks = dividir_documentos(documentos)

    embeddings = CohereEmbeddings(
        model="embed-v4.0",
        cohere_api_key=COHERE_API_KEY
    )

    vectorstore = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    Path(VECTOR_DB_PATH).mkdir(exist_ok=True)

    vectorstore.save_local(VECTOR_DB_PATH)

    print("✅ Índice creado correctamente.")


def cargar_vectorstore():

    embeddings = CohereEmbeddings(
        model="embed-v4.0",
        cohere_api_key=COHERE_API_KEY
    )

    return FAISS.load_local(
        VECTOR_DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )