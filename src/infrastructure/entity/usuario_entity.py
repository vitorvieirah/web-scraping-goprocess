from src.config.database import Base
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import BINARY

class UsuarioEntity(Base):
    __tablename__ = 'usuario_entity'

    id_usuario = Column(BINARY(16), primary_key=True, index=True)
    nome = Column(String, nullable=False)
    usuario = Column(String, nullable=False)
    senha = Column(String, nullable=False)
    seguradora = Column(String, nullable=False)