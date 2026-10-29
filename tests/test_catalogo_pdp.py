import os

from utils.evidencia import *
from utils.logger import configurar_logger

from config.configuracoes import *

from pages.navbar_page import NavBarPage
from pages.catalog_page import CatalogPage
from pages.pdp_page import PdpPage

# ============================================================
# PREPARAÇÃO DA EXECUÇÃO
# ============================================================

def preparar_execucao(request):

    id_execucao = request.config.id_execucao

    pasta_evidencia = os.path.join(
        "evidências",
        id_execucao,
        "catalogo_pdp"
    )

    pasta_execucao = os.path.join(
        "logs",
        id_execucao,
        "catalogo_pdp"
    )

    os.makedirs(pasta_evidencia, exist_ok=True)
    os.makedirs(pasta_execucao, exist_ok=True)

    return pasta_evidencia, pasta_execucao


# ============================================================
# CENÁRIO BDD
# ============================================================

caminho_cenario = os.path.join(
    "cenarios",
    "CT-CATALOGO-PDP-001.md"
)

# ============================================================
# TESTE
# ============================================================

def test_acessar_catalogo_e_visualizar_produto(navegador, request):

    driver = navegador

    pasta_evidencia, pasta_execucao = preparar_execucao(request)

    logger, caminho_log = configurar_logger(
        pasta_execucao,
        "teste_catalogo_pdp.log"
    )

    try:

        logger.info(
            '=== INÍCIO DO TESTE DE CATÁLOGO E PDP ==='
        )

        driver.maximize_window()

        capturar_evidencia(
            driver,
            pasta_evidencia,
            '01_Home com navbar, clicar na opção catalogo'
        )

        logger.info('Home com navbar, clicar na opção catalogo')

        # ====================================================
        # ACESSAR CATÁLOGO
        # ====================================================

        navbar = NavBarPage(driver)

        navbar.acessar_catalogo()

        capturar_evidencia(
            driver,
            pasta_evidencia,
            '02_Catálogo PLP acessado'
        )

        logger.info('Catálogo acessado')

        # ====================================================
        # SELECIONAR PRODUTO
        # ====================================================

        catalogo = CatalogPage(driver)

        catalogo.rolar_para_step_2()

        capturar_evidencia_destacada(
            driver,
            pasta_evidencia,
            '03_Produto Noir Jacket localizado na PLP',
            catalogo.CARD_NOIR_JACKET_COMPLET
        )

        logger.info(
            'Produto Noir Jacket localizado na PLP'
        )

        # ====================================================
        # ACESSAR PDP
        # ====================================================

        catalogo.acessar_produto(
            catalogo.CARD_NOIR_JACKET_COMPLET
        )

        capturar_evidencia(
            driver,
            pasta_evidencia,
            '04_Produto selecionado - Grey Jacket'
        )

        logger.info(
            'Produto selecionado - Grey Jacket'
        )

        # ====================================================
        # ADD TO CART
        # ====================================================

        pdp = PdpPage(driver)

        pdp.adicionar_ao_carrinho()

        capturar_evidencia(
            driver,
            pasta_evidencia,
            '05_Botão "ADD TO CART" acionado '
        )

        logger.info(
            'ADD TO CART acionado'
        )

        # ====================================================
        # FINALIZAÇÃO
        # ====================================================

        logger.info(
            'Teste executado com sucesso'
        )

        logger.info(
            '========== FIM DO TESTE =========='
        )

    except Exception as erro:

        logger.error(
            f'Falha na execução do teste | '
            f'Tipo: {type(erro).__name__} | '
            f'Detalhe: {str(erro).splitlines()[0]}'
        )

        if driver is not None:
            capturar_evidencia(
                driver,
                pasta_evidencia,
                'erro_catalogo_pdp'
            )

        raise

    