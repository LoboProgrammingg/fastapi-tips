from fastapi import APIRouter
from src.models.contato import Contato
from src.db.memoria_db import CONTATOS, PROXIMO_ID

router = APIRouter(
    prefix="/contatos",
    tags=["Contatos"]
)

@router.post("/", response_model=Contato, status_code=201)
async def criar_contato(contato: Contato):

    global PROXIMO_ID
    
    contato.id = PROXIMO_ID
    CONTATOS.append(contato)
    PROXIMO_ID += 1

    return contato