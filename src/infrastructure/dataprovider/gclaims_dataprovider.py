import logging
import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class GclaimsDataProvider:
    def __init__(self, driver):
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