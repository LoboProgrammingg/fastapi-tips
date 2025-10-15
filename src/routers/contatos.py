from fastapi import APIRouter, HTTPException, status, Header
from src.models.contato import Contato
from db.memoria_db import CONTATOS, PROXIMO_ID
from src.core.config import settings
from typing import List, Optional
from src.utils.query_utils import apply_pagination_and_sorting
from datetime import datetime
from src.models.enums import SortingDirection


API_KEY_SECRET = "SECRET"


async def verify_api_key(x_api_key: str = Header(..., alias="X-API-Key")):
    if x_api_key != settings.API_KEY_SECRET:
        raise HTTPException(status_code=401, detail="Chave de API inválida ou ausente")


router = APIRouter(prefix="/contatos", tags=["Contatos"])


@router.get("/", response_model=List[Contato])
async def listar_contatos(
    nome: Optional[str] = None,      
    empresa: Optional[str] = None,
    limit: int = 10,
    offset: int = 0,
    sort_by: Optional[str] = 'id', 
    direction: SortingDirection = SortingDirection.asc
):
    contatos_filtrados = CONTATOS

    if nome:
        contatos_filtrados = [
            contato for contato in contatos_filtrados 
            if nome.lower() in contato.nome.lower()
        ]
        
    if empresa:
        contatos_filtrados = [
            contato for contato in contatos_filtrados 
            if contato.empresa and empresa.lower() in contato.empresa.lower()
        ]

    return apply_pagination_and_sorting(
        contatos=contatos_filtrados,
        limit=limit,
        offset=offset,
        sort_by=sort_by,
        direction=direction.value
    )


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

            novo_contato = contato_atualizado.model_copy(
                update={
                    "id": contato_id,
                    "data_criacao": contato.data_criacao,
                    "data_atualizacao": agora,
                }
            )

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


@router.patch("/{contato_id}", response_model=Contato)
async def atualizar_parcialmente_contato(contato_id: int, contato_patch: Contato):
    for index, contato_existente in enumerate(CONTATOS):
        if contato_existente.id == contato_id:

            dados_atualizar = contato_patch.model_dump(exclude_unset=True)

            if not dados_atualizar:
                return contato_existente

            contato_atualizado = contato_existente.model_copy(update=dados_atualizar)

            agora = datetime.now()
            final_contato = contato_atualizado.model_copy(
                update={
                    "id": contato_id,
                    "data_criacao": contato_existente.data_criacao,
                    "data_atualizacao": agora,
                }
            )

            CONTATOS[index] = final_contato

            return final_contato

    raise HTTPException(status_code=404, detail="Contato não encontrado")
