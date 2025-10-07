from selenium import webdriver

class WebScrapingDataProvider:

    def raspar(self):
        driver = webdriver.Chrome()
        driver.get("https://inspectos.com/sistema/index.html#/home")