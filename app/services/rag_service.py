from langchain_cohere import ChatCohere
from langchain_core.prompts import ChatPromptTemplate

from app.core.prompts import PROMPT_RRHH
from app.services.vectorstore_service import VectorStoreService
from app.core.config import COHERE_API_KEY


class RAG:

    def __init__(self):

        manager = VectorStoreService()

        self.vectorstore = manager.cargar()

        self.retriever = self.vectorstore.as_retriever(
            search_kwargs={"k": 4}
        )

        self.llm = ChatCohere(
            model="command-a-03-2025",
            temperature=0,
            cohere_api_key=COHERE_API_KEY
        )

        self.prompt = ChatPromptTemplate.from_template(PROMPT_RRHH)

        self.chain = self.prompt | self.llm

    def preguntar(self, pregunta: str):

        # Buscar los fragmentos más relevantes
        documentos = self.retriever.invoke(pregunta)

        # Construir el contexto
        contexto = ""

        for i, doc in enumerate(documentos, start=1):
            pagina = doc.metadata.get("page", "desconocida")

            if pagina != "desconocida":
                pagina += 1

            contexto += (
                f"Fragmento {i} (Página {pagina})\n"
                f"{doc.page_content}\n\n"
            )

        # Obtener páginas únicas utilizadas
        fuentes = sorted({
            doc.metadata["page"] + 1
            for doc in documentos
            if "page" in doc.metadata
        })

        # Llamar al modelo
        respuesta = self.chain.invoke({
            "context": contexto,
            "question": pregunta
        })

        return {
            "respuesta": respuesta.content,
            "fuentes": fuentes
        }