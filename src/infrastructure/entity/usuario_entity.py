from src.config.database import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.mysql import BINARY
from sqlalchemy.orm import relationship

class UsuarioEntity(Base):
    __tablename__ = 'usuarios'

    id_usuario = Column(BINARY(16), primary_key=True, index=True)
    nome = Column(String, nullable=False)
    seguradora_id = Column(BINARY(16), ForeignKey("seguradoras.id_seguradora"), nullable=False)

    # Relacionamento direto: o usuário pertence a uma seguradora
    seguradora = relationship(
        "SeguradoraEntity",
        back_populates="usuarios"
    )