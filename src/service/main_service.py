from src.infrastructure.dataprovider.webscraping_dataprovider import WebScrapingDataProvider
from src.config.settings import USERNAME, PASSWORD

class MainService:
    def __init__(self):
        self.dataprovider = WebScrapingDataProvider(headless=False)

    def coletar_dados(self):
        dados = self.dataprovider.login(login_url="https://inspectos.com/sistema/index.html#/home",
                                        username=USERNAME,
                                        password=PASSWORD)
        return dados

if __name__ == "__main__":
    service = MainService()
    resultado = service.coletar_dados()
    print("Resultado da coleta:", resultado)