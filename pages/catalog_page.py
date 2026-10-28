from selenium.webdriver.common.by import By


class CatalogPage:

    CARD_BLACK_HEELS_COMPLET = (By.ID, "product-1")
    CARD_BRONZE_SANDALS_COMPLET = (By.ID, "product-2")
    CARD_BROWN_SHADES_COMPLET = (By.ID, "product-3")

    CARD_GREY_JACKET_COMPLET = (By.ID, "product-4")
    CARD_NOIR_JACKET_COMPLET = (By.ID, "product-5")
    CARD_STRIPED_TOP_COMPLET = (By.ID, "product-6")

    CARD_WHITE_SANDALS_COMPLET = (By.ID, "product-7")

    def __init__(self, driver):
        self.driver = driver

    def rolar_ate_produto(self, locator):
        elemento = self.driver.find_element(*locator)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            elemento
        )

    def rolar_para_step_2(self):
        self.rolar_ate_produto(
            self.CARD_GREY_JACKET_COMPLET
        )

    def rolar_para_step_3(self):
        self.rolar_ate_produto(
            self.CARD_WHITE_SANDALS_COMPLET
        )

    def acessar_produto(self, locator):
        elemento = self.driver.find_element(*locator)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            elemento
        )

        elemento.click()