from src.config.database import Base, engine
from src.infrastructure.dataprovider.pericia_dataprovider import PericiaDataprovider
from src.infrastructure.dataprovider.webscraping_dataprovider import WebScrapingDataProvider
from src.config.settings import USERNAME
from src.config.settings import PASSWORD
from src.infrastructure.entity.pericia_entity import PericiaEntity


Base.metadata.create_all(engine)

class MainService:
    def __init__(self):
        self.pericia_dataprovider = PericiaDataprovider()
        self.ws_dataprovider = WebScrapingDataProvider(headless=False)

    def coletar_dados(self):
        self.ws_dataprovider.login(login_url="https://inspectos.com/sistema/index.html#/home",
                                   username=USERNAME,
                                   password=PASSWORD)
        dados = self.ws_dataprovider.raspar()

        dados_salvos = []
        for pericia in dados:
            pericia_salva = self.pericia_dataprovider.salvar(pericia=pericia)

            dados_salvos.append(pericia_salva)

        return dados_salvos

if __name__ == "__main__":
    service = MainService()
    resultado = service.coletar_dados()
    print("Resultado da coleta:", resultado)