from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import time


class AerolineasHomePage():
    btn_locator_aceptar_cookies = (
        By.XPATH, "//button[@type='cookies']//*[text()='Aceptar']")
    txt_locator_origen = (
        By.XPATH, "//input[@placeholder='Origen']")
    txt_locator_destino = (
        By.XPATH, "//input[@placeholder='Destino']")
    btn_locator_partida = (By.ID, "from-date")
    btn_locator_regreso = (By.ID, "to-date")
    slc_locator_clase_pasajeros = (By.ID, "cabin-passengers")
    slc_locator_clase_lista = (By.ID, "cabin-passengers-list")
    btn_locator_agregar_pasajeros = (
        By.XPATH, "//button[@class='styled__IconContainer-sc-1sy3ra0-1 eoncfD add-adt']")
    btn_locator_buscarvuelos = (By.ID, "search-flights")
    btn_locator_iniciar_sesion = (
        By.XPATH, "//*[@class='styled__LoginLabel-sc-22nvvu-14 hcmvtN menu-login']")
    locator_pestaña_vuelos = (By.XPATH, "//a[contains(text(),'VUELOS')]")
    locator_radio_ida_vuelta = (
        By.XPATH, "//div[@class='styled__RadioCheck-i11vkm-2 XHVSa']")
    list_locator_origen_destino = (
        By.XPATH, "//ul[@role='listbox']//li[@role='option']")

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Hacemos click en el botón de aceptar cookies")
    def click_aceptar_cookies(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.btn_locator_aceptar_cookies))
        if self.driver.find_element(*self.btn_locator_aceptar_cookies).is_displayed():
            self.driver.find_element(*self.btn_locator_aceptar_cookies).click()
        else:
            print("No se pudo hacer click en Aceptar cookies")

    @allure.step("Validamos que la pestaña contenga la palabra Vuelos")
    def pestaña_vuelos(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locator_pestaña_vuelos))
        assert self.driver.find_element(
            *self.locator_pestaña_vuelos).is_displayed()
        print("Se encuentra seleccionada la pestaña Vuelos")

    @allure.step("Validamos que este seleccionado el radio button Ida y Vuelta")
    def ida_y_vuelta(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locator_radio_ida_vuelta))
        assert self.driver.find_element(
            *self.locator_radio_ida_vuelta).is_displayed()
        print("Elección de vuelo Ida y Vuelta")

    @allure.step("Ingresamos un Origen")
    def ingresar_orgien(self, Origen, Origen_buscado):
        assert WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.txt_locator_origen))
        assert self.driver.find_element(
            *self.txt_locator_origen).is_displayed()
        self.driver.find_element(
            *self.txt_locator_origen).clear()
        time.sleep(2)
        self.driver.find_element(
            *self.txt_locator_origen).send_keys(Origen)
        time.sleep(2)
        self.seleccionar_lista_opciones(Origen_buscado)

    @allure.step("Ingresamos un Destino")
    def ingresar_destino(self, Destino, Destino_buscado):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.txt_locator_destino))
        assert self.driver.find_element(
            *self.txt_locator_destino).is_displayed()
        self.driver.find_element(
            *self.txt_locator_destino).clear()
        time.sleep(2)
        self.driver.find_element(
            *self.txt_locator_destino).send_keys(Destino)
        time.sleep(5)
        self.seleccionar_lista_opciones(Destino_buscado)

    @allure.step('Seleccionar de la lista origen o destino')
    def seleccionar_lista_opciones(self, texto_buscado):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.list_locator_origen_destino))
        elementos_destino_origen = self.driver.find_elements(*self.list_locator_origen_destino)
        for elemento in elementos_destino_origen:
            print(elemento.text)
            print(texto_buscado)
            print(texto_buscado in elemento.text)
            print("-"*5)
            if texto_buscado in elemento.text:
                assert texto_buscado in elemento.text, f"[{texto_buscado}] distinto a [{elemento.text}]"
                elemento.click()
                break

    @allure.step("Elegir fecha de Partida")
    def ingresar_fecha_partida(self, texto):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.btn_locator_partida))
        time.sleep(2)
        self.driver.find_element(
            *self.btn_locator_partida).send_keys(texto)

    @allure.step("Elegir fecha de Regreso")
    def ingresar_fecha_regreso(self, texto):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.btn_locator_regreso))
        time.sleep(2)
        self.driver.find_element(
            *self.btn_locator_regreso).send_keys(texto)
        time.sleep(1)
        self.driver.find_element(
            *self.btn_locator_regreso).send_keys(Keys.ESCAPE)

    @allure.step("Seleccionar la cantidad de pasajeros")
    def cantidad_pasajeros(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.slc_locator_clase_pasajeros))
        assert self.driver.find_element(
            *self.slc_locator_clase_pasajeros).is_displayed()
        time.sleep(2)
        self.driver.find_element(*self.slc_locator_clase_pasajeros).click()
        if self.driver.find_element(*self.slc_locator_clase_lista).is_displayed():
            assert WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.btn_locator_agregar_pasajeros))
            assert self.driver.find_element(
                *self.btn_locator_agregar_pasajeros).is_displayed()
            time.sleep(2)
            self.driver.find_element(
                *self.btn_locator_agregar_pasajeros).click()
            time.sleep(2)
        else:
            print("La lista pasajeros no esta desplegada")

    @allure.step("Hacer click en el botón Buscar vuelos")
    def buscar_vuelos(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.btn_locator_buscarvuelos))
        assert self.driver.find_element(
            *self.btn_locator_buscarvuelos).is_displayed()
        self.driver.find_element(
            *self.btn_locator_buscarvuelos).click()

    @allure.step("Hacer click en el botón para dirigirnos a la página Iniciar Sesión")
    def click_iniciar_sesion(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.btn_locator_iniciar_sesion))
        if self.driver.find_element(*self.btn_locator_iniciar_sesion).is_displayed():
            self.driver.find_element(*self.btn_locator_iniciar_sesion).click()
            print("Hacemos click en Iniciar Sesión")
        else:
            print("No se pudo hacer click en Iniciar Sesión")

    @allure.step("Validamos que el texto \"{texto}\" se encuentre en la URL")
    def validar_contenido_URL(self, texto):
        """
        Método para validar que el texto dado está presente en la URL actual.
        """
        assert texto in self.driver.current_url, f"El valor {
            texto} no se encuentra en la URL"
