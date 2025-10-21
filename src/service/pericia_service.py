from src.domain.pericia import Pericia
from src.infrastructure.dataprovider.pericia_dataprovider import PericiaDataprovider


class PericiaService:
    def __init__(self, data_provider: PericiaDataprovider):
        self.data_provider = data_provider


    def salvar(self, pericia: Pericia):
        return self.data_provider.salvar(pericia)


