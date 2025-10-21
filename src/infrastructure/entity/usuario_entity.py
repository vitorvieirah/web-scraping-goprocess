from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.config.database import Base

class UsuarioEntity(Base):
    __tablename__ = 'usuarios'

    id_usuario = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, nullable=False)

    # 🔗 Relacionamentos
    seguradoras = relationship("SeguradoraEntity", back_populates="usuario", cascade="all, delete-orphan")  # plural
    pericias = relationship("PericiaEntity", back_populates="usuario", cascade="all, delete-orphan")  # plural

