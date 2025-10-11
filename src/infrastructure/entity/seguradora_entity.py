from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import BINARY
from sqlalchemy.orm import relationship

from src.config.database import Base

class SeguradoraEntity(Base):
    __tablename__ = 'seguradora'

    id_seguradora = Column(BINARY(16), primary_key=True, index=True)
    nome = Column(String, nullable=False)
    usuario_credencial = Column(String, nullable=False)
    senha_credencial = Column(String, nullable=False)
    usuarios = relationship(
        "UsuarioEntity",
        back_populates="seguradora"
    )