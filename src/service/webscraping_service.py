from ..infrastructure.dataprovider.webscraping_dataprovider import WebScrapingDataProvider

class WebScrapingService:

    def __init__(self, dataprovider: WebScrapingDataProvider):
        self.dataprovider = dataprovider

    def coletar_dados(self):
        dados = self.dataprovider.raspar()
        return dados