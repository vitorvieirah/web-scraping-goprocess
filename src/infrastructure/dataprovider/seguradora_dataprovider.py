import uuid

from cryptography.fernet import Fernet
from sqlalchemy.exc import SQLAlchemyError
import logging

from src.domain.usuario import Usuario
from src.infrastructure.entity.seguradora_entity import SeguradoraEntity
from src.infrastructure.exception.DataProviderException import DataProviderException

from src.config.database import SessionLocal
from src.infrastructure.mapper.mapper_seguradora import SeguradoraMapper
from src.domain.seguradora import Seguradora

logger = logging.getLogger(__name__)

class SeguradoraDataProvider:

    def __init__(self, seguradora_mapper: SeguradoraMapper, chave_fernet: str):
        self.seguradora_mapper = seguradora_mapper
        self.cipher = Fernet(chave_fernet)

    def salvar(self, seguradora: Seguradora):
        session = SessionLocal()

        seguradora_entity = self.seguradora_mapper.para_entity(seguradora)

        seguradora_entity.usuario_credencial = self.cipher.encrypt(seguradora_entity.usuario_credencial.encode()).decode()
        seguradora_entity.senha_credencial = self.cipher.encrypt(seguradora_entity.senha_credencial.encode()).decode()

        try:
            persisted_entity = session.merge(seguradora_entity)
            session.commit()

            seguradora_domain = self.seguradora_mapper.para_domain(persisted_entity)
            seguradora_domain.usuario_credencial = self.cipher.decrypt(seguradora_domain.usuario_credencial.encode()).decode()
            seguradora_domain.senha_credencial = self.cipher.decrypt(seguradora_domain.senha_credencial.encode()).decode()

            return seguradora_domain
        except Exception as e:
            session.rollback()
            logger.exception(f"Erro ao salvar seguradora no banco de dados: {e}")
            raise DataProviderException("Erro ao salvar seguradora")
        finally:
            session.close()

    def listar_por_usuario(self, id_usuario: uuid.UUID):
        session = SessionLocal()
        try:
            seguradoras = (
                session.query(SeguradoraEntity)
                .filter(SeguradoraEntity.usuario_id == id_usuario)
                .all()
            )
            return seguradoras
        except Exception as e:
            session.rollback()
            logger.exception(f"Erro ao listar seguradoras pelo id do usuário: {e}")
            raise DataProviderException("Erro ao listar seguradoras pelo id do usuário")
        finally:
            session.close()