from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.config.database import Base


class UsuarioEntity(Base):
    __tablename__ = 'usuarios'

    id_usuario = Column(UUID(as_uuid=True), primary_key=True, index=True)
    nome = Column(String, nullable=False)

    seguradoras = relationship("SeguradoraEntity", back_populates="usuario", cascade="all, delete-orphan")
    pericias = relationship("PericiaEntity", back_populates="usuario", cascade="all, delete-orphan")

