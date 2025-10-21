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

    def processar(self, usuario: Usuario):
        seguradoras_usuario = self.seguradora_service.listar_por_usuario(usuario.id_usuario)

        for seguradora in seguradoras_usuario:
            self.processar_scraping(seguradora)

    def processar_scraping(self, seguradora: Seguradora):
        match seguradora.identificador:
            case 'SWISS_RE':
                self.swiss_re_data_provider.login(seguradora.url_site, seguradora.senha_credencial, seguradora.user_credencial)
                dados = self.swiss_re_data_provider.raspar()

                for pericia in dados:
                    self.pericia_service.salvar(pericia=pericia)


