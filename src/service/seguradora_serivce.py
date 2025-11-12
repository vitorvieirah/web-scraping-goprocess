from src.infrastructure.dataprovider.seguradora_dataprovider import SeguradoraDataProvider
from src.domain.seguradora import Seguradora
from src.domain.identificador_seguradora import IdentificadorSeguradora
from src.infrastructure.mapper.mapper_seguradora import SeguradoraMapper
from src.config.settings import FERNET_KEY


class SeguradoraService:
    def __init__(self, data_provider: SeguradoraDataProvider):
        self.data_provider = data_provider


    def listar_por_usuario(self, id_usuario):
        return self.data_provider.listar_por_usuario(id_usuario)

    def cadastrar(self):
        print("=== Cadastro de Seguradora ===")

        nome = input("Nome da seguradora: ")
        usuario_credencial = input("Usuário: ")
        senha_credencial = input("Senha: ")
        usuario_id = int(input("ID do usuário: "))
        url_site = input("URL do site: ")

        # Mostra as opções de identificadores disponíveis
        print("\nSelecione o identificador da seguradora:")
        identificadores = list(IdentificadorSeguradora)
        for i, identificador in enumerate(identificadores, start=1):
            print(f"{i}. {identificador.value}")

        # Captura a escolha do usuário
        while True:
            try:
                escolha = int(input("Escolha (número): "))
                if 1 <= escolha <= len(identificadores):
                    identificador_escolhido = identificadores[escolha - 1]
                    break
                else:
                    print("❌ Opção inválida. Tente novamente.")
            except ValueError:
                print("❌ Digite um número válido.")

        seguradora = Seguradora(
            id_seguradora=None,
            nome=nome,
            user_credencial=usuario_credencial,
            senha_credencial=senha_credencial,
            usuario_id=usuario_id,
            identificador=identificador_escolhido,
            url_site=url_site,
        )

        mapper = SeguradoraMapper()
        data_provider = SeguradoraDataProvider(mapper, FERNET_KEY)

        resultado = data_provider.salvar(seguradora)
        print(f"\n✅ Seguradora '{resultado.nome}' cadastrada com sucesso!")
        print(f"Usuário criptografado: {resultado.user_credencial}")
        print(f"Senha criptografada: {resultado.senha_credencial}")
