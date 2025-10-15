from fastapi import FastAPI
from src.routers import contatos
from src.routers import health
from src.routers import admin
from src.core.logging import logger
from src.middleware.request_id import RequestIDMiddleware
from src.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Uma API simples para gerenciar contatos.",
    version=settings.VERSION
)

app.add_middleware(RequestIDMiddleware)

app.include_router(health.router) 
app.include_router(contatos.router) 
app.include_router(admin.router)

logger.info(f"Aplicação FastAPI inicializada e routers carregados. Versão {settings.VERSION}.")