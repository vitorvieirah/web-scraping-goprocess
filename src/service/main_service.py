from src.infrastructure.dataprovider.webscraping_dataprovider import WebScrapingDataProvider
from src.config.settings import USERNAME
from src.config.settings import PASSWORD

class MainService:
    def __init__(self):
        self.dataprovider = WebScrapingDataProvider(headless=False)

    def coletar_dados(self):
        print('Username', USERNAME)
        print('Password', PASSWORD)

        self.dataprovider.login(login_url="https://inspectos.com/sistema/index.html#/home",
                                        username=USERNAME,
                                        password=PASSWORD)
        dados = self.dataprovider.raspar()
        return dados

if __name__ == "__main__":
    service = MainService()
    resultado = service.coletar_dados()
    print("Resultado da coleta:", resultado)