
from src.domain.seguradora import Seguradora
from src.infrastructure.entity.seguradora_entity import SeguradoraEntity
from src.infrastructure.mapper.mapper_usuario import UsuarioMapper

class SeguradoraMapper:

    def __init__(self):
        self.usuario_mapper = UsuarioMapper()

    def para_entity(self, seguradora: Seguradora) -> SeguradoraEntity:

        entity = SeguradoraEntity(
            id_seguradora=seguradora.id_seguradora,
            nome=seguradora.nome,
            usuario_credencial=seguradora.usuario_credencial,
            senha_credencial=seguradora.senha_credencial
        )

        # Mapeia usuários se houver
        if seguradora.usuarios:
            entity.usuarios = [
                self.usuario_mapper.paraEntity(usuario) for usuario in seguradora.usuarios
            ]

        return entity

    def para_domain(self, entity: SeguradoraEntity) -> Seguradora:

        usuarios_domain = []
        if entity.usuarios:
            usuarios_domain = [
                self.usuario_mapper.paraDomain(usuario_entity)
                for usuario_entity in entity.usuarios
            ]

        return Seguradora(
            id_seguradora=entity.id_seguradora,
            nome=entity.nome,
            usuario_credencial=entity.usuario_credencial,
            senha_credencial=entity.senha_credencial,
            usuarios=usuarios_domain
        )