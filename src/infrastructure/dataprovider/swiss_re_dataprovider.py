import logging
import time
from operator import itemgetter
from typing import Optional

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from src.domain.pericia import Pericia

logger = logging.getLogger(__name__)


class SwissReDataProvider:

    def __init__(self, headless: Optional[bool] = True, timeout: int = 12):
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

        service = Service(ChromeDriverManager().install())
        try:
            self.driver = webdriver.Chrome(service=service, options=options)
        except WebDriverException:
            logger.exception("Erro ao iniciar WebDriver")
            raise

        self.wait = WebDriverWait(self.driver, timeout)

    def login(self, login_url: str, username: str, password: str):
        self.driver.get(login_url)
        email_input = self.wait.until(EC.presence_of_element_located((By.NAME, "email")))

        email_input.clear()
        email_input.send_keys(username)

        password_input = self.driver.find_element(By.NAME, "senha")
        password_input.clear()
        password_input.send_keys(password)

        self.driver.find_element(By.ID, "enter").click()

        print("Login enviado com sucesso!")

    def raspar(self):
        pericia_lista = []

        wait = WebDriverWait(self.driver, 15)

        entrar_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "(//div[contains(@class,'row')]/div[contains(@class,'col-3')])[2]//div[text()='ENTRAR']")
            )
        )

        entrar_btn.click()

        # Código produção

        # div_aguardando_aceite = wait.until(EC.element_to_be_clickable((
        #     By.XPATH,
        #     "//div[contains(@class, 'panel-heading')]"
        #     "[.//span[contains(text(), 'Aguardando Aceite')]]"
        #     "/following-sibling::div[contains(@class, 'panel-body')]"
        #     "//div[contains(@ng-click, 'filtrarInspecoesPorContador')]"
        # )))
        #
        # div_aguardando_aceite.click()

        # Codigo desenvolvimento

        aba_grid = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//ul[contains(@class, 'nav-tabs')]//span[contains(text(), 'GRID DE INSPEÇÃO')]")
        ))
        aba_grid.click()

        switch_button = wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR,
            "span.insp360-checklist-switch.switch[name='exibeInspecoesConcluidas']"
        )))
        switch_button.click()


        # ========================================

        tabela_pericias = wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "table.insp360-grid-primeira-tabela")
            )
        )
        tbody = tabela_pericias.find_element(By.TAG_NAME, "tbody")
        item_lista = tbody.find_elements(By.TAG_NAME, "tr")

        for item in item_lista:
            item.find_element(By.TAG_NAME, "td").click()

            modal = wait.until(EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, 'div[ng-show-360="exibeModal"]')
            ))

            wait.until(EC.visibility_of_element_located(
                (By.TAG_NAME, 'ng-template-modal-inspecao')
            ))

            #  Tabela 1
            seguradora = modal.find_elements(
                By.CSS_SELECTOR,
                'span[ng-if="campo == campoDinamicoResumo.seguradora"]')[1].text

            numero_proposta = modal.find_elements(
                By.CSS_SELECTOR,
                'span[ng-if="campo == campoDinamicoResumo.numero_proposta"]')[1].text

            numero_apolice = modal.find_elements(
                By.CSS_SELECTOR,
                'span[ng-if="campo == campoDinamicoResumo.numero_apolice"]')[1].text

            #  Tabela 2


            #  Tabela 3
            status = modal.find_element(
                By.CSS_SELECTOR,
                'span.label.insp360-grid-inspecao-status.insp360-status-inspecao-64'
            ).text

            print(f"seguradora: {seguradora}, n proposta: {numero_proposta}, n apolice: {numero_apolice}, status: {status}")

            #  Tabela 4
            #cultura
            #produtividade_esperada
            #numero_sinistro
            #evento

            #  Tabela Area Segurada


            #  Tabela Proponente
            div_proponente = modal.find_element(
                By.XPATH,
                "//div[contains(@ng-repeat, 'proponente in modal.proponentes')]"
            )

            cpf_cnpj = div_proponente.find_element(
                By.XPATH,
                ".//span[normalize-space(text())='CPF/CNPJ']/ancestor::div[contains(@class,'row')]/div[contains(@class,'col-xs-52')]//span"
            ).text

            #  Tabela Corretor
            corretor = modal.find_elements(
                By.CSS_SELECTOR,
                'span[ng-show-360="modal.corretor.telefones.length == 0"]')[1].text

            print(f"cpf_cnpj: {cpf_cnpj}, corretor: {corretor}")
            # print(f"tam: {len(cpf_cnpj)}, corretor: {corretor}")


            # created_at = str
            # data_empresa = str
            # categoria = str
            # tipo_vistoria = str
            # causa = str
            # segurado = str
            # numero_contato = str
            # municipio = str
            # uf = str
            # area = str
            # nome_analista = str
            # data_captura = str
            # cobertura = str


            pericia = Pericia(
                seguradora=seguradora,
                numero_proposta=numero_proposta,
                numero_apolice=numero_apolice,
                status=status,
                cpf_cnpj=cpf_cnpj,
                corretor=corretor,
            )
            pericia_lista.append(pericia)

            modal.find_element(By.CSS_SELECTOR, 'i[ng-click*="fecharModal"]').click()

        print("Parte 2 feita!")
        return pericia_lista

