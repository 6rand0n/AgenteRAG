from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.models.schemas import (
    PreguntaRequest,
    PreguntaResponse
)

from app.services.rag_service import RAG

templates = Jinja2Templates(directory="app/templates")
router = APIRouter()
rag = RAG()


@router.get("/", response_class=HTMLResponse)
def inicio(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

@router.post(
    "/preguntar",
    response_model=PreguntaResponse
)
def preguntar(datos: PreguntaRequest):

    return rag.preguntar(datos.pregunta)