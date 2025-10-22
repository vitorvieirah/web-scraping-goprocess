import logging

from src.infrastructure.entity.pericia_entity import PericiaEntity
from src.config.database import SessionLocal
from src.infrastructure.mapper.mapper_pericia import PericiaMapper
from src.infrastructure.exception.DataProviderException import DataProviderException
from src.domain.pericia import Pericia

logger = logging.getLogger(__name__)

class PericiaDataprovider:
    def __init__(self):
        self.pericia_mapper = PericiaMapper()

    def salvar(self, pericia: Pericia) -> Pericia:
        session = SessionLocal()
        pericia_entity = self.pericia_mapper.para_entity(domain=pericia)
        try:
            persisted_entity = session.merge(pericia_entity)
            session.commit()
            return self.pericia_mapper.para_domain(entity=persisted_entity)
        except Exception as e:
            session.rollback()
            logger.exception(f"Erro ao salvar pericia no banco de dados: {e}")
            raise DataProviderException("Erro ao salvar pericia")
        finally:
            session.close()
        