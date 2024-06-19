from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class OlvideMiContraseña:
    txt_ingresar_numero = (By.NAME, "membershipNumber")
    btn_aceptar = (By.XPATH, "//button[contains(text(),'Aceptar')]")
    btn_cancelar = (By.XPATH, "//button[contains(text(),'Cancelar')]")

    def __init__(self, driver):
        self.driver = driver

    def ingresar_numero(self, datos_registro):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.txt_ingresar_numero))
        assert self.driver.find_element(
            *self.txt_ingresar_numero).is_displayed()
        self.driver.find_element(
            *self.txt_ingresar_numero).send_keys(datos_registro)
