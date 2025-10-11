from src.domain.usuario import Usuario
from typing import List, Optional
from uuid import UUID


class Seguradora:
    def __init__(
        self,
        id_seguradora: UUID,
        nome: str,
        usuario_credencial: str,
        senha_credencial: str,
        usuarios: Optional[List[Usuario]] = None
    ):
        self.id_seguradora = id_seguradora
        self.nome = nome
        self.usuario_credencial = usuario_credencial
        self.senha_credencial = senha_credencial
        self.usuarios = usuarios or []