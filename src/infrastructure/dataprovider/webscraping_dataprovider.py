import logging
import os
import time
from typing import List, Dict, Optional
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException

logger = logging.getLogger(__name__)

class WebScrapingDataProvider:

    """
    WebScrapingDataProvider (Selenium)
    - Inicia o Chrome via webdriver-manager (evita lidar com chromedriver manual).
    - Recebe configurações de seletores (ex.: CSS para campo usuário/senha/botão) e o login_url.
    - Usa WebDriverWait + expected_conditions para robustez.
    - Faz login, valida sucesso (espera algum elemento), e então raspa os itens.
    - Exporta os dados como List[dict] para o Service.
    """

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

        time.sleep(5)
        print("Login enviado com sucesso!")
