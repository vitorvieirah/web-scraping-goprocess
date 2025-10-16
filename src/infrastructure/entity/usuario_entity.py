from src.config.database import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.mysql import BINARY
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

class UsuarioEntity(Base):
    __tablename__ = 'usuarios'

    id_usuario = Column(UUID(as_uuid=True), primary_key=True, index=True)
    nome = Column(String, nullable=False)
    seguradora_id = Column(BINARY(16), ForeignKey("seguradoras.id_seguradora"), nullable=False)

    # Relacionamento direto: o usuário pertence a uma seguradora
    seguradora = relationship(
        "SeguradoraEntity",
        back_populates="usuarios"
    )