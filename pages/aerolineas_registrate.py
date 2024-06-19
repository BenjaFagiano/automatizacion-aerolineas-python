from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class AerolineasRegistrate:
    """
    Clase que valida los locator de la pantalla registrate
    """
    txt_nombre = (By.NAME, "firstName")
    txt_apellido = (By.NAME, "lastName")
    txt_fecha_nacimiento = (By.NAME, "birthDate")
    slc_tipo_documento = (By.XPATH, "//div[@class='css-10nd86i']")
    txt_ingresar_numero = (By.NAME, "identificationCode")
    txt_ingresar_email = (By.NAME, "mail")
    btn_aceptar = (By.XPATH, "//button[contains(text(),'Aceptar')]")
    btn_cancelar = (By.XPATH, "//button[contains(text(),'Cancelar')]")
    txt_pre_inscripcion = (
        By.XPATH, "//*[@class='styled__Title-k6t5hw-3 cPnsML refund-title'][contains(text(), 'Realizaste tu pre-inscripción al programa Aerolíneas Plus.')]")

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ingresar un Nombre")
    def ingresar_nombre(self, datos_registro):
        """
        Metodo para ingresar un nombre
        """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.txt_nombre))
        assert self.driver.find_element(
            *self.txt_nombre).is_displayed()
        self.driver.find_element(
            *self.txt_nombre).send_keys(datos_registro)

    @allure.step("Ingresar un Apellido")
    def ingresar_apellido(self, datos_registro):
        """
        Metodo para ingresar un apellido
        """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.txt_apellido))
        assert self.driver.find_element(
            *self.txt_apellido).is_displayed()
        self.driver.find_element(
            *self.txt_apellido).send_keys(datos_registro)

    @allure.step("Ingresar Fecha de Nacimiento")
    def ingresar_fecha_nacimiento(self, datos_registro):
        """
        Metodo para ingresar la fecha de nacimiento
        """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.txt_fecha_nacimiento))
        assert self.driver.find_element(
            *self.txt_fecha_nacimiento).is_displayed()
        self.driver.find_element(
            *self.txt_fecha_nacimiento).send_keys(datos_registro)

    @allure.step("Seleccionar Tipo de Documento")
    def seleccionar_documento(self):
        """
        Metodo para seleccionar un tipo de documento
        """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.slc_tipo_documento))
        self.driver.find_element(
            *self.slc_tipo_documento).is_displayed()
        with allure.step("Hace click en el selector y seleccionamos DNI"):
            assert self.driver.find_element(
                *self.slc_tipo_documento).is_enabled()
            self.driver.find_element(*self.slc_tipo_documento).click()
            self.driver.find_element(
                *self.slc_tipo_documento).send_keys(Keys.ARROW_DOWN)
            self.driver.find_element(
                *self.slc_tipo_documento).send_keys(Keys.ENTER)

    @allure.step("Ingresar el Número de Documento")
    def ingresar_numero_documento(self, datos_registro):
        """
        Metodo para ingresar el número de docuemento
        """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.txt_ingresar_numero))
        assert self.driver.find_element(
            *self.txt_ingresar_numero).is_displayed()
        self.driver.find_element(
            *self.txt_ingresar_numero).send_keys(datos_registro)

    @allure.step("Ingresar un Email")
    def ingresar_email(self, datos_registro):
        """
        Metodo para ingresar un Email
        """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.txt_ingresar_email))
        assert self.driver.find_element(
            *self.txt_ingresar_email).is_displayed()
        self.driver.find_element(
            *self.txt_ingresar_email).send_keys(datos_registro)

    @allure.step("Hacemos clic en el botón Aceptar")
    def click_aceptar(self):
        """
        Método para hacer clic en el botón aceptar
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.btn_aceptar)
        )
        assert self.driver.find_element(*self.btn_aceptar).is_displayed()
        self.driver.find_element(*self.btn_aceptar).click()

    @allure.step("Mensaje de validación de correo enviado")
    def mensaje_pre_inscripcion(self):
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(self.txt_pre_inscripcion))
        assert self.driver.find_element(
            *self.txt_pre_inscripcion).is_displayed()
