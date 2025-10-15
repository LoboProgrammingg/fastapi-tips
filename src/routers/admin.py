from fastapi import APIRouter, Depends, status
from src.db.memoria_db import CONTATOS, PROXIMO_ID
from src.routers.contatos import verify_api_key

router = APIRouter(
    prefix="/admin",
    tags=["Admin"],
    dependencies=[Depends(verify_api_key)]
)

@router.delete("/db/clear", status_code=status.HTTP_204_NO_CONTENT)
async def clear_database():
    global PROXIMO_ID
    
    CONTATOS.clear()
    PROXIMO_ID = 1
    
    return