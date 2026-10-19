
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from config.configuracoes import TIMEOUT


class CheckOutPaymentPage:

    # ====================================================
    # LOCATORS - STEP 1
    # ====================================================

    INPUT_EMAIL = (By.ID, "email")
    CHECK_BOX = (By.XPATH, "//div[2]/div[1]/div/label")
    COUNTRY = (By.ID, "SelectPS33_32_2t_19_34_2p_2v_2t-22")
    INPUT_FIRST_NAME = (By.XPATH, "//div[2]/div[1]/div/input")
    INPUT_LAST_NAME = (By.XPATH, "//div[2]/div[2]/div/input")
    INPUT_COMPANY = (By.XPATH, "//div[3]/div/div/input")
    INPUT_POSTAL_CODE = (By.XPATH, "//div[4]/div/div/div/div/input")
    INPUT_STREET = (By.XPATH, "//div[5]/div[1]/div/div/input")
    INPUT_NUMBER = (By.XPATH, "//div[5]/div[2]/div/input")
    INPUT_COMPLEMENT = (By.XPATH, "//div[6]/div[1]/div/input")
    INPUT_NEIGHBORHOOD = (By.XPATH, "//div[6]/div[2]/div/input")

    # ====================================================
    # LOCATORS - STEP 2
    # ====================================================

    INPUT_CITY = (By.XPATH, "//div[1]/div[7]/div[1]")
    INPUT_ESTATE = (By.XPATH, "//div[1]/div[7]/div[2]")
    INPUT_PHONE = (By.XPATH, "//div[8]/div/div/input")

    SAVE_INFORMATION_CHECKBOX = (
        By.XPATH,
        "//div[9]/div/div/input"
    )

    # ====================================================
    # LOCATORS - STEP 3
    # ====================================================

    WORD_CREDT_CARD = (By.XPATH, "//div[1]/h3/strong")
    INPUT_CARD_NUMBER = (By.ID, "number")
    INPUT_EXPIRATION_DATE = (By.ID, "expiry")
    INPUT_SECURITY_CODE = (By.ID, "verification_value")
    INPUT_NAME_ON_CARD = (By.ID, "name")

    BILLING_ADDRESS_CHECKBOX = (
        By.ID,
        "billingAddressCheckbox"
    )

    INPUT_CPF = (By.XPATH, "//section/div/div/div[1]/input")

    BUTTON_PAY_NOW = (By.ID, "checkout-pay-button")

    # ====================================================
    # INICIALIZAÇÃO
    # ====================================================

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, TIMEOUT)

    # ====================================================
    # ESPERA
    # ====================================================

    def aguardar_elemento(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def aguardar_elemento_clicavel(self, locator):
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )

    # ====================================================
    # SCROLL
    # ====================================================

    def rolar_ate_elemento(self, locator):
        elemento = self.aguardar_elemento(locator)

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                block: 'center'
            });
            """,
            elemento
        )

    def rolar_para_step_1(self):
        self.rolar_ate_elemento(self.INPUT_EMAIL)

    def rolar_para_step_2(self):
        self.rolar_ate_elemento(self.INPUT_PHONE)

    def rolar_para_step_3(self):
        self.rolar_ate_elemento(self.INPUT_CARD_NUMBER)

    # ====================================================
    # DESTAQUE
    # ====================================================

    def destacar_elemento(self, locator):
        elemento = self.aguardar_elemento(locator)

        self.driver.execute_script(
            """
            arguments[0].style.border = '3px solid green';
            arguments[0].style.boxSizing = 'border-box';
            """,
            elemento
        )

    # ====================================================
    # CLIQUE
    # ====================================================

    def clicar_elemento(self, locator):
        elemento = self.aguardar_elemento_clicavel(locator)
        elemento.click()

    def mover_cursor_para_elemento(self, locator):
        elemento = self.aguardar_elemento(locator)

        ActionChains(self.driver).move_to_element(
            elemento
        ).perform()

    # ====================================================
    # PREENCHIMENTO
    # ====================================================

    def preencher_campo(self, locator, valor):
        elemento = self.aguardar_elemento_clicavel(locator)
        elemento.clear()
        elemento.send_keys(str(valor))

    
    # ====================================================
    # STEP 1 - CONTATO E ENDEREÇO
    # ====================================================

    def preencher_email(self, email):
        self.preencher_campo(self.INPUT_EMAIL, email)

    def preencher_primeiro_nome(self, nome):
        self.preencher_campo(self.INPUT_FIRST_NAME, nome)

    def preencher_sobrenome(self, sobrenome):
        self.preencher_campo(self.INPUT_LAST_NAME, sobrenome)

    def preencher_empresa(self, empresa):
        self.preencher_campo(self.INPUT_COMPANY, empresa)

    def preencher_cep(self, cep):
        self.preencher_campo(self.INPUT_POSTAL_CODE, cep)

    def preencher_rua(self, rua):
        self.preencher_campo(self.INPUT_STREET, rua)

    def preencher_numero(self, numero):
        self.preencher_campo(self.INPUT_NUMBER, numero)

    def preencher_complemento(self, complemento):
        self.preencher_campo(self.INPUT_COMPLEMENT, complemento)

    def preencher_bairro(self, bairro):
        self.preencher_campo(self.INPUT_NEIGHBORHOOD, bairro)


    # ====================================================
    # STEP 2 - LOCALIZAÇÃO E TELEFONE
    # ====================================================

    def preencher_telefone(self, telefone):
        self.preencher_campo(self.INPUT_PHONE, telefone)


    # ====================================================
    # STEP 3 - PAGAMENTO COM CARTÃO
    # ====================================================

    def preencher_numero_cartao(self, numero):
        self.preencher_campo(self.INPUT_CARD_NUMBER, numero)

    def preencher_validade_cartao(self, validade):
        self.preencher_campo(self.INPUT_EXPIRATION_DATE, validade)

    def preencher_codigo_seguranca(self, codigo):
        self.preencher_campo(self.INPUT_SECURITY_CODE, codigo )

    def preencher_nome_cartao(self, nome):
        self.preencher_campo(self.INPUT_NAME_ON_CARD, nome)

    def preencher_cpf(self, cpf):
        self.preencher_campo(self.INPUT_CPF, cpf)


    # ====================================================
    # FINALIZAR PAGAMENTO
    # ====================================================
    def finalizar_pagamento(self):
        self.rolar_ate_elemento(self.BUTTON_PAY_NOW)
        self.clicar_elemento(self.BUTTON_PAY_NOW)
