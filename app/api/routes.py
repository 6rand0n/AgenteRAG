from fastapi import APIRouter

from app.models.schemas import (
    PreguntaRequest,
    PreguntaResponse
)

from app.services.rag_service import RAG

router = APIRouter()

rag = RAG()


@router.get("/")
def inicio():

    return {
        "mensaje": "Agente RRHH funcionando."
    }


@router.post(
    "/preguntar",
    response_model=PreguntaResponse
)
def preguntar(datos: PreguntaRequest):

    return rag.preguntar(datos.pregunta)