from tokenize import String

from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import BINARY, TINYINT
from src.config.database import Base

class PericiaEntity(Base):
    __tablename__ = 'pericias'

    id = Column(BINARY(16), primary_key=True, index=True)
    created_at = Column(String, nullable=True)
    data_empresa = Column(String, nullable=True)
    categoria = Column(String, nullable=True)
    tipo_vistoria = Column(String, nullable=True)
    causa = Column(String, nullable=True)
    numero_proposta = Column(String, nullable=True)
    cultura = Column(String, nullable=True)
    produtividade_esperada = Column(String, nullable=True)
    seguradora = Column(String, nullable=True)
    numero_apolice = Column(String, nullable=True)
    segurado = Column(String, nullable=True)
    cpf_cnpj = Column(String, nullable=True)
    numero_contato = Column(String, nullable=True)
    municipio = Column(String, nullable=True)
    uf = Column(String, nullable=True)
    area = Column(String, nullable=True)
    nome_analista = Column(String, nullable=True)
    numero_sinistro = Column(String, nullable=True)
    data_captura = Column(String, nullable=True)
    status = Column(String, nullable=True)
    evento = Column(String, nullable=True)
    cobertura = Column(String, nullable=True)
    corretor = Column(String, nullable=True)
