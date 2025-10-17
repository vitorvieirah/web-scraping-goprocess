from dataclasses import dataclass
from uuid import UUID
from typing import Optional, List

@dataclass
class Usuario:
    def __init__(
        self,
        id_usuario: UUID,
        nome: str,
        seguradoras: Optional[List["Seguradora"]] = None,
        pericias: Optional[List["Pericia"]] = None
    ):
        self.id_usuario = id_usuario
        self.nome = nome
        self.seguradoras = seguradoras or []
        self.pericias = pericias or []