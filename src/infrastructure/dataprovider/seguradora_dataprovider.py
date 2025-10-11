from cryptography.fernet import Fernet
from sqlalchemy.exc import SQLAlchemyError
import logging
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
            logger.exception("Erro ao salvar usuário no banco de dados", e)
            raise DataProviderException("Erro ao salvar usuário")
        finally:
            session.close()
    