
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
    COUNTRY = (By.NAME, "countryCode")
    INPUT_FIRST_NAME = (By.XPATH, "//div[2]/div[1]/div/input")
    INPUT_LAST_NAME = (By.XPATH, "//div[2]/div[2]/div/input")
    INPUT_COMPANY = (By.XPATH, "//div[3]/div/div/input")
    INPUT_POSTAL_CODE = (By.ID, "postalCode")
    INPUT_STREET = (By.XPATH, "//div[5]/div[1]/div/div/input")
    INPUT_NUMBER = (By.XPATH, "//div[5]/div[2]/div/input")
    INPUT_COMPLEMENT = (By.XPATH, "//div[6]/div[1]/div/input")
    INPUT_NEIGHBORHOOD = (By.XPATH, "//div[6]/div[2]/div/input")
    STATE = (By.NAME, "zone")

    # ====================================================
    # LOCATORS - STEP 2
    # ====================================================

    INPUT_CITY = (
        By.CSS_SELECTOR,
        '#shippingAddressForm input[name="city"]:not([data-autofill-honeypot])'
    )
    INPUT_ESTATE = (By.XPATH, "//div[1]/div[7]/div[2]")
    INPUT_PHONE = (By.XPATH, "//div[8]/div/div/input")

    SAVE_INFORMATION_CHECKBOX = (
        By.XPATH,
        "//div[9]/div/div/input"
    )

    # ====================================================
    # LOCATORS - STEP 3
    # ====================================================

    IFRAME_CARD_NUMBER = (By.CSS_SELECTOR, 'iframe[title="Card number"]')
    WORD_CREDT_CARD = (By.XPATH, "//div[1]/h3/strong")
    INPUT_CARD_NUMBER = (By.XPATH, "//input[@placeholder='Card number']")
    IFRAME_EXPIRATION_DATE = (By.CSS_SELECTOR, 'iframe[title="Expiration date (MM / YY)"]')
    INPUT_EXPIRATION_DATE = (By.XPATH, "//input[@placeholder='Expiration date (MM / YY)']")
    IFRAME_SECURITY_CODE = (By.CSS_SELECTOR, 'iframe[title="Security code"]')
    INPUT_SECURITY_CODE = (By.XPATH, "//input[@placeholder='Security code']")
    IFRAME_NAME_ON_CARD = (By.CSS_SELECTOR, 'iframe[title="Name on card"]')
    INPUT_NAME_ON_CARD = (By.ID, "name")

    BILLING_ADDRESS_CHECKBOX = (
        By.ID,
        "billingAddressCheckbox"
    )

    INPUT_CPF = (
        By.CSS_SELECTOR,
        'section[aria-label="Additional information"] input[name="CPF/CNPJ"]'
    )

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
        self.rolar_ate_elemento(self.IFRAME_CARD_NUMBER)

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

    def selecionar_pais(self, pais):
        elemento = self.aguardar_elemento_clicavel(self.COUNTRY)

        seletor = Select(elemento)
        seletor.select_by_value(pais)

        assert seletor.first_selected_option.get_attribute("value") == pais, (
            f"País selecionado diferente do esperado: {pais}"
        )

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

    def preencher_cidade(self, cidade):
        self.preencher_campo(self.INPUT_CITY, cidade)

    # ====================================================
    # STEP 2 - LOCALIZAÇÃO E TELEFONE
    # ====================================================

    def selecionar_estado(self, estado):
        elemento = self.aguardar_elemento_clicavel(self.STATE)

        seletor = Select(elemento)
        seletor.select_by_value(estado)

        assert seletor.first_selected_option.get_attribute("value") == estado, (
            f"Estado selecionado diferente do esperado: {estado}"
        )

    def preencher_telefone(self, telefone):
        self.preencher_campo(self.INPUT_PHONE, telefone)


    # ====================================================
    # STEP 3 - PAGAMENTO COM CARTÃO
    # ====================================================
   
    def preencher_numero_cartao(self, numero):

        iframe = self.aguardar_elemento(self.IFRAME_CARD_NUMBER)

        self.driver.switch_to.frame(iframe)

        try:
            campo = self.aguardar_elemento_clicavel(
                self.INPUT_CARD_NUMBER
            )

            campo.clear()
            campo.send_keys(str(numero))

        finally:
            self.driver.switch_to.default_content()
    
    def preencher_validade_cartao(self, validade):
        iframe = self.aguardar_elemento(
            self.IFRAME_EXPIRATION_DATE
        )

        self.driver.switch_to.frame(iframe)

        try:
            campo = self.aguardar_elemento_clicavel(
                self.INPUT_EXPIRATION_DATE
            )

            campo.clear()

            # Remove o separador e envia somente os dígitos.
            validade_numerica = "".join(
                caractere for caractere in str(validade)
                if caractere.isdigit()
            )

            campo.send_keys(validade_numerica[:2])
            campo.send_keys(validade_numerica[2:])

            valor_preenchido = campo.get_attribute("value")
            print(f"Validade preenchida: {valor_preenchido}")

            assert valor_preenchido.replace(" ", "").replace("/", "") == validade_numerica, (
                f"Validade incompleta: {valor_preenchido}"
            )

        finally:
            self.driver.switch_to.default_content()

    def preencher_codigo_seguranca(self, codigo):

        iframe = self.aguardar_elemento(
            self.IFRAME_SECURITY_CODE
        )

        self.driver.switch_to.frame(iframe)

        try:
            campo = self.aguardar_elemento_clicavel(
                self.INPUT_SECURITY_CODE
            )

            campo.clear()
            campo.send_keys(str(codigo))

        finally:
            self.driver.switch_to.default_content()
    
    def preencher_nome_cartao(self, nome):

        iframe = self.aguardar_elemento(
            self.IFRAME_NAME_ON_CARD
        )

        self.driver.switch_to.frame(iframe)

        try:
            campo = self.aguardar_elemento_clicavel(
                self.INPUT_NAME_ON_CARD
            )

            # Limpa o nome preenchido automaticamente
            campo.clear()

            # Preenche o nome configurado no .env
            campo.send_keys(str(nome))

            # Valida o preenchimento
            nome_preenchido = campo.get_attribute("value")

            assert nome_preenchido == str(nome), (
                "Nome do titular do cartão diferente "
                "do valor configurado."
            )

        finally:
            self.driver.switch_to.default_content()

    def preencher_cpf(self, cpf):
        self.preencher_campo(self.INPUT_CPF, cpf)


    # ====================================================
    # FINALIZAR PAGAMENTO
    # ====================================================
    def finalizar_pagamento(self):
        self.rolar_ate_elemento(self.BUTTON_PAY_NOW)
        self.clicar_elemento(self.BUTTON_PAY_NOW)
