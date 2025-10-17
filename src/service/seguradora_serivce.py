import uuid

from src.infrastructure.dataprovider.seguradora_dataprovider import SeguradoraDataProvider
from src.infrastructure.dataprovider.usuario_dataprovider import UsuarioDataProvider
from src.service.webscraping_service import WebscrapingService


class SeguradoraService:
    def __init__(self, data_provider: SeguradoraDataProvider):
        self.data_provider = data_provider


    def listar_por_usuario(self, id_usuario: uuid.UUID):
        return self.data_provider.listar_por_usuario(id_usuario)