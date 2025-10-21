from src.domain.seguradora import Seguradora, IdentificadorSeguradora
from src.infrastructure.entity.seguradora_entity import SeguradoraEntity


class SeguradoraMapper:

    @staticmethod
    def para_domain(entity: SeguradoraEntity) -> Seguradora:
        identificador_enum = (
            IdentificadorSeguradora(entity.identificador)
            if entity.identificador
            else None
        )

        return Seguradora(
            id_seguradora=entity.id_seguradora,
            nome=entity.nome,
            user_credencial=entity.user_credencial,
            senha_credencial=entity.senha_credencial,
            identificador=identificador_enum,
            url_site=entity.url_site,
            usuario_id=entity.usuario_id
        )

    @staticmethod
    def para_entity(domain: Seguradora) -> SeguradoraEntity:
        identificador_str = (
            domain.identificador.value
            if domain.identificador
            else None
        )

        return SeguradoraEntity(
            id_seguradora=domain.id_seguradora,
            nome=domain.nome,
            user_credencial=domain.user_credencial,
            senha_credencial=domain.senha_credencial,
            identificador=identificador_str,
            url_site=domain.url_site,
            usuario_id=domain.usuario_id
        )
