from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class RecuperarNumeroSocio:
    slc_tipo_documento = (By.XPATH, "//div[@class='css-10nd86i']")
    txt_ingresar_numero = (By.NAME, "numberOfIdentification")
    txt_fecha_nacimiento = (By.NAME, "dateOfBirth")
    btn_aceptar = (By.XPATH, "//button[contains(text(),'Aceptar')]")
    btn_cancelar = (By.XPATH, "//button[contains(text(),'Cancelar')]")

    def __init__(self, driver):
        self.driver = driver
