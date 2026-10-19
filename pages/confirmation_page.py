
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.configuracoes import TIMEOUT


class ConfirmationPage:

    CONTAINER_CONFIRMATION = (
        By.XPATH,
        "//div/main/div/div/div/header"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, TIMEOUT)

    def aguardar_confirmacao(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.CONTAINER_CONFIRMATION
            )
        )

    def destacar_confirmacao(self):
        elemento = self.aguardar_confirmacao()

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                block: 'center'
            });

            arguments[0].style.border = '3px solid green';
            arguments[0].style.boxSizing = 'border-box';
            """,
            elemento
        )

    def obter_mensagem_confirmacao(self):
        elemento = self.aguardar_confirmacao()
        return elemento.text.strip()
