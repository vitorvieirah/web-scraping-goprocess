from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import BINARY, TINYINT
from src.config.database import Base

class PericiaEntity(Base):
    __tablename__ = 'pericias'

    id_pericia = Column(BINARY(16), primary_key=True, index=True)
    titulo = Column(String(255), nullable=True)
