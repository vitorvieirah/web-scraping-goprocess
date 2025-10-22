from src.config.database import Base, engine, SessionLocal
from src.infrastructure.dataprovider.swiss_re_dataprovider import SwissReDataProvider
from src.infrastructure.dataprovider.usuario_dataprovider import UsuarioDataProvider
from src.infrastructure.dataprovider.pericia_dataprovider import PericiaDataprovider
from src.service.pericia_service import PericiaService
from src.service.usuario_service import UsuarioService
from src.service.webscraping_service import WebscrapingService
from src.service.seguradora_serivce import SeguradoraService
from src.infrastructure.mapper.mapper_seguradora import SeguradoraMapper
from src.infrastructure.dataprovider.seguradora_dataprovider import SeguradoraDataProvider
from src.config.settings import FERNET_KEY

Base.metadata.create_all(engine)

class MainService:
    def __init__(self, usuario_service: UsuarioService, webscraping_service: WebscrapingService,
                 seguradora_service: SeguradoraService):
        self.usuario_service = usuario_service
        self.webscraping_service = webscraping_service
        self.seguradora_service = seguradora_service

    def coletar_dados(self):
        usuarios = self.usuario_service.listar_usuarios()
        for usuario in usuarios:
            self.webscraping_service.processar(usuario)

    def cadastrar_seguradora(self):
        self.seguradora_service.cadastrar()

    def listar_seguradoras(self):
        id_usuario = int(input("Informe o ID do usuário: "))
        seguradoras_lista = self.seguradora_service.listar_por_usuario(id_usuario)
        print(f"seguradoras: {seguradoras_lista}")


if __name__ == "__main__":
    db = SessionLocal()

    mapper = SeguradoraMapper()

    usuario_data_provider = UsuarioDataProvider()
    pericia_data_provider = PericiaDataprovider()
    seguradora_data_provider = SeguradoraDataProvider(mapper, FERNET_KEY)
    swiss_re_data_provider = SwissReDataProvider(headless=False)

    # Cria os services
    usuario_service = UsuarioService(usuario_data_provider)
    pericia_service = PericiaService(pericia_data_provider)
    seguradora_service = SeguradoraService(seguradora_data_provider)

    # você precisa inicializar esses outros também
    webscraping_service = WebscrapingService(seguradora_service, swiss_re_data_provider, pericia_service)

    service = MainService(usuario_service, webscraping_service, seguradora_service)



    # Injeta dependências no WebscrapingService
    webscraping_service = WebscrapingService(
        seguradora_service=seguradora_service,
        swiss_re_data_provider=swiss_re_data_provider,
        pericia_service=pericia_service
    )

    print("\n=== MENU ===")
    print("1. Cadastrar Seguradora")
    print("2. Listar Seguradoras")
    print("3. Rodar automação")
    opcao = input("Escolha: ")

    if opcao == "1":
        service.cadastrar_seguradora()
    elif opcao == "2":
        service.listar_seguradoras()
    elif opcao == "3":
        service.coletar_dados()
    else:
        print("Opção inválida!")