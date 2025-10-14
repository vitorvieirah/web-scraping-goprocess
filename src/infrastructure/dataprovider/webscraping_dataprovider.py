import logging
import time
from typing import Optional

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

logger = logging.getLogger(__name__)


class WebScrapingDataProvider:

    def __init__(self, headless: Optional[bool] = False, timeout: int = 12):
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

        time.sleep(5)
        print("Parte 2 feita!")


