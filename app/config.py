import os

from dotenv import load_dotenv

load_dotenv()

COHERE_API_KEY = os.getenv("COHERE_API_KEY")

PDF_PATH = "documentos/reglamentoDeTrabajo_FicticiaDeMexicoCV.pdf"

VECTOR_DB_PATH = "vectorstore"