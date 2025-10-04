import logging
from cryptography.fernet import Fernet
from src.config.database import SessionLocal
from src.infrastructure.entity.usuario_entity import UsuarioEntity
from src.infrastructure.mapper.mapper_usuario import UsuarioMapper
from src.infrastructure.exception.DataProviderException import DataProviderException

logger = logging.getLogger(__name__)

class UsuarioDataProvider:
    def __init__(self, usuario_mapper: UsuarioMapper, chave_fernet: str):
        self.usuario_mapper = usuario_mapper
        self.cipher = Fernet(chave_fernet)

    def salvar(self, usuario):
        session = SessionLocal()

        usuario_entity = self.usuario_mapper.para_entity(usuario)
        usuario_entity.usuario = self.cipher.encrypt(usuario_entity.usuario.encode()).decode()
        usuario_entity.senha = self.cipher.encrypt(usuario_entity.senha.encode()).decode()

        try:
            persisted_entity = session.merge(usuario_entity)
            session.commit()

            # descriptografando para devolver
            domain_obj = self.usuario_mapper.para_domain(persisted_entity)
            domain_obj.usuario = self.cipher.decrypt(domain_obj.usuario.encode()).decode()
            domain_obj.senha = self.cipher.decrypt(domain_obj.senha.encode()).decode()

            return domain_obj
        except Exception as e:
            session.rollback()
            logger.exception("Erro ao salvar usuário no banco de dados", e)
            raise DataProviderException("Erro ao salvar usuário")
        finally:
            session.close()

    def get_usuario(self, usuario_id):
        session = SessionLocal()

        try:
            usuario_entity = session.query(UsuarioEntity).filter_by(id=usuario_id).first()
            if usuario_entity:
                usuario_entity.usuario = self.cipher.decrypt(usuario_entity.usuario.encode()).decode()
                usuario_entity.senha = self.cipher.decrypt(usuario_entity.senha.encode()).decode()
                return self.usuario_mapper.para_domain(usuario_entity)
            return None
        except Exception as e:
            logger.exception("Erro ao buscar usuário no banco de dados", e)
            raise DataProviderException("Erro ao buscar usuário")
        finally:
            session.close()
