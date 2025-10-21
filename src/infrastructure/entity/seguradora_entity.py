from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from src.config.database import Base

class SeguradoraEntity(Base):
    __tablename__ = 'seguradoras'

    id_seguradora = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, nullable=False)
    user_credencial = Column(String, nullable=False)
    senha_credencial = Column(String, nullable=False)
    identificador = Column(String, nullable=False)
    url_site = Column(String, nullable=False)

    usuario_id = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)

    # 🔗 Relacionamentos
    usuario = relationship("UsuarioEntity", back_populates="seguradoras")
    pericias = relationship("PericiaEntity", back_populates="seguradora", cascade="all, delete-orphan")