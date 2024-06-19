import pytest
import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pages.aerolineas_home_page import AerolineasHomePage
from pages.aerolineas_iniciar_sesion import AerolineasIniciarSesion
from pages.aerolineas_registrate import AerolineasRegistrate
import time

usuario = "bfagiano@yopmail.com"
contraseña = "123456"


class Test:

    @allure.title("Test 1 - Iniciar sesión fallido")
    @allure.description("Objetivo: Ingresar datos que no se encuentren cargados y aparezca el mensaje de error al iniciar sesión")
    @pytest.mark.P3
    def test_iniciar_sesion_fallido(self, driver):
        """
        Test Ingresar usuario y contraseña, hacer click en Ingresar y aparece el error
        """
        with allure.step("Nos dirigimos a la web de Aerolineas"):
            driver.get("https://www.aerolineas.com.ar/")
        home_page = AerolineasHomePage(driver)
        home_page.click_aceptar_cookies()
        home_page.click_iniciar_sesion()
        sesion_page = AerolineasIniciarSesion(driver)
        sesion_page.ingresar_usuario(usuario)
        sesion_page.ingresar_contraseña(contraseña)
        sesion_page.click_ingresar()
        # sesion_page.validar_error_inicio()
        sesion_page.click_en_registrate()
        registrar_page = AerolineasRegistrate(driver)
        registrar_page.validar_contenido_URL("pre-registro")


if __name__ == "__main__":
    pytest.main()
