from fastapi import APIRouter

router = APIRouter(tags=["Root"])


@router.get("/")
async def read_root():
    return {"message": "Bem-vindo à API do Mini CRM"}
