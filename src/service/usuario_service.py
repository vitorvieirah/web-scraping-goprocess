from src.infrastructure.dataprovider.usuario_dataprovider import UsuarioDataProvider


class UsuarioService:
    def __init__(self, data_provider: UsuarioDataProvider):
        self.data_provider = data_provider



    def listar_usuarios(self):
        return self.data_provider.listar()