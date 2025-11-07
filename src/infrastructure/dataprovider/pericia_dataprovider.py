import logging

from sqlalchemy.exc import IntegrityError

from src.config.database import SessionLocal
from src.domain.pericia import Pericia
from src.infrastructure.exception.DataProviderException import DataProviderException
from src.infrastructure.mapper.mapper_pericia import PericiaMapper

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

        except IntegrityError as e:
            session.rollback()
            # ⚠️ Aqui tratamos apenas o caso de duplicidade
            if 'unique constraint' in str(e).lower() or 'duplicate key' in str(e).lower():
                logger.warning(f"⚠️ Proposta duplicada ignorada: {pericia.numero_proposta}")
                return None
            else:
                logger.exception(f"Erro de integridade ao salvar perícia: {e}")
                raise DataProviderException("Erro de integridade no banco de dados.")

        except Exception as e:
            session.rollback()
            logger.exception(f"Erro ao salvar perícia no banco de dados: {e}")
            raise DataProviderException("Erro ao salvar perícia.")

        finally:
            session.close()
