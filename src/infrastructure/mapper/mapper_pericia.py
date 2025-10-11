from src.domain.pericia import Pericia
from src.infrastructure.entity.pericia_entity import PericiaEntity

class PericiaMapper:

    def para_entity(self, pericia: Pericia) -> PericiaEntity:
        return PericiaEntity(
            id=pericia.id,  
            created_at=pericia.created_at,
            data_empresa=pericia.data_empresa,
            categoria=pericia.categoria,
            tipo_vistoria=pericia.tipo_vistoria,
            causa=pericia.causa,
            numero_proposta=pericia.numero_proposta,
            cultura=pericia.cultura,
            produtividade_esperada=pericia.produtividade_esperada,
            seguradora=pericia.seguradora,
            numero_apolice=pericia.numero_apolice,
            segurado=pericia.segurado,
            cpf_cnpj=pericia.cpf_cnpj,
            numero_contato=pericia.numero_contato,
            municipio=pericia.municipio,
            uf=pericia.uf,
            area=pericia.area,
            nome_analista=pericia.nome_analista,
            numero_sinistro=pericia.numero_sinistro,
            data_captura=pericia.data_captura,
            status=pericia.status,
            evento=pericia.evento,
            cobertura=pericia.cobertura,
            corretor=pericia.corretor
        )

    def para_domain(self, pericia_entity: PericiaEntity) -> Pericia:
        return Pericia(
            id=pericia_entity.id,
            created_at=pericia_entity.created_at,
            data_empresa=pericia_entity.data_empresa,
            categoria=pericia_entity.categoria,
            tipo_vistoria=pericia_entity.tipo_vistoria,
            causa=pericia_entity.causa,
            numero_proposta=pericia_entity.numero_proposta,
            cultura=pericia_entity.cultura,
            produtividade_esperada=pericia_entity.produtividade_esperada,
            seguradora=pericia_entity.seguradora,
            numero_apolice=pericia_entity.numero_apolice,
            segurado=pericia_entity.segurado,
            cpf_cnpj=pericia_entity.cpf_cnpj,
            numero_contato=pericia_entity.numero_contato,
            municipio=pericia_entity.municipio,
            uf=pericia_entity.uf,
            area=pericia_entity.area,
            nome_analista=pericia_entity.nome_analista,
            numero_sinistro=pericia_entity.numero_sinistro,
            data_captura=pericia_entity.data_captura,
            status=pericia_entity.status,
            evento=pericia_entity.evento,
            cobertura=pericia_entity.cobertura,
            corretor=pericia_entity.corretor
        )

