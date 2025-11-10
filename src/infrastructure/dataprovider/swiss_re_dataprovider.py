import logging
import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from src.domain.pericia import Pericia

logger = logging.getLogger(__name__)


class SwissReDataProvider:
    def __init__(self, driver,):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 12)

    # ====================== LOGIN ======================
    def login(self, login_url: str, username: str, password: str):
        self.driver.get(login_url)
        email_input = self.wait.until(EC.presence_of_element_located((By.NAME, "email")))
        email_input.clear()
        email_input.send_keys(username)

        password_input = self.driver.find_element(By.NAME, "senha")
        password_input.clear()
        password_input.send_keys(password)

        self.driver.find_element(By.ID, "enter").click()
        print("✅ Login enviado com sucesso!")

    # ====================== RASPAGEM ======================
    def raspar(self):
        pericia_lista = []
        wait = self.wait

        # === Acessa seguradora ===
        seguradora_btn = wait.until(
            EC.presence_of_all_elements_located((
                By.XPATH,
                "//div[contains(@class, 'insp360-mouse-link') and contains(@class, 'clients')]"
            ))
        )[1]
        seguradora_btn.click()

        entrar_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "(//div[contains(@class,'row')]/div[contains(@class,'col-3')])[1]//div[text()='ENTRAR']")
            )
        )
        entrar_btn.click()

        # === Seleciona aba "Aguardando Aceite" ===
        div_aguardando_aceite = wait.until(EC.element_to_be_clickable((
            By.XPATH,
            "//div[contains(@class, 'panel-heading')]"
            "[.//span[contains(text(), 'Aguardando Aceite')]]"
            "/following-sibling::div[contains(@class, 'panel-body')]"
            "//div[contains(@ng-click, 'filtrarInspecoesPorContador')]"
        )))
        div_aguardando_aceite.click()

        # === Tabela principal ===
        wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "table.insp360-grid-primeira-tabela"))
        )

        # --- função auxiliar ---
        def extrair_pericias_da_pagina():
            print("🔄 Extraindo dados da página...")

            # Aguarda a tabela estar presente e visível
            time.sleep(1)  # Pequeno delay para garantir carregamento

            tbody = self.driver.find_element(By.CSS_SELECTOR, "table.insp360-grid-primeira-tabela tbody")
            linhas = tbody.find_elements(By.TAG_NAME, "tr")

            print(f"📊 {len(linhas)} registros encontrados nesta página")

            for index, item in enumerate(linhas, start=1):
                try:
                    item.find_element(By.TAG_NAME, "td").click()

                    modal = wait.until(EC.visibility_of_element_located(
                        (By.CSS_SELECTOR, 'div[ng-show-360="exibeModal"]')
                    ))

                    wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH, "//span[@class='insp360-exibe-textarea ng-binding']")
                    ))

                    # === coleta de dados ===
                    seguradora_nome = modal.find_elements(
                        By.CSS_SELECTOR,
                        'span[ng-if="campo == campoDinamicoResumo.seguradora"]')[1].text

                    numero_proposta = modal.find_elements(
                        By.CSS_SELECTOR,
                        'span[ng-if="campo == campoDinamicoResumo.numero_proposta"]')[1].text

                    numero_apolice = modal.find_elements(
                        By.CSS_SELECTOR,
                        'span[ng-if="campo == campoDinamicoResumo.numero_apolice"]')[1].text

                    spans = modal.find_elements(
                        By.XPATH, "//span[@class='insp360-exibe-textarea ng-binding']"
                    )
                    area_segurada_total = spans[1].text
                    numero_sinistro = spans[4].text
                    data_aviso_sinistro = spans[6].text
                    data_ocorrencia = spans[7].text
                    evento = spans[8].text
                    cultura = spans[9].text
                    produtividade_estimada = spans[10].text
                    numero_aviso = spans[11].text
                    cobertura_sinistrada = spans[12].text

                    div_proponente = modal.find_element(
                        By.XPATH, "//div[contains(@ng-repeat, 'proponente in modal.proponentes')]"
                    )
                    linha_nome_telefone = div_proponente.find_element(By.CSS_SELECTOR, 'div.row')
                    nome_proponente = linha_nome_telefone.find_elements(By.TAG_NAME, 'div')[1].text
                    telefone_proponente = linha_nome_telefone.find_elements(By.TAG_NAME, 'div')[3].text

                    cpf_cnpj_proponente = div_proponente.find_element(
                        By.XPATH,
                        ".//span[normalize-space(text())='CPF/CNPJ']/ancestor::div[contains(@class,'row')]/div[contains(@class,'col-xs-52')]//span"
                    ).text

                    nome_corretor = modal.find_elements(
                        By.CSS_SELECTOR,
                        'span[ng-show-360="modal.corretor.telefones.length == 0"]')[1].text

                    pericia = Pericia(
                        seguradora_nome=seguradora_nome,
                        numero_proposta=numero_proposta,
                        numero_apolice=numero_apolice,
                        area_segurada_total=area_segurada_total,
                        numero_sinistro=numero_sinistro,
                        data_aviso_sinistro=data_aviso_sinistro,
                        data_ocorrencia=data_ocorrencia,
                        evento=evento,
                        cultura=cultura,
                        produtividade_estimada=produtividade_estimada,
                        numero_aviso=numero_aviso,
                        cobertura_sinistrada=cobertura_sinistrada,
                        nome_proponente=nome_proponente,
                        telefone_proponente=telefone_proponente,
                        cpf_cnpj_proponente=cpf_cnpj_proponente,
                        nome_corretor=nome_corretor,
                    )

                    pericia_lista.append(pericia)
                    print(f"✅ {index}/{len(linhas)} perícia coletada nesta página")

                except Exception as e:
                    print(f"⚠️ Erro ao processar item {index}: {e}")
                    logger.exception(f"Erro detalhado ao processar item {index}")

                finally:
                    # Fecha o modal com segurança
                    try:
                        close_btn = self.driver.find_element(By.CSS_SELECTOR, 'i[ng-click*="fecharModal"]')
                        if close_btn.is_displayed():
                            close_btn.click()
                            time.sleep(0.5)  # Aumentado para garantir que o modal feche
                    except Exception:
                        pass

        # --- Loop de páginas ---
        pagina_atual = 1
        max_tentativas_proxima_pagina = 3

        while True:
            print(f"\n📄 Coletando página {pagina_atual}...")
            extrair_pericias_da_pagina()

            # Verifica se existe próxima página
            tem_proxima_pagina = False

            try:
                # Procura o botão de próxima página
                btn_proxima = self.driver.find_element(By.CSS_SELECTOR, "li.pagination-next a")
                parent_li = btn_proxima.find_element(By.XPATH, "..")

                # Verifica se o botão está desabilitado
                classes = parent_li.get_attribute("class") or ""
                if "disabled" in classes:
                    print("✅ Última página alcançada (botão desabilitado)")
                    break

                tem_proxima_pagina = True

            except NoSuchElementException:
                print("✅ Última página alcançada (botão não encontrado)")
                break

            # Tenta ir para a próxima página
            if tem_proxima_pagina:
                tentativa = 0
                sucesso = False

                while tentativa < max_tentativas_proxima_pagina and not sucesso:
                    try:
                        tentativa += 1
                        print(f"🔄 Tentativa {tentativa} de ir para página {pagina_atual + 1}...")

                        # Scroll até o botão
                        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn_proxima)
                        time.sleep(0.5)

                        # Pega referência da primeira linha da tabela atual
                        try:
                            tbody_antes = self.driver.find_element(
                                By.CSS_SELECTOR, "table.insp360-grid-primeira-tabela tbody"
                            )
                            primeira_linha_antes = tbody_antes.find_element(By.TAG_NAME, "tr")
                            texto_primeira_linha_antes = primeira_linha_antes.text
                        except:
                            texto_primeira_linha_antes = None

                        # Clica no botão
                        self.driver.execute_script("arguments[0].click();", btn_proxima)
                        print("🖱️ Clique executado, aguardando carregamento...")

                        # Aguarda um tempo fixo para a página processar
                        time.sleep(2)

                        # Verifica se a tabela foi atualizada (conteúdo diferente)
                        try:
                            tbody_depois = WebDriverWait(self.driver, 8).until(
                                EC.presence_of_element_located(
                                    (By.CSS_SELECTOR, "table.insp360-grid-primeira-tabela tbody")
                                )
                            )

                            # Aguarda ter pelo menos uma linha
                            WebDriverWait(self.driver, 5).until(
                                lambda d: len(d.find_elements(
                                    By.CSS_SELECTOR, "table.insp360-grid-primeira-tabela tbody tr"
                                )) > 0
                            )

                            # Verifica se o conteúdo mudou
                            primeira_linha_depois = tbody_depois.find_element(By.TAG_NAME, "tr")
                            texto_primeira_linha_depois = primeira_linha_depois.text

                            if texto_primeira_linha_antes and texto_primeira_linha_depois == texto_primeira_linha_antes:
                                print(f"⚠️ Conteúdo da tabela não mudou (tentativa {tentativa})")
                                time.sleep(1)
                                continue

                            pagina_atual += 1
                            print(f"✅ Navegou para página {pagina_atual}")
                            sucesso = True

                        except TimeoutException:
                            print(f"⚠️ Timeout ao aguardar atualização da tabela (tentativa {tentativa})")
                            time.sleep(1)

                    except Exception as e:
                        print(f"⚠️ Erro na tentativa {tentativa}: {str(e)[:100]}")
                        time.sleep(1)

                if not sucesso:
                    print(
                        f"❌ Não foi possível avançar para a próxima página após {max_tentativas_proxima_pagina} tentativas")
                    break

        print(f"\n🧾 Total de perícias coletadas: {len(pericia_lista)}")
        return pericia_lista