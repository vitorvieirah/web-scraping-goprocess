from src.domain.pericia import Pericia
from src.infrastructure.entity.pericia_entity import PericiaEntity
from src.infrastructure.mapper.mapper_seguradora import SeguradoraMapper
from src.infrastructure.mapper.mapper_usuario import UsuarioMapper


class PericiaMapper:

    @staticmethod
    def para_domain(entity: PericiaEntity) -> Pericia:
        usuario_domain = UsuarioMapper.para_domain(entity.usuario) if entity.usuario else None
        seguradora_domain = SeguradoraMapper.para_domain(entity.seguradora) if entity.seguradora else None

        return Pericia(
            id=entity.id,
            created_at=entity.created_at,
            seguradora_nome=entity.seguradora_nome,
            numero_proposta=entity.numero_proposta,
            numero_apolice=entity.numero_apolice,
            area_segurada_total=entity.area_segurada_total,
            numero_sinistro=entity.numero_sinistro,
            data_aviso_sinistro=entity.data_aviso_sinistro,
            data_ocorrencia=entity.data_ocorrencia,
            evento=entity.evento,
            cultura=entity.cultura,
            produtividade_estimada=entity.produtividade_estimada,
            numero_aviso=entity.numero_aviso,
            cobertura_sinistrada=entity.cobertura_sinistrada,
            nome_proponente=entity.nome_proponente,
            telefone_proponente=entity.telefone_proponente,
            cpf_cnpj_proponente=entity.cpf_cnpj_proponente,
            nome_corretor=entity.nome_corretor,
            usuario_id=entity.usuario_id,
            seguradora_id=entity.seguradora_id,
            usuario_rel=usuario_domain,
            seguradora_rel=seguradora_domain
        )

    @staticmethod
    def para_entity(domain: Pericia) -> PericiaEntity:
        return PericiaEntity(
            id=domain.id,
            created_at=domain.created_at,
            seguradora_nome=domain.seguradora_nome,
            numero_proposta=domain.numero_proposta,
            numero_apolice=domain.numero_apolice,
            area_segurada_total=domain.area_segurada_total,
            numero_sinistro=domain.numero_sinistro,
            data_aviso_sinistro=domain.data_aviso_sinistro,
            data_ocorrencia=domain.data_ocorrencia,
            evento=domain.evento,
            cultura=domain.cultura,
            produtividade_estimada=domain.produtividade_estimada,
            numero_aviso=domain.numero_aviso,
            cobertura_sinistrada=domain.cobertura_sinistrada,
            nome_proponente=domain.nome_proponente,
            telefone_proponente=domain.telefone_proponente,
            cpf_cnpj_proponente=domain.cpf_cnpj_proponente,
            nome_corretor=domain.nome_corretor,
            usuario_id=domain.usuario_id,
            seguradora_id=domain.seguradora_id
        )
