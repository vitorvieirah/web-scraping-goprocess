from dataclasses import dataclass
from uuid import UUID


@dataclass
class Pericia:
    id = UUID
    created_at = str
    data_empresa = str
    categoria = str
    tipo_vistoria = str
    causa = str
    numero_proposta = str
    cultura = str
    produtividade_esperada = str
    seguradora = str
    numero_apolice = str
    segurado = str
    cpf_cnpj = str
    numero_contato = str
    municipio = str
    uf = str
    area = str
    nome_analista = str
    numero_sinistro = str
    data_captura = str
    status = str
    evento = str
    cobertura = str
    corretor = str