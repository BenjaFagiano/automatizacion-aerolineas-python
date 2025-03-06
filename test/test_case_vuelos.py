import pytest
import allure
from pages.aerolineas_home_page import AerolineasHomePage
from pages.aerolineas_result_page import AerolineasResultPage
from utils.data_driven import DatosConfig
import os


destino = os.getenv("destino")
DATOS_LISTA = DatosConfig(destino).obtener_datos_origen_destino_lista()


class Test:
    """
    Clase para realizar test de buscar vuelos
    """
    @allure.title("Validar que permita buscar vuelos")
    @allure.description("Validar que se completen todos los datos y permite buscar vuelos a distintos destinos")
    @pytest.mark.parametrize("Origen, Origen_buscado, Destino, Destino_buscado, Url", DATOS_LISTA)
    def test_buscar_vuelos_internacionales(self, driver, Origen, Origen_buscado, Destino, Destino_buscado, Url, fecha_salida_br, fecha_regreso_br):
        with allure.step("Nos dirigimos a la página de Aerolineas Argentinas"):
            driver.get(Url)
        home_page = AerolineasHomePage(driver)
        home_page.click_aceptar_cookies()
        home_page.ingresar_origen(Origen, Origen_buscado)
        home_page.ingresar_destino(Destino, Destino_buscado)
        home_page.ingresar_fecha_partida(fecha_salida_br)
        home_page.ingresar_fecha_regreso(fecha_regreso_br)
        home_page.cantidad_pasajeros()
        home_page.buscar_vuelos()
        result_page = AerolineasResultPage(driver)
        result_page.validar_monto_vuelos()


if __name__ == "__main__":
    pytest.main()
