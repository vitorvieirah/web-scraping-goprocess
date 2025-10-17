from src.domain.identificador_seguradora import IdentificadorSeguradora
from src.domain.seguradora import Seguradora
from src.infrastructure.entity.seguradora_entity import SeguradoraEntity
from src.infrastructure.mapper.mapper_usuario import UsuarioMapper

class SeguradoraMapper:

    @staticmethod
    def para_domain(entity: SeguradoraEntity) -> Seguradora:
        usuario_domain = UsuarioMapper.para_domain(entity.usuario) if entity.usuario else None

        identificador_enum = IdentificadorSeguradora(entity.identificador) if entity.identificador else None

        return Seguradora(
            id_seguradora=entity.id_seguradora,
            nome=entity.nome,
            user_credencial=entity.user_credencial,
            senha_credencial=entity.senha_credencial,
            usuario_id=entity.usuario_id,
            usuario=usuario_domain,
            identificador=identificador_enum,
            pericias=[],
            url_site=entity.url_site,
        )

    @staticmethod
    def para_entity(domain: Seguradora) -> SeguradoraEntity:
        identificador_str = domain.identificador.value if domain.identificador else None

        entity = SeguradoraEntity(
            id_seguradora=domain.id_seguradora,
            nome=domain.nome,
            user_credencial=domain.user_credencial,
            senha_credencial=domain.senha_credencial,
            identificador=identificador_str,
            usuario_id=domain.usuario_id,
            url_site=domain.url_site,
        )

        return entity