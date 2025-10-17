from src.domain.identificador_seguradora import IdentificadorSeguradora
from src.domain.usuario import Usuario
from typing import List, Optional
from uuid import UUID


class Seguradora:
    def __init__(
        self,
        id_seguradora: UUID,
        nome: str,
        user_credencial: str,
        senha_credencial: str,
        usuario_id: UUID,
        usuario: Optional["Usuario"] = None,
        pericias: Optional[List["Pericia"]] = None,
        identificador: IdentificadorSeguradora = None,
        url_site: str = ""
    ):
        self.id_seguradora = id_seguradora
        self.nome = nome
        self.user_credencial = user_credencial
        self.senha_credencial = senha_credencial
        self.usuario_id = usuario_id
        self.usuario = usuario
        self.pericias = pericias or []
        self.identificador = identificador
        self.url_site = url_site
