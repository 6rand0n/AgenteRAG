from pydantic import BaseModel


class PreguntaRequest(BaseModel):
    pregunta: str


class PreguntaResponse(BaseModel):
    respuesta: str
    fuentes: list[int]