from fastapi import APIRouter
from src.db.memoria_db import CONTATOS, PROXIMO_ID

router = APIRouter(
    tags=["Health"] 
)

@router.get("/health")
async def check_health():
    return {
        "status": "OK", 
        "version": "0.7.0",
        "database_status": {
            "type": "in_memory",
            "contacts_count": len(CONTATOS),
            "next_id": PROXIMO_ID
        }
    }