from fastapi import FastAPI
from src.routers import root

app = FastAPI(
    title="Mini CRM API",
    description="Uma API simples para gerenciar contatos.",
    version="0.3.0",
)

app.include_router(root.router)
