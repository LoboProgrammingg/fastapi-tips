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
                "empresa": "Tech Solutions Ltda",
            }
        }
