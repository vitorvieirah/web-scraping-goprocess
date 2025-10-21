from src.domain.usuario import Usuario
from src.infrastructure.entity.usuario_entity import UsuarioEntity

class UsuarioMapper:

    @staticmethod
    def para_domain(entity: "UsuarioEntity") -> Usuario:
        return Usuario(
            id_usuario=entity.id_usuario,
            nome=entity.nome
        )

    @staticmethod
    def para_entity(domain: Usuario) -> "UsuarioEntity":
        return UsuarioEntity(
            id_usuario=domain.id_usuario,
            nome=domain.nome
        )
