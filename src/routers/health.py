from fastapi import APIRouter
from src.db.memoria_db import CONTATOS, PROXIMO_ID
from src.core.config import settings

router = APIRouter(
    tags=["Health"] 
)

@router.get("/health")
async def check_health():
    return {
        "status": "OK", 
        "version": settings.VERSION,
        "database_status": {
            "type": "in_memory",
            "contacts_count": len(CONTATOS),
            "next_id": PROXIMO_ID          
        }
    }

@router.get("/status")
async def get_api_status():
    return {
        "project_name": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "environment": settings.ENVIRONMENT
    }