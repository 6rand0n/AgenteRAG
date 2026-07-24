import os
from dotenv import load_dotenv

load_dotenv()

COHERE_API_KEY = os.getenv("COHERE_API_KEY")

PDF_PATH = "documentos/reglamentoDeTrabajo_FicticiaDeMexicoCV.pdf"
VECTOR_DB_PATH = "vectorstore"

EMBEDDING_MODEL = "embed-v4.0"
CHAT_MODEL = "command-a-03-2025"

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
RETRIEVER_K = 4