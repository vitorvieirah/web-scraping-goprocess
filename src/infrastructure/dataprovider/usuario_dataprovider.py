import logging
from src.config.database import SessionLocal
from src.domain.usuario import Usuario
from src.infrastructure.entity.usuario_entity import UsuarioEntity
from src.infrastructure.mapper.mapper_usuario import UsuarioMapper
from src.infrastructure.exception.DataProviderException import DataProviderException

logger = logging.getLogger(__name__)

class UsuarioDataProvider:
    def __init__(self, usuario_mapper: UsuarioMapper):
        self.usuario_mapper = usuario_mapper

    def salvar(self, usuario: Usuario):
        session = SessionLocal()

        usuario_entity = self.usuario_mapper.para_entity(usuario)

        try:
            persisted_entity = session.merge(usuario_entity)
            session.commit()

            # descriptografando para devolver
            domain_obj = self.usuario_mapper.para_domain(persisted_entity)

            return domain_obj
        except Exception as e:
            session.rollback()
            logger.exception(f"Erro ao salvar usuario no banco de dados: {e}")
            raise DataProviderException("Erro ao salvar usuário")
        finally:
            session.close()

    def get_usuario(self, usuario_id):
        session = SessionLocal()

        try:
            usuario_entity = session.query(UsuarioEntity).filter_by(id=usuario_id).first()
            if usuario_entity:
                return self.usuario_mapper.para_domain(usuario_entity)
            return None
        except Exception as e:
            logger.exception(f"Erro ao buscar usuário no banco de dados: {e}")
            raise DataProviderException("Erro ao buscar usuário")
        finally:
            session.close()
