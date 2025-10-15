from fastapi import APIRouter, HTTPException, status, Header
from src.models.contato import Contato
from src.db.memoria_db import CONTATOS, PROXIMO_ID
from typing import List, Optional
from datetime import datetime


API_KEY_SECRET = "SECRET"


async def verify_api_key(x_api_key: str = Header(..., alias="X-API-Key")):
    if x_api_key != API_KEY_SECRET:
        raise HTTPException(status_code=401, detail="Chave de API inválida ou ausente")


router = APIRouter(prefix="/contatos", tags=["Contatos"])


@router.post("/", response_model=Contato, status_code=201)
async def criar_contato(contato: Contato):
    global PROXIMO_ID

    agora = datetime.now()

    contato.id = PROXIMO_ID

    CONTATOS.append(
        contato.model_copy(
            update={"id": PROXIMO_ID, "data_criacao": agora, "data_atualizacao": agora}
        )
    )
    PROXIMO_ID += 1

    return CONTATOS[-1]


@router.get("/", response_model=List[Contato])
async def listar_contatos(
    nome: Optional[str] = None,
    empresa: Optional[str] = None,
    limit: int = 10,
    offset: int = 0,
    sort_by: Optional[str] = "id",
    direction: Optional[str] = "asc",
):
    contatos_filtrados = CONTATOS

    if nome:
        contatos_filtrados = [
            contato
            for contato in contatos_filtrados
            if nome.lower() in contato.nome.lower()
        ]

    if empresa:
        contatos_filtrados = [
            contato
            for contato in contatos_filtrados
            if contato.empresa and empresa.lower() in contato.empresa.lower()
        ]

    campos_validos = Contato.model_fields.keys()

    if sort_by and sort_by in campos_validos:
        reverse_sort = direction.lower() == "desc"

        try:
            contatos_filtrados = sorted(
                contatos_filtrados,
                key=lambda c: (
                    getattr(c, sort_by) if getattr(c, sort_by) is not None else ""
                ),
                reverse=reverse_sort,
            )
        except Exception:
            pass

    return contatos_filtrados[offset : offset + limit]


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
