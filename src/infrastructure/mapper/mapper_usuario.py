from src.domain.usuario import Usuario
from src.infrastructure.entity.usuario_entity import UsuarioEntity

class UsuarioMapper:

    @staticmethod
    def para_domain(entity: UsuarioEntity) -> Usuario:
        return Usuario(
            id_usuario=entity.id_usuario,
            nome=entity.nome,
            seguradoras=[],
            pericias=[]
        )

    @staticmethod
    def para_entity(domain: Usuario) -> UsuarioEntity:
        entity = UsuarioEntity(
            id_usuario=domain.id_usuario,
            nome=domain.nome
        )
        return entity