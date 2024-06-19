import pytest
import allure
from pages.aerolineas_home_page import AerolineasHomePage
from pages.aerolineas_iniciar_sesion import AerolineasIniciarSesion
from pages.aerolineas_registrate import AerolineasRegistrate
from pages.aerolineas_olvide_contraseña import OlvideMiContraseña
from pages.aerolineas_recuperar_numero import RecuperarNumeroSocio


class Test:
    """
    Clase para realizar test de registrarse e iniciar sesión
    """
    @allure.title("Validar que permita iniciar sesión")
    @allure.description("Validar que se completen todos los datos y permite iniciar sesión")
    @pytest.mark.P1
    def test_iniciar_sesion(self, driver, datos_inicio_sesion):
        """
        Test para validar que se inicie sesión
        """
        with allure.step("Nos dirigimos a la página de Aerolineas Argentinas"):
            driver.get("https://www.aerolineas.com.ar/")
        home_page = AerolineasHomePage(driver)
        home_page.click_aceptar_cookies()
        home_page.click_iniciar_sesion()
        iniciar_page = AerolineasIniciarSesion(driver)
        iniciar_page.ingresar_usuario(datos_inicio_sesion[0])
        iniciar_page.ingresar_contraseña(datos_inicio_sesion[1])

    @allure.title("Validar que permita registrarse")
    @allure.description("Se ingresan los datos para poder registrarse en la página de Aerolineas")
    @pytest.mark.P1
    # Verificar si se puede agregar el sumar días (Ver clase de nuevo)
    def test_registrate(self, driver, datos_registro):
        """
        Test para validar el correcto registro
        """
        with allure.step("Nos dirigimos a la página de Aerolineas Argentinas"):
            driver.get("https://www.aerolineas.com.ar/")
        home_page = AerolineasHomePage(driver)
        home_page.click_aceptar_cookies()
        home_page.click_iniciar_sesion()
        iniciar_page = AerolineasIniciarSesion(driver)
        registrate_page = AerolineasRegistrate(driver)
        iniciar_page.click_en_registrate()
        home_page.validar_contenido_URL("pre-registro")
        registrate_page.ingresar_nombre(datos_registro[0])
        registrate_page.ingresar_apellido(datos_registro[1])
        registrate_page.ingresar_fecha_nacimiento(datos_registro[2])
        registrate_page.seleccionar_documento()
        registrate_page.ingresar_numero_documento(datos_registro[3])
        registrate_page.ingresar_email(datos_registro[4])
        registrate_page.click_aceptar()
        registrate_page.mensaje_pre_inscripcion()

    @allure.title("Validar que pueda recuperar el número de Aerolineas Plus")
    @allure.description("Luego de presionar click en el botón Olvide mi número de Aerolineas Plus")
    @pytest.mark.P2
    def test_olvide_minumero(self, driver):
        """
        Test para validar el recupero del número de Aerolineas Plus
        """
        with allure.step("Nos dirigimos a la página de Aerolineas Argentinas"):
            driver.get("https://www.aerolineas.com.ar/")
        home_page = AerolineasHomePage(driver)
        home_page.click_aceptar_cookies()
        home_page.click_iniciar_sesion()
        iniciar_page = AerolineasIniciarSesion(driver)
        iniciar_page.click_olvide_minumero()
        home_page.validar_contenido_URL("recuperar-numero-de-socio")

    @allure.title("Validar que pueda recuperar la contraseña")
    @allure.description("Recuperar la contraseña con el número de Aerolineas Plus")
    @pytest.mark.P2
    def test_olvide_contraseña(self, driver):
        """
        Test para validar el recupero la contraseña
        """
        with allure.step("Nos dirigimos a la página de Aerolineas Argentinas"):
            driver.get("https://www.aerolineas.com.ar/")
        home_page = AerolineasHomePage(driver)
        home_page.click_aceptar_cookies()
        home_page.click_iniciar_sesion()
        iniciar_page = AerolineasIniciarSesion(driver)
        iniciar_page.click_olvide_contraseña()
        home_page.validar_contenido_URL("olvide-mi-clave")


if __name__ == "__main__":
    pytest.main()
