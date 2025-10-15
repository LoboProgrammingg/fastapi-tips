from fastapi import FastAPI
from src.routers import contatos
from src.routers import health
from src.routers import admin
from src.core.logging import logger
from src.middleware.request_id import RequestIDMiddleware, REQUEST_ID_HEADER
from src.core.config import settings
from starlette.requests import Request
from starlette.responses import JSONResponse

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Uma API simples para gerenciar contatos.",
    version=settings.VERSION
)

app.add_middleware(RequestIDMiddleware)

app.include_router(health.router) 
app.include_router(contatos.router) 
app.include_router(admin.router)

@app.exception_handler(Exception)
async def internal_exception_handler(request: Request, exc: Exception):
    request_id = request.state.request_id if hasattr(request.state, 'request_id') else 'N/A'
    
    logger.error(f"Erro Interno Não Tratado [ID: {request_id}]: {exc}", exc_info=True)
    
    return JSONResponse(
        status_code=500,
        content={
            "detail": "Ocorreu um erro interno não esperado.",
            "request_id": request_id
        },
        headers={REQUEST_ID_HEADER: request_id} 
    )

logger.info(f"Aplicação FastAPI inicializada e routers carregados. Versão {settings.VERSION}.")