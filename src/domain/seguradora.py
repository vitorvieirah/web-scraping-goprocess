from src.domain.identificador_seguradora import IdentificadorSeguradora
from typing import List, Optional
from uuid import UUID
from dataclasses import dataclass


@dataclass
class Seguradora:
    id_seguradora: Optional[int] = None
    nome: Optional[str] = None
    user_credencial: Optional[str] = None
    senha_credencial: Optional[str] = None
    identificador: Optional[IdentificadorSeguradora] = None
    url_site: Optional[str] = None
    usuario_id: Optional[int] = None
