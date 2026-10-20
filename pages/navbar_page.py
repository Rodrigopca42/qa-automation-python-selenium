from selenium.webdriver.common.by import By


class NavBarPage:

    # ========================================================
    # LOCATORS
    # ========================================================

    HOME = (By.XPATH, '//*[@id="main-menu"]/li[1]/a')
    CATALOGO = (By.CSS_SELECTOR, '#main-menu a[href="/collections/all"]')
    BLOG = (By.XPATH, '//*[@id="main-menu"]/li[3]/a')
    ABOUT_US = (By.XPATH, '//*[@id="main-menu"]/li[4]/a')

    # ========================================================
    # CONSTRUTOR
    # ========================================================

    def __init__(self, driver):
        self.driver = driver

    # ========================================================
    # AÇÕES
    # ========================================================

    def acessar_home(self):
        link_home = self.driver.find_element(
            *self.HOME
        )

        link_home.click()

    def acessar_catalogo(self):
        link_catalogo = self.driver.find_element(
            *self.CATALOGO
        )

        link_catalogo.click()

    def acessar_blog(self):
        link_blog = self.driver.find_element(
            *self.BLOG
        )

        link_blog.click()

    def acessar_sobre_nos(self):
        link_sobre_nos = self.driver.find_element(
            *self.ABOUT_US
        )

        link_sobre_nos.click()