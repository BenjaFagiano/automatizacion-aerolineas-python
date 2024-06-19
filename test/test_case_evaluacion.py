import pytest
import allure
from pages.aerolineas_home_page import AerolineasHomePage
from pages.aerolineas_result_page import AerolineasResultPage
from utils.data_driven import DatosConfig
import os


def datos_vuelo_nacional():
    destino = os.getenv("destino")
    datos = DatosConfig(destino)
    return datos.obtener_datos_xlsx("evaluacion")


class Test:
    destino = os.getenv("destino")
    DATOS_LISTA = DatosConfig(destino).obtener_datos_origen_destino_lista()

    """
    Clase del test de la evaluación
    """
    @allure.title("Evaluación Clase 8")
    @allure.description("Evaluación: Verificar que existan vuelos para 2 personas")
    @pytest.mark.skip
    @pytest.mark.parametrize("Origen, Destino, Url", datos_vuelo_nacional())
    def test_buscar_vuelos_evaluacion(self, driver, Origen, Destino, Url, fecha_salida, fecha_regreso):
        with allure.step("Nos dirigimos a la página de Aerolineas Argentinas"):
            driver.get(Url)
        home_page = AerolineasHomePage(driver)
        home_page.click_aceptar_cookies()
        home_page.pestaña_vuelos()
        home_page.ida_y_vuelta()
        home_page.ingresar_orgien(Origen)
        home_page.ingresar_destino(Destino)
        home_page.ingresar_fecha_partida(fecha_salida)
        home_page.ingresar_fecha_regreso(fecha_regreso)
        home_page.cantidad_pasajeros()
        home_page.buscar_vuelos()
        result_page = AerolineasResultPage(driver)
        result_page.validar_monto_vuelos()

    @allure.title("Test verificar autocompletado")
    @allure.description("Test para verificar que si muestra una lista, muestre todos los elementos y seleccione el deseado")
    @pytest.mark.parametrize("Origen, Origen_buscado, Destino, Destino_buscado, Url", DATOS_LISTA)
    def test_validar_autocompletado(self, driver, Origen, Origen_buscado, Destino, Destino_buscado, Url):
        with allure.step("Nos dirigimos a la página de Aerolineas Argentinas"):
            driver.get(Url)
        home_page = AerolineasHomePage(driver)
        home_page.click_aceptar_cookies()
        home_page.ingresar_orgien(Origen, Origen_buscado)
        home_page.ingresar_destino(Destino, Destino_buscado)


if __name__ == "__main__":
    pytest.main()
