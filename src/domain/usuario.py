from dataclasses import dataclass, field
from typing import List, Optional

from src.domain.pericia import Pericia
from src.domain.seguradora import Seguradora


@dataclass
class Usuario:
    id_usuario: Optional[int]
    nome: str
