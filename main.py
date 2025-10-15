from fastapi import FastAPI
from src.routers import contatos
from src.routers import health

app = FastAPI(
    title="Mini CRM API",
    description="Uma API simples para gerenciar contatos.",
    version="0.5.0"
)

app.include_router(health.router) 

app.include_router(contatos.router)