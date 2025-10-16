from dataclasses import dataclass
from uuid import UUID

@dataclass
class Usuario:
    id: UUID
    nome: str
    seguradora: str