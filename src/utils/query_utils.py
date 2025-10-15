from typing import List, Any
from src.models.contato import Contato

def apply_pagination_and_sorting(
    contatos: List[Contato], 
    limit: int, 
    offset: int, 
    sort_by: str, 
    direction: str
) -> List[Contato]:

    campos_validos = Contato.model_fields.keys()
    
    if sort_by and sort_by in campos_validos:
        reverse_sort = direction.lower() == 'desc'
        
        def sort_key(c: Contato) -> Any:
            val = getattr(c, sort_by)
            if val is None:
                return "" if isinstance(getattr(Contato, sort_by, None), str) else 0
            return val

        try:
            contatos = sorted(
                contatos, 
                key=sort_key,
                reverse=reverse_sort
            )
        except Exception:
            pass 

    return contatos[offset : offset + limit]