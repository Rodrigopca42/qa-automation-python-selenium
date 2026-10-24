import os

from utils.evidencia import *
from utils.logger import configurar_logger

from config.configuracoes import *

from pages.navbar_page import NavBarPage
from pages.header_page import HeaderPage
from pages.catalog_page import CatalogPage
from pages.pdp_page import PdpPage
from pages.cart_page import CartPage


# ============================================================
# IDENTIFICAÇÃO DA EXECUÇÃO
# ============================================================

def preparar_execucao(request):

    id_execucao = request.config.id_execucao

    pasta_evidencia = os.path.join(
        "evidências",
        id_execucao,
        "adicionar_produtos_carrinho"
    )

    pasta_execucao = os.path.join(
        "logs",
        id_execucao,
        "adicionar_produtos_carrinho"
    )

    os.makedirs(pasta_evidencia, exist_ok=True)
    os.makedirs(pasta_execucao, exist_ok=True)

    return pasta_evidencia, pasta_execucao


# ============================================================
# CENÁRIO BDD
# ============================================================

caminho_cenario = os.path.join(
    "cenarios",
    "CT-Adicionar-Produtos-Carrinho-002.md"
)


# ============================================================
# TESTE
# ============================================================

def test_adicionar_produtos_ao_carrinho(navegador, request):

    driver = navegador

    pasta_evidencia, pasta_execucao = preparar_execucao(request)

    logger, caminho_log = configurar_logger(
        pasta_execucao,
        "teste_adicionar_produtos_carrinho.log"
    )

    status_teste = "FAIL"

    try:

        logger.info(
            "========== INÍCIO DO TESTE: ADICIONAR PRODUTOS AO CARRINHO =========="
        )

        driver.maximize_window()

        # ====================================================
        # HOME
        # ====================================================

        logger.info("Home acessada")

        capturar_evidencia(
            driver,
            pasta_evidencia,
            "01_Home acessada"
        )

        # ====================================================
        # ACESSAR CATÁLOGO
        # ====================================================

        logger.info(
            "Clique em Catálogo na navbar"
        )

        navbar = NavBarPage(driver)
        header = HeaderPage(driver)

        navbar.acessar_catalogo()

        capturar_evidencia(
            driver,
            pasta_evidencia,
            "02_Clique em Catálogo na navbar"
        )

        # ====================================================
        # PRODUTO 1 - STEP 1
        # ====================================================

        logger.info(
            "Selecionando o primeiro produto no catálogo"
        )

        catalogo = CatalogPage(driver)

        capturar_evidencia_destacada(
            driver,
            pasta_evidencia,
            "03_Selecionando o produto do 1ª step do PLP",
            catalogo.CARD_BLACK_HEELS_COMPLET
        )

        catalogo.acessar_produto(
            catalogo.CARD_BLACK_HEELS_COMPLET
        )

        # ====================================================
        # PDP - PRODUTO 1
        # ====================================================

        logger.info(
            "PDP do primeiro produto acessada"
        )

        pdp = PdpPage(driver)

        capturar_evidencia_destacada(
            driver,
            pasta_evidencia,
            "04_PDP do primeiro produto acessada",
            pdp.ADD_TO_CART
        )

        pdp.adicionar_ao_carrinho()

        # ====================================================
        # MINICART - PRODUTO 1
        # ====================================================

        logger.info(
            "Primeiro produto adicionado ao minicart"
        )

        aguardar_atualizacao_minicart()

        capturar_evidencia_destacada(
            driver,
            pasta_evidencia,
            "05_Primeiro produto adicionado ao minicart",
            header.MINI_CART
        )
        # ====================================================
        # RETORNO AO CATÁLOGO
        # ====================================================

        logger.info(
            "Retorno ao catálogo"
        )

        navbar.acessar_catalogo()

        capturar_evidencia(
            driver,
            pasta_evidencia,
            "06_Retorno ao catálogo - PLP"
        )

        # ====================================================
        # PRODUTO 2 - STEP 2
        # ====================================================

        logger.info(
            "Selecionando outro produto no segundo step"
        )

        catalogo.rolar_para_step_2()

        capturar_evidencia_destacada(
            driver,
            pasta_evidencia,
            "07_Selecionando o produto no 2ª step da PLP",
            catalogo.CARD_GREY_JACKET_COMPLET
        )

        catalogo.acessar_produto(
            catalogo.CARD_GREY_JACKET_COMPLET
        )

        # ====================================================
        # PDP - PRODUTO 2
        # ====================================================

        logger.info(
            "PDP do segundo produto acessada"
        )

        capturar_evidencia_destacada(
            driver,
            pasta_evidencia,
            "08_PDP do segundo produto acessada",
            pdp.ADD_TO_CART
        )

        pdp.adicionar_ao_carrinho()

        # ====================================================
        # MINICART - PRODUTO 2
        # ====================================================

        logger.info(
            "Segundo produto adicionado ao minicart"
        )

        aguardar_atualizacao_minicart()
        
        capturar_evidencia_destacada(
            driver,
            pasta_evidencia,
            "09_Segundo produto adicionado ao minicart",
            header.MINI_CART
        )

        # ====================================================
        # RETORNO AO CATÁLOGO
        # ====================================================

        logger.info(
            "Retorno ao catálogo - PLP"
        )

        navbar.acessar_catalogo()

        capturar_evidencia(
            driver,
            pasta_evidencia,
            "10_Retorno ao catálogo - PLP"
        )

       # ====================================================
       # VERIFICAR PRODUTOS NO MINICART
       # ====================================================

        logger.info(
            "Acessando minicart para verificar os produtos"
        )

        header.acessar_mini_carrinho()

        cart = CartPage(driver)

        cart.destacar_produto_1()
        cart.destacar_produto_2()

        capturar_evidencia(
            driver,
            pasta_evidencia,
            "11_Acessando minicart para verificar os produtos"
        )

        # ====================================================
        # FINALIZAÇÃO
        # ====================================================

        logger.info(
            "Produtos verificados no minicart"
        )

        status_teste = "PASS"

        logger.info(
            "Sucesso"
        )

        logger.info(
            "========== FIM DO TESTE =========="
        )
    except Exception as erro:

        logger.error(
            f"Erro durante a execução do teste: {erro}"
        )

        if driver is not None:

            capturar_evidencia(
                driver,
                pasta_evidencia,
                "erro_adicionar_produtos_carrinho"
            )

        raise

   