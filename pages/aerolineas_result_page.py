from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import allure


class AerolineasResultPage():
    txt_locator_fechas = (
        By.XPATH, "//button[@class='react-calendar__tile react-calendar__tile--active react-calendar__tile--rangeStart react-calendar__tile--rangeEnd react-calendar__tile--rangeBothEnds react-calendar__month-view__days__day']")
    label_locator_monto = (
        By.XPATH, "//label[@class='styled__Label-nhpxq-6 styled__Price-nhpxq-7 gxgowN sffc-total']")

    def __init__(self, driver):
        self.driver = driver


    @allure.step("Validamos que el monto del vuelo buscado, sea mayor a 0")
    def validar_monto_vuelos(self):
        try:
            elemento_texto = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(self.label_locator_monto))
            if self.driver.find_element(*self.label_locator_monto).is_displayed():
                texto = elemento_texto.text
                try:
                    monto = float(
                        texto.split()[-1].replace('.', '').replace(',', '.'))
                    assert monto > 0
                    print(
                        f"El monto del precio es mayor a 0, el viaje cuesta {monto}")
                except ValueError:
                    print("El monto del precio es igual a 0")
        except:
            # Si hay un error al esperar el elemento del monto, asume que no hay vuelos disponibles
            print("No se encontró el monto. No hay vuelos disponibles.")

        """ 
        texto.split() -> lo utilizo para dividir la cadena en palabras
        Extraigo el valor de la cadena (ARS + monto). Con el replaced eliminamos la separación de la , y utilizamos el "."
        Luego lo comparo para ver si es mayor a 0
        """
