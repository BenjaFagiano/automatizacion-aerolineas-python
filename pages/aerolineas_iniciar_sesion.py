from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import time


class AerolineasIniciarSesion():
    txt_locator_usuario = (By.ID, "userNameInput")
    txt_locator_contraseña = (By.ID, "passwordInput")
    btn_locator_ingresar = (By.XPATH, "//button[contains(text(),'INGRESAR')]")
    btn_locator_registrate = (
        By.XPATH, "//button[contains(text(),'registrate') and @class='button__StyledButton-sc-17uyx03-1 MlVrU button-']")
    label_locator_error = (
        By.XPATH, "//div[@class='styled__ErrorMessage-sc-1msw87d-8 vYNnF' and text()='Alguno de los datos ingresados es incorrecto. Intentalo nuevamente.']")
    btn_olvide_minumero = (
        By.XPATH, "//a[contains(text(),'Olvidé mi número Aerolíneas Plus')]")
    btn_olvide_contraseña = (
        By.XPATH, "//a[contains(text(),'Olvidé mi contraseña')]")

    def __init__(self, driver):
        self.driver = driver

    # Agregar assert en cada acción

    @allure.step("Ingresar un nombre de usuario")
    def ingresar_usuario(self, usuario):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.txt_locator_usuario))
        assert self.driver.find_element(
            *self.txt_locator_usuario).is_displayed()
        self.driver.find_element(
            *self.txt_locator_usuario).send_keys(usuario)

    @allure.step("Ingresar una contraseña")
    def ingresar_contraseña(self, contraseña):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.txt_locator_contraseña))
        assert self.driver.find_element(
            *self.txt_locator_contraseña).is_displayed()
        self.driver.find_element(
            *self.txt_locator_contraseña).send_keys(contraseña)

    @allure.step("Hacer click en el botón Ingresar")
    def click_ingresar(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.btn_locator_ingresar))
        if self.driver.find_element(*self.btn_locator_ingresar).is_displayed():
            self.driver.find_element(*self.btn_locator_ingresar).click()
            print("Hacemos click en Ingresar")
        else:
            print("No se pudo hacer click en Ingresar")

    @allure.step("No se pudo iniciar sesión")
    def validar_error_inicio(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.label_locator_error))
        assert self.driver.element_text(
            *self.label_locator_error).is_displayed()
        print("No aparece el mensaje de error")

    @allure.step("Hacemos click en el botón registrate")
    def click_en_registrate(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_any_elements_located(self.btn_locator_registrate))
        assert self.driver.find_element(
            *self.btn_locator_registrate).is_enabled()
        print("Hacemos click en el botón registrate")
        self.driver.implicitly_wait(2)
        self.driver.find_element(
            *self.btn_locator_registrate).click()

    @allure.step("Hacemos click en el botón Olvidé mi número Aerolineas Plus")
    def click_olvide_minumero(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.btn_olvide_minumero))
        assert self.driver.find_element(
            *self.btn_olvide_minumero).is_displayed()
        self.driver.find_element(*self.btn_olvide_minumero).click()

    @allure.step("Hacemos click en el botón Olvide mi Contraseña")
    def click_olvide_contraseña(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.btn_olvide_contraseña))
        assert self.driver.find_element(
            *self.btn_olvide_contraseña).is_displayed()
        assert self.driver.find_element(*self.btn_olvide_contraseña).click()
