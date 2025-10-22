from sqlalchemy import Column, String, Integer, DateTime, func, ForeignKey

from sqlalchemy.orm import relationship

from src.config.database import Base


class PericiaEntity(Base):
    __tablename__ = 'pericias'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    created_at = Column(DateTime, nullable=False, default=func.now())
    seguradora_nome = Column(String, nullable=False)
    numero_proposta = Column(String, nullable=False)
    numero_apolice = Column(String, nullable=False)
    area_segurada_total = Column(String, nullable=False)
    numero_sinistro = Column(String, nullable=False)
    data_aviso_sinistro = Column(String, nullable=False)
    data_ocorrencia = Column(String, nullable=False)
    evento = Column(String, nullable=False)
    cultura = Column(String, nullable=False)
    produtividade_estimada = Column(String, nullable=False)
    numero_aviso = Column(String, nullable=False)
    cobertura_sinistrada = Column(String, nullable=False)
    nome_proponente = Column(String, nullable=False)
    telefone_proponente = Column(String, nullable=False)
    cpf_cnpj_proponente = Column(String, nullable=False)
    nome_corretor = Column(String, nullable=False)

    #🔗 FK para Usuario e Seguradora
    usuario_id = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    seguradora_id = Column(Integer, ForeignKey("seguradoras.id_seguradora"), nullable=False)

    # 🔗 Relacionamentos
    usuario = relationship("UsuarioEntity", back_populates="pericias")
    seguradora = relationship("SeguradoraEntity", back_populates="pericias")