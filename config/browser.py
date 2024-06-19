# browser.py
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager as EdgeDriverManager
from selenium.webdriver.chrome.service import Service


class BrowserConfig:

    """
    Clase para configurar el navegador que se usará en las pruebas.
    ejemplo:
    browser = BrowserConfig('chrome').select_browser()
    """

    def __init__(self, browser):

        self.BROWSER = browser
        self.driver = None

    def select_browser(self):
        """
        Método para seleccionar el navegador que se usará en las pruebas.
        """
        if self.BROWSER == 'firefox':
            self.driver = webdriver.Firefox(
                service=Service(GeckoDriverManager().install()))
        elif self. BROWSER == 'chrome':
            self.driver = webdriver.Chrome(service=Service(
                ChromeDriverManager().install()))
        elif self. BROWSER == 'chrome-headless':
            self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                           options=self.chrome_headless_options())
        elif self. BROWSER == 'edge':
            self.driver = webdriver.Edge(service=Service(
                EdgeDriverManager().install()))
        else:
            raise ValueError(f'--browser="{self.BROWSER}" no esta definido')
        return self.driver
