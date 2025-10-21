from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Usuario:
    id_usuario: Optional[int]
    nome: str
