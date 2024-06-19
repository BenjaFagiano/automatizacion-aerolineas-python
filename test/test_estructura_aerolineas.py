import pytest
import allure
from selenium import webdriver
from webdriver_manager import chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from time import sleep


class Test:
    # Locators

    btn_locator_aceptar_cookies = (
        By.XPATH, "//button[@type='cookies']//*[text()='Aceptar']")
    txt_locator_origen = (
        By.XPATH, "//*[@class='react-autosuggest__input suggestion-input-sb-origin']")
    txt_locator_destino = (
        By.XPATH, "//*[@class='react-autosuggest__input suggestion-input-sb-destination']")
    btn_locator_partida = (By.ID, 'from-date')  # Probar esto
    btn_locator_regreso = (By.ID, 'to-date')    # Probar esto
    slc_locator_clase_pasajeros = (By.ID, 'cabin-passengers')
    btn_locator_buscarvuelos = (By.XPATH, "//button[@name='search-flights']")
    btn_locator_centroAyuda = (
        By.XPATH, "//button[contains(text(), 'Centro de ayuda')]")
    txt_locator_comunicate = (
        By.XPATH, "//label[contains(text(), 'Comunicate con nosotros')]")
    btn_locator_contenidos = (
        By.XPATH, "//button[contains(text(), 'Contenidos Institucionales')]")
    btn_locator_suscribirme = (By.XPATH, "//a[contains(text(),'Suscribirme')]")

    # Test

    @allure.title("TC 1 - Validar los elementos desplegados en la pagina Aerolineas")
    @allure.description("Validar que se muestren los elementos desplegados en la pagina de Aerolineas Argentinas")
    @pytest.mark.P4
    def test_estructura_elementos(self, driver):
        with allure.step("Navegar en la pagina de Aerolineas Argentinas"):
            driver.get("https://www.aerolineas.com.ar/")

        with allure.step("Validar que se muestre el boton Aceptar cookies"):
            element_btn_aceptar_cookies = driver.find_element(
                *self.btn_locator_aceptar_cookies)
            assert element_btn_aceptar_cookies.is_displayed()
            element_btn_aceptar_cookies.click()  # Si no aparece que avance. Y poner mensaje

        with allure.step("Validar que se muestre el TextBox Origen"):
            element_txt_origen = driver.find_element(
                *self.txt_locator_origen)
            assert element_txt_origen.is_displayed()

        with allure.step("Validar que se muestre el TextBox Destino"):
            element_txt_destino = driver.find_element(
                *self.txt_locator_destino)
            assert element_txt_destino.is_displayed()

        with allure.step("Validar que se muestre el selector de fecha Partida"):
            element_btn_partida = driver.find_element(
                *self.btn_locator_partida)
            assert element_btn_partida.is_displayed()

        with allure.step("Validar que se muestre el selector de fecha Regreso"):
            element_btn_regreso = driver.find_element(
                *self.btn_locator_regreso)
            assert element_btn_regreso.is_displayed()

        with allure.step("Validar que se muestre el menu desplegable Clase/Pasajeros"):
            element_slc_clase_pasajeros = driver.find_element(
                *self.slc_locator_clase_pasajeros)
            assert element_slc_clase_pasajeros.is_displayed()

        with allure.step("Validar que se muestre el boton Buscar Vuelos"):
            element_btn_buscarvuelos = driver.find_element(
                *self.btn_locator_buscarvuelos)
            assert element_btn_buscarvuelos.is_displayed()

        with allure.step("Validar que se muestre el boton Centro de ayuda"):
            element_btn_centroAyuda = driver.find_element(
                *self.btn_locator_centroAyuda)
            assert element_btn_centroAyuda.is_displayed()

        with allure.step("Validar que se muestre el boton Comunicate con nosotros"):
            element_txt_comunicate = driver.find_element(
                *self.txt_locator_comunicate)
            assert element_txt_comunicate.is_displayed()

        with allure.step("Validar que se muestre el boton Contenidos institucionales"):
            element_btn_contenidos = driver.find_element(
                *self.btn_locator_contenidos)
            assert element_btn_contenidos.is_displayed()

        with allure.step("Validar que se muestre el TextBox Destino"):
            element_btn_suscribirme = driver.find_element(
                *self.btn_locator_suscribirme)
            assert element_btn_suscribirme.is_displayed()


if __name__ == "__main__":
    pytest.main()
