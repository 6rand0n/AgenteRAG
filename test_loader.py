from app.loader import cargar_documentos
from app.loader import dividir_documentos

docs = cargar_documentos()

print(f"Páginas: {len(docs)}")

chunks = dividir_documentos(docs)

print(f"Chunks: {len(chunks)}")

print()

print(chunks[0].page_content)