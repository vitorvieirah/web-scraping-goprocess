import logging

from src.infrastructure.entity.pericia_entity import PericiaEntity
from src.config.database import SessionLocal
from src.infrastructure.mapper.mapper_pericia import PericiaMapper
from src.infrastructure.exception.DataProviderException import DataProviderException

logger = logging.getLogger(__name__)

class PericiaDataprovider:
    def __init__(self, pericia_mapper: PericiaMapper):
        self.pericia_mapper = pericia_mapper

    def salvar(self, pericia: PericiaEntity):
        session = SessionLocal()
        pericia_entity = self.pericia_mapper.paraEntity(pericia=pericia)
        try:
            persisted_entity = session.merge(pericia_entity)
            session.commit()
            return self.pericia_mapper.paraDomain(pericia_entity=persisted_entity)
        except Exception as e:
            session.rollback()
            logger.exception("Erro ao salvar pericia no banco de dados", e)
            raise DataProviderException("Erro ao salvar pericia")
        finally:
            session.close()
        