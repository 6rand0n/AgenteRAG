from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.routes import router

app = FastAPI(
    title="Agente RRHH",
    version="1.0.0"
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(router)