import uuid
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

REQUEST_ID_HEADER = "X-Request-ID"

class RequestIDMiddleware(BaseHTTPMiddleware):
    """
    Middleware que gera um ID único para cada requisição (X-Request-ID) 
    e o adiciona ao cabeçalho da resposta para rastreamento.
    """
    async def dispatch(self, request: Request, call_next):
        request_id = str(uuid.uuid4())
        
        request.state.request_id = request_id 
        
        response = await call_next(request)
        
        response.headers[REQUEST_ID_HEADER] = request_id
        
        return response