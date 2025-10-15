from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

class Contato(BaseModel):
    id: Optional[int] = None
    nome: str
    email: str
    telefone: Optional[str] = None
    empresa: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "nome": "Alice Silva",
                "email": "alice.silva@exemplo.com",
                "telefone": "5511987654321",
                "empresa": "Tech Solutions Ltda"
            }
        }

app = FastAPI(
    title="Mini CRM API",
    description="Uma API simples para gerenciar contatos.",
    version="0.2.0"
)

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Bem-vindo à API do Mini CRM"}