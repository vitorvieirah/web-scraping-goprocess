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
            data_empresa=entity.data_empresa,
            categoria=entity.categoria,
            tipo_vistoria=entity.tipo_vistoria,
            causa=entity.causa,
            numero_proposta=entity.numero_proposta,
            cultura=entity.cultura,
            produtividade_esperada=entity.produtividade_esperada,
            seguradora_scr=entity.seguradora_scr,
            numero_apolice=entity.numero_apolice,
            segurado=entity.segurado,
            cpf_cnpj=entity.cpf_cnpj,
            numero_contato=entity.numero_contato,
            municipio=entity.municipio,
            uf=entity.uf,
            area=entity.area,
            nome_analista=entity.nome_analista,
            numero_sinistro=entity.numero_sinistro,
            data_captura=entity.data_captura,
            status=entity.status,
            evento=entity.evento,
            cobertura=entity.cobertura,
            corretor=entity.corretor,
            usuario_id=entity.usuario_id,
            seguradora_id=entity.seguradora_id,
            usuario=usuario_domain,
            seguradora=seguradora_domain
        )

    @staticmethod
    def para_entity(domain: Pericia) -> PericiaEntity:
        entity = PericiaEntity(
            id=domain.id,
            created_at=domain.created_at,
            data_empresa=domain.data_empresa,
            categoria=domain.categoria,
            tipo_vistoria=domain.tipo_vistoria,
            causa=domain.causa,
            numero_proposta=domain.numero_proposta,
            cultura=domain.cultura,
            produtividade_esperada=domain.produtividade_esperada,
            seguradora_scr=domain.seguradora_scr,
            numero_apolice=domain.numero_apolice,
            segurado=domain.segurado,
            cpf_cnpj=domain.cpf_cnpj,
            numero_contato=domain.numero_contato,
            municipio=domain.municipio,
            uf=domain.uf,
            area=domain.area,
            nome_analista=domain.nome_analista,
            numero_sinistro=domain.numero_sinistro,
            data_captura=domain.data_captura,
            status=domain.status,
            evento=domain.evento,
            cobertura=domain.cobertura,
            corretor=domain.corretor,
            usuario_id=domain.usuario_id,
            seguradora_id=domain.seguradora_id
        )
        return entity