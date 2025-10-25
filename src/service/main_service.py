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
    def __init__(self, usuario_service: UsuarioService, seguradora_service: SeguradoraService,
                 pericia_service: PericiaService):
        self.usuario_service = usuario_service
        self.seguradora_service = seguradora_service
        self.pericia_service = pericia_service

    def coletar_dados(self):
        usuarios = self.usuario_service.listar_usuarios()

        for index, usuario in enumerate(usuarios, start=1):
            print(f"\n=== Iniciando coleta para usuário {index}: {usuario.nome} ===")

            seguradoras_usuario = self.seguradora_service.listar_por_usuario(usuario.id_usuario)

            for seg_index, seguradora in enumerate(seguradoras_usuario, start=1):
                print(f"\n--- Processando seguradora {seg_index}: {seguradora.nome} ---")

                # 🔹 Novo navegador para cada seguradora
                swiss_re_data_provider = SwissReDataProvider(headless=True)

                try:
                    webscraping_service = WebscrapingService(
                        seguradora_service=self.seguradora_service,
                        swiss_re_data_provider=swiss_re_data_provider,
                        pericia_service=self.pericia_service
                    )

                    # 🔹 Agora processa apenas essa seguradora
                    webscraping_service.processar_scraping(seguradora)

                except Exception as e:
                    print(f"❌ Erro ao processar seguradora {seguradora.nome}: {e}")

                finally:
                    # Fecha o navegador com segurança
                    try:
                        swiss_re_data_provider.close()
                    except Exception:
                        pass
                    try:
                        swiss_re_data_provider.driver.quit()
                        print(f"✅ Navegador fechado para seguradora {seguradora.nome}.")
                    except Exception:
                        print(f"⚠️ Falha ao fechar o navegador da seguradora {seguradora.nome}.")

    def cadastrar_seguradora(self):
        self.seguradora_service.cadastrar()

    def listar_seguradoras(self):
        id_usuario = int(input("Informe o ID do usuário: "))
        seguradoras_lista = self.seguradora_service.listar_por_usuario(id_usuario)
        print(f"Seguradoras: {seguradoras_lista}")


if __name__ == "__main__":
    db = SessionLocal()
    mapper = SeguradoraMapper()

    usuario_data_provider = UsuarioDataProvider()
    pericia_data_provider = PericiaDataprovider()
    seguradora_data_provider = SeguradoraDataProvider(mapper, FERNET_KEY)

    usuario_service = UsuarioService(usuario_data_provider)
    pericia_service = PericiaService(pericia_data_provider)
    seguradora_service = SeguradoraService(seguradora_data_provider)

    service = MainService(usuario_service, seguradora_service, pericia_service)

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
