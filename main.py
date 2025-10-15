from fastapi import FastAPI
from src.routers import root
from src.routers import contatos

app = FastAPI(
    title="Mini CRM API",
    description="Uma API simples para gerenciar contatos.",
    version="0.4.0"
)

app.include_router(root.router)
app.include_router(contatos.router)