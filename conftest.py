# conftest.py
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from config.browser import BrowserConfig
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta
import os


def pytest_addoption(parser):
    """
    Agregar opciones de línea de comandos para seleccionar el navegador
    """
    parser.addoption("--browser", action="store", default="chrome",
                     help="Escoger navegador: chrome o edge")
    parser.addoption("--destino", action="store", default="nacional",
                     help="Escoger destino: nacional o internacional")


def pytest_configure(config):
    os.environ["destino"] = config.getoption("destino")
    os.environ["browser"] = config.getoption("browser")


@pytest.fixture(autouse=True)
def driver(request):
    """
    Fixture para inicializar el driver del navegador
    """
    browser_seleccionado = request.config.getoption("--browser")
    driver = BrowserConfig(browser_seleccionado).select_browser()
    driver.maximize_window()
    # Retorna el objeto driver para las pruebas que lo necesiten (yield es como un return pero no cierra el driver)
    yield driver
    print("Cerrar Browser")
    driver.quit()


@pytest.fixture
def datos_inicio_sesion():
    return ["bfagiano@yopmail.com", "123456"]


@pytest.fixture
def num_aerolineas_plus():
    return [""]


@pytest.fixture
def datos_registro():
    return ["Benjamin", "Fagiano", "29/04/1990", "35134359", "bfagiano@yopmail.com"]


@pytest.fixture
def sumar_dias_salida():
    # Toma la fecha de hoy y le suma 2 días
    hoy = datetime.now()
    fecha = hoy + timedelta(days=2)
    return fecha.strftime('%d/%m/%Y')


@pytest.fixture
def sumar_dias_regreso():
    # Toma la fecha de hoy y le suma 2 días
    hoy = datetime.now()
    fecha = hoy + timedelta(days=20)
    return fecha.strftime('%d/%m/%Y')


@pytest.fixture
def fecha_salida():
    # Toma la fecha de hoy y suma un mes
    hoy = datetime.now()
    fecha = hoy + relativedelta(months=1)
    return fecha.strftime('%d/%m/%Y')


@pytest.fixture
def fecha_regreso():
    # Toma la fecha de hoy y suma un mes
    hoy = datetime.now()
    fecha = hoy + relativedelta(months=1) + timedelta(days=7)
    return fecha.strftime('%d/%m/%Y')

@pytest.fixture
def fecha_salida_br():
    fecha = datetime(2025,5,5)
    return fecha.strftime('%d/%m/%Y')


@pytest.fixture
def fecha_regreso_br():
    fecha = datetime(2025, 5, 5) + relativedelta(days=7)
    return fecha.strftime('%d/%m/%Y')
