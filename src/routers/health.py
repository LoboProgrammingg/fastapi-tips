from fastapi import APIRouter

router = APIRouter(tags=["Health"])


@router.get("/health")
async def check_health():
    return {"status": "OK", "version": "0.4.0"}
