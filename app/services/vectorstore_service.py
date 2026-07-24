from pathlib import Path

from langchain_cohere import CohereEmbeddings
from langchain_community.vectorstores import FAISS

from app.core.config import (
    COHERE_API_KEY,
    VECTOR_DB_PATH,
    EMBEDDING_MODEL
)

from app.services.document_loader import DocumentLoader


class VectorStoreService:

    def __init__(self):

        self.embeddings = CohereEmbeddings(
            model=EMBEDDING_MODEL,
            cohere_api_key=COHERE_API_KEY
        )

    def crear(self):

        loader = DocumentLoader()

        documentos = loader.cargar()

        chunks = loader.dividir(documentos)

        vectorstore = FAISS.from_documents(
            chunks,
            self.embeddings
        )

        Path(VECTOR_DB_PATH).mkdir(exist_ok=True)

        vectorstore.save_local(VECTOR_DB_PATH)

    def cargar(self):

        return FAISS.load_local(
            VECTOR_DB_PATH,
            self.embeddings,
            allow_dangerous_deserialization=True
        )