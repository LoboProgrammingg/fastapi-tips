from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Contato(BaseModel):
    id: Optional[int] = None
    nome: str
    email: str
    telefone: Optional[str] = None
    empresa: Optional[str] = None
    
    data_criacao: Optional[datetime] = None
    data_atualizacao: Optional[datetime] = None

    class Config:
        schema_extra = {
            "example": {
                "nome": "Alice Silva",
                "email": "alice.silva@exemplo.com",
                "telefone": "5511987654321",
                "empresa": "Tech Solutions Ltda",
                "data_criacao": "2025-10-15T12:00:00",
                "data_atualizacao": "2025-10-15T12:00:00"
            }
        }