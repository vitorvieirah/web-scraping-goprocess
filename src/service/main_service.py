from src.config.database import Base, engine
from src.config.settings import PASSWORD
from src.config.settings import USERNAME
from src.infrastructure.dataprovider.pericia_dataprovider import PericiaDataprovider
from src.infrastructure.dataprovider.swiss_re_dataprovider import WebScrapingDataProvider
from src.service.usuario_service import UsuarioService
from src.domain.usuario import Usuario
from src.service.webscraping_service import WebscrapingService

Base.metadata.create_all(engine)

class MainService:
    def __init__(self, usuario_service: UsuarioService, webscraping_service: WebscrapingService):
        self.usuario_service = usuario_service
        self.webscraping_service = webscraping_service

    def coletar_dados(self):
        usuarios = self.usuario_service.listar_usuarios()

        for usuario in usuarios:
            self.webscraping_service.processar(usuario)




if __name__ == "__main__":
    service = MainService()
    resultado = service.coletar_dados()
    print("Resultado da coleta:", resultado)