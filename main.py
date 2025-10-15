from fastapi import FastAPI
from src.routers import contatos
from src.routers import health
from src.core.logging import logger
from src.middleware.request_id import RequestIDMiddleware

app = FastAPI(
    title="Mini CRM API",
    description="Uma API simples para gerenciar contatos.",
    version="0.6.0" 
)

app.add_middleware(RequestIDMiddleware)

app.include_router(health.router) 
app.include_router(contatos.router) 

logger.info("Aplicação FastAPI inicializada e routers carregados. Versão 0.6.0.")