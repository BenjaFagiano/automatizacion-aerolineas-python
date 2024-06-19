import pytest
import allure
from pages.aerolineas_home_page import AerolineasHomePage
from utils.data_driven import DatosConfig
import os


def datos_vuelo_nacional():
    destino = os.getenv("destino")
    datos = DatosConfig(destino)
    return datos.obtener_datos_xlsx("Hoja1")


class Test:
    """
    Clase para realizar test de buscar vuelos
    """
    @allure.title("Validar que permita buscar vuelos")
    @allure.description("Validar que se completen todos los datos y permite buscar vuelos a distintos destinos")
    @pytest.mark.P1
    @pytest.mark.parametrize("Origen, Destino", datos_vuelo_nacional())
    def test_buscar_vuelos(self, driver, Origen, Destino, sumar_dias_salida, sumar_dias_regreso):
        """
        Test para validar que se busque vuelos
        """
        with allure.step("Nos dirigimos a la página de Aerolineas Argentinas"):
            driver.get("https://www.aerolineas.com.ar/")
        home_page = AerolineasHomePage(driver)
        home_page.click_aceptar_cookies()
        home_page.ingresar_orgien(Origen)
        home_page.ingresar_destino(Destino)
        home_page.ingresar_fecha_partida(sumar_dias_salida)
        home_page.ingresar_fecha_regreso(sumar_dias_regreso)
        home_page.buscar_vuelos()


if __name__ == "__main__":
    pytest.main()
