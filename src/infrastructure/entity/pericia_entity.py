import uuid

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.config.database import Base


class PericiaEntity(Base):
    __tablename__ = 'pericias'

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    created_at = Column(String, nullable=True)
    data_empresa = Column(String, nullable=True)
    categoria = Column(String, nullable=True)
    tipo_vistoria = Column(String, nullable=True)
    causa = Column(String, nullable=True)
    numero_proposta = Column(String, nullable=True)
    cultura = Column(String, nullable=True)
    produtividade_esperada = Column(String, nullable=True)
    seguradora_scr = Column(String, nullable=True)
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


# 🔗 FK para Usuario e Seguradora
    usuario_id = Column(UUID(as_uuid=True), ForeignKey("usuarios.id_usuario"), nullable=False)
    seguradora_id = Column(UUID(as_uuid=True), ForeignKey("seguradoras.id_seguradora"), nullable=False)

    # 🔗 Relacionamentos
    usuario = relationship("UsuarioEntity", back_populates="pericias")
    seguradora = relationship("SeguradoraEntity", back_populates="pericias")