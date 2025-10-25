from src.domain.seguradora import Seguradora
from src.domain.usuario import Usuario
from src.infrastructure.dataprovider.swiss_re_dataprovider import SwissReDataProvider
from src.service.pericia_service import PericiaService
from src.service.seguradora_serivce import SeguradoraService


class WebscrapingService:
    def __init__(self, seguradora_service: SeguradoraService, swiss_re_data_provider: SwissReDataProvider, pericia_service: PericiaService):
        self.seguradora_service = seguradora_service
        self.swiss_re_data_provider = swiss_re_data_provider
        self.pericia_service = pericia_service

    def processar_scraping(self, seguradora: Seguradora):
        print(f"Iniciando scraping da seguradora: {seguradora.nome}")

        match seguradora.identificador.value:
            case 'SWISS_RE':
                self.swiss_re_data_provider.login(
                    login_url=seguradora.url_site,
                    password=seguradora.senha_credencial,
                    username=seguradora.user_credencial
                )

                dados = self.swiss_re_data_provider.raspar()

                for pericia in dados:
                    pericia.usuario_id = seguradora.usuario_id
                    pericia.seguradora_id = seguradora.id_seguradora
                    self.pericia_service.salvar(pericia=pericia)

        print(f"✅ Finalizado scraping da seguradora: {seguradora.nome}")


