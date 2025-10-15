from fastapi import APIRouter, HTTPException, status
from src.models.contato import Contato
from src.db.memoria_db import CONTATOS, PROXIMO_ID
from typing import List
from datetime import datetime

router = APIRouter(
    prefix="/contatos",
    tags=["Contatos"]
)


@router.post("/", response_model=Contato, status_code=201)
async def criar_contato(contato: Contato):
    global PROXIMO_ID
    
    agora = datetime.now()

    contato.id = PROXIMO_ID
    
    CONTATOS.append(contato.model_copy(update={
        "id": PROXIMO_ID,
        "data_criacao": agora,
        "data_atualizacao": agora
    })) 
    PROXIMO_ID += 1

    return CONTATOS[-1]


@router.get("/", response_model=List[Contato])
async def listar_contatos():
    return CONTATOS


@router.get("/{contato_id}", response_model=Contato)
async def buscar_contato_por_id(contato_id: int):
    for contato in CONTATOS:
        if contato.id == contato_id:
            return contato

    raise HTTPException(status_code=404, detail="Contato não encontrado")


@router.put("/{contato_id}", response_model=Contato)
async def atualizar_contato(contato_id: int, contato_atualizado: Contato):
    for index, contato in enumerate(CONTATOS):
        if contato.id == contato_id:
            
            agora = datetime.now()
            
            novo_contato = contato_atualizado.model_copy(update={
                "id": contato_id,
                "data_criacao": contato.data_criacao,
                "data_atualizacao": agora
            })
            
            CONTATOS[index] = novo_contato
            
            return novo_contato
            
    raise HTTPException(status_code=404, detail="Contato não encontrado")


@router.delete("/{contato_id}", status_code=status.HTTP_204_NO_CONTENT)
async def excluir_contato(contato_id: int):
    for index, contato in enumerate(CONTATOS):
        if contato.id == contato_id:
            del CONTATOS[index]
            return
            
    raise HTTPException(status_code=404, detail="Contato não encontrado")