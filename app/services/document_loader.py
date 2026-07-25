from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.core.config import (
    PDF_PATH,
    CHUNK_SIZE,
    CHUNK_OVERLAP
)


class DocumentLoader:

    def cargar(self):

        loader = PyPDFLoader(PDF_PATH)

        return loader.load()

    def dividir(self, documentos):

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP
        )

        return splitter.split_documents(documentos)