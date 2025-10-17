from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.config.database import Base


class SeguradoraEntity(Base):
    __tablename__ = 'seguradora'

    id_seguradora = Column(UUID(as_uuid=True), primary_key=True, index=True)
    nome = Column(String, nullable=False)
    user_credencial = Column(String, nullable=False)
    senha_credencial = Column(String, nullable=False)
    identificador = Column(String, nullable=False)
    url_site = Column(String, nullable=False)

    usuario_id = Column(UUID(as_uuid=True), ForeignKey("usuarios.id_usuario"), nullable=False)

    usuario = relationship("UsuarioEntity", back_populates="seguradoras")
    pericias = relationship("PericiaEntity", back_populates="seguradora", cascade="all, delete-orphan")