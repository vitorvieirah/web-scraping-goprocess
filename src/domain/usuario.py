from dataclasses import dataclass

@dataclass
class Usuario:
    id: str
    nome: str
    usuario: str
    senha: str
    seguradora: str