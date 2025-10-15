from pydantic import BaseModel
from typing import Optional

class ErrorResponse(BaseModel):
    detail: str
    request_id: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "detail": "Contato não encontrado",
                "request_id": "f5e9c0b1-3e4a-4d7c-8b9a-1c3e5a7b6d5f"
            }
        }