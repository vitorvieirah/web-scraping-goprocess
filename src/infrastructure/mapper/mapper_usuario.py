from src.domain.usuario import Usuario
from src.infrastructure.entity.usuario_entity import UsuarioEntity

class UsuarioMapper:

    @staticmethod
    def para_domain(usuario_entity: UsuarioEntity) -> Usuario:
        return Usuario(
            id=usuario_entity.id_usuario,
            nome=usuario_entity.nome,
            usuario=usuario_entity.usuario,
            senha=usuario_entity.senha,
            seguradora=usuario_entity.seguradora,
        )

    @staticmethod
    def para_entity(usuario: Usuario) -> UsuarioEntity:
        return UsuarioEntity(
            id_usuario=usuario.id,
            nome=usuario.nome,
            usuario=usuario.usuario,
            senha=usuario.senha,
            seguradora=usuario.seguradora,
        )