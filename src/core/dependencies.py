from fastapi import Header, HTTPException
from src.core.config import settings

async def verify_api_key(x_api_key: str = Header(..., alias="X-API-Key")):
    if x_api_key != settings.API_KEY_SECRET:
        raise HTTPException(status_code=401, detail="Chave de API inválida ou ausente")