from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import re

from src.domain.pericia import Pericia


class GclaimsDataProvider:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    # ====================== LOGIN ======================
    def login(self, login_url: str, username: str, password: str):
        self.driver.get(login_url)
        email_input = self.wait.until(EC.presence_of_element_located((By.ID, "txtNomeUsuario")))
        email_input.clear()
        email_input.send_keys(username)

        password_input = self.driver.find_element(By.ID, "txtPassword")
        password_input.clear()
        password_input.send_keys(password)

        self.driver.find_element(By.ID, "btn_login").click()
        print("✅ Login enviado com sucesso!")

    # ====================== RASPAGEM ======================
    def raspar(self):
        global main_window
        pericia_lista = []

        self.wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, ".col-sm-4.col-xs-12.col-md-3.col-lg-2.ng-scope")
            )
        )

        pericias_list = self.driver.find_elements(
            By.CSS_SELECTOR,
            "#tab-vistorias-aguardando-aceite .col-sm-4.col-xs-12.col-md-3.col-lg-2.ng-scope"
        )

        for i, pericia in enumerate(pericias_list):
            try:
                print(f"🔍 Processando perícia {i + 1} de {len(pericias_list)}")

                # Salva a aba principal
                main_window = self.driver.current_window_handle

                numero_sinistro = pericia.find_element(By.TAG_NAME, "h4").text.strip()

                # === Endereço ===
                endereco_div = pericia.find_element(By.XPATH, ".//div[b[normalize-space(text())='Endereço']]")
                endereco_texto = endereco_div.text.split("\n", 1)[1].strip()
                match = re.search(r'([A-Za-zÀ-ÿ\s]+)/([A-Z]{2})', endereco_texto)

                municipio = match.group(1).strip() if match else None
                uf = match.group(2).strip() if match else None

                # === Dados principais ===
                dados = {
                    "Cobertura": None,
                    "Data de Aviso": None,
                    "Data da ocorrência": None,
                    "Seguradora": None,
                    "Contato Segurado": None,
                    "Nro Apolice": None,
                    "Área plantada": None,
                    "Cultura": None
                }

                segurado_div = pericia.find_element(By.XPATH, ".//div[b[normalize-space(text())='Segurado']]")
                segurado = segurado_div.text.split("\n", 1)[1].strip()

                info_divs = pericia.find_elements(
                    By.XPATH,
                    ".//div[@ng-repeat='item in (surveyDispatchToMe.CardMeta || [])']"
                )

                for div in info_divs:
                    partes = div.text.split("\n", 1)
                    if len(partes) == 2:
                        chave, valor = partes
                        chave, valor = chave.strip(), valor.strip()
                        chave_normalizada = chave.lower().replace("º", "").replace("ó", "o").replace("á", "a")

                        for campo in dados.keys():
                            if campo.lower().replace("º", "").replace("ó", "o").replace("á", "a") in chave_normalizada:
                                dados[campo] = valor

                # Clica no link para abrir a nova aba
                link_element = pericia.find_element(By.XPATH, ".//a[contains(@href, '/External/Survey/Info')]")
                link_element.click()

                # Aguarda a nova aba abrir e muda o foco para ela
                time.sleep(3)
                windows = self.driver.window_handles

                self.driver.switch_to.window(windows[-1])

                processo = None
                data_entrada = None

                # ========== BUSCA DO PROCESSO ==========
                tentativas_processo = [
                    (By.CSS_SELECTOR, 'input[ng-model="claim.ClaimCode"]'),
                    (By.XPATH, '//input[@ng-model="claim.ClaimCode"]'),
                    (By.XPATH, '//label[contains(text(), "Processo")]/following-sibling::input'),
                    (By.XPATH, '//div[contains(@class, "form-group")]//label[contains(text(), "Processo")]/../input')
                ]

                for tentativa, locator in enumerate(tentativas_processo, 1):
                    try:
                        processo_input = WebDriverWait(self.driver, 10).until(
                            EC.presence_of_element_located(locator)
                        )
                        # Aguarda o Angular preencher o valor
                        for wait_attempt in range(10):
                            processo = processo_input.get_attribute("value")
                            if processo and processo.strip():
                                print(f"✅ Processo encontrado: {processo}")
                                break
                            time.sleep(1)
                        else:
                            print("⚠️ Input de processo encontrado mas valor está vazio")
                            continue
                        break
                    except (TimeoutException, NoSuchElementException) as e:
                        print(f"❌ Tentativa {tentativa} falhou: {e}")
                        continue

                if not processo:
                    print("❌ Não foi possível obter o número do processo")
                    processo = "N/A"

                # ========== BUSCA DA DATA DE ENTRADA ==========
                tentativas_data_entrada = [
                    (By.XPATH, '//label[contains(text(), "Data Entrada")]/following-sibling::div//input'),
                    (By.XPATH,
                     '//div[contains(@class, "form-group")]//label[contains(text(), "Data Entrada")]/../div//input'),
                    (By.XPATH,
                     '//div[contains(@class, "input-group") and .//label[contains(text(), "Data Entrada")]]//input'),
                    (By.CSS_SELECTOR, 'div.input-group[ng-model="claim.ReceivedDate"] input')
                ]

                for tentativa, locator in enumerate(tentativas_data_entrada, 1):
                    try:
                        data_entrada_input = WebDriverWait(self.driver, 10).until(
                            EC.presence_of_element_located(locator)
                        )
                        # Aguarda o Angular preencher o valor
                        for wait_attempt in range(10):
                            data_entrada = data_entrada_input.get_attribute("value")
                            if data_entrada and data_entrada.strip():
                                print(f"✅ Data de entrada encontrada: {data_entrada}")
                                break
                            time.sleep(1)
                        else:
                            print("⚠️ Input de data de entrada encontrado mas valor está vazio")
                            continue
                        break
                    except (TimeoutException, NoSuchElementException) as e:
                        print(f"❌ Tentativa {tentativa} falhou: {e}")
                        continue

                if not data_entrada:
                    print("❌ Não foi possível obter a data de entrada")
                    data_entrada = "N/A"

                # ========== CONCATENA PROCESSO + DATA ENTRADA ==========
                # Garante que as variáveis são strings
                processo_str = str(processo).strip() if processo else "N/A"
                data_entrada_str = str(data_entrada).strip() if data_entrada else "N/A"

                if processo_str != "N/A" and data_entrada_str != "N/A":
                    # Formata a data: remove barras, dois pontos e substitui espaços por underline
                    data_formatada = data_entrada_str.replace('/', '').replace('-', '').replace(':', '').replace(' ', '_').strip()
                    identificador_unico = f"{processo_str}_{data_formatada}"
                else:
                    identificador_unico = processo_str if processo_str != "N/A" else f"SINISTRO_{i+1}"
                    print(f"⚠️ Usando fallback para identificador: {identificador_unico}")

                self.driver.close()
                self.driver.switch_to.window(main_window)


                self.wait.until(
                    EC.presence_of_all_elements_located(
                        (By.CSS_SELECTOR, ".col-sm-4.col-xs-12.col-md-3.col-lg-2.ng-scope")
                    )
                )

                # === Cria objeto Pericia ===
                pericia_obj = Pericia(
                    seguradora_nome=dados["Seguradora"],
                    numero_apolice=dados["Nro Apolice"],
                    nome_proponente=segurado,
                    telefone_proponente=dados["Contato Segurado"],
                    area_segurada_total=dados["Área plantada"],
                    cultura=dados["Cultura"],
                    data_aviso_sinistro=dados["Data de Aviso"],
                    data_ocorrencia=dados["Data da ocorrência"],
                    cobertura_sinistrada=dados["Cobertura"],
                    numero_sinistro=numero_sinistro,
                    identificador_unico=identificador_unico,  # Usando processo + data como identificador
                    uf=uf,
                    municipio=municipio,
                )

                pericia_lista.append(pericia_obj)
                print(f"✅ Perícia {identificador_unico} coletada com sucesso!\n")

            except Exception as e:
                print(f"❌ Erro ao processar perícia {i + 1}: {e}")
                try:
                    self.driver.switch_to.window(main_window)
                except:
                    pass
                continue

        print(f"\n🧾 Total de perícias coletadas: {len(pericia_lista)}")
        return pericia_lista