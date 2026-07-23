from langchain_community.document_loaders import PyPDFLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.config import PDF_PATH

def cargar_documentos():

    loader = PyPDFLoader(PDF_PATH)

    documentos = loader.load()

    return documentos


def dividir_documentos(documentos):

    splitter = RecursiveCharacterTextSplitter(

        chunk_size=1000,

        chunk_overlap=200

    )

    return splitter.split_documents(documentos)