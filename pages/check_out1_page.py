
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.configuracoes import TIMEOUT


class CheckOut1Page:

    # ====================================================
    # LOCATORS - CHECKOUT 1
    # ====================================================

    CONTAINER_PRODUT1 = (By.XPATH, "//section/form/div[1]/div[2]")
    CONTAINER_PRODUT2 = (By.XPATH, "//section/form/div[1]/div[3]")
    TOTAL_PRICE = (By.XPATH, "//form/div[2]/div[2]/h2")
    QUANTIDADE = (By.XPATH, "//div[2]/div[3]/input")
    DELETE = (By.XPATH, "//div[2]/div[5]/a")
    CONTINUE_SHOPPING = (By.XPATH, "//div[2]/div[1]/a")
    ADD_NOTE = (By.ID, "note")
    UPDATE = (By.XPATH, "//div[3]/div[2]/input[1]")
    CHECK_OUT = (By.XPATH, "//div[3]/div[2]/input[2]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, TIMEOUT)

    # ====================================================
    # LOCALIZAÇÃO E ESPERA
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
    # DESTAQUE
    # ====================================================

    def destacar_elemento(self, locator):
        elemento = self.aguardar_elemento(locator)

        self.driver.execute_script(
            """
            arguments[0].style.border = '5px solid green';
            arguments[0].style.boxSizing = 'border-box';
            """,
            elemento
        )

    # ====================================================
    # INTERAÇÕES
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
    # AÇÕES DO CHECKOUT 1
    # ====================================================

    def acessar_checkout(self):
        self.mover_cursor_para_elemento(self.CHECK_OUT)

        botao_checkout = self.aguardar_elemento_clicavel(
            self.CHECK_OUT
        )

        botao_checkout.click()

    def continuar_comprando(self):
        self.clicar_elemento(self.CONTINUE_SHOPPING)

    def atualizar_carrinho(self):
        self.clicar_elemento(self.UPDATE)

    def preencher_observacao(self, texto):
        campo = self.aguardar_elemento(self.ADD_NOTE)
        campo.clear()
        campo.send_keys(texto)

    # ====================================================
    # CONSULTAS PARA VALIDAÇÃO
    # ====================================================

    def produto_1_visivel(self):
        return self.aguardar_elemento(
            self.CONTAINER_PRODUT1
        ).is_displayed()

    def produto_2_visivel(self):
        return self.aguardar_elemento(
            self.CONTAINER_PRODUT2
        ).is_displayed()
