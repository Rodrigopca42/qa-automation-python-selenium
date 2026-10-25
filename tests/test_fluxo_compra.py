
import os

from config.configuracoes import *

from data.dados_checkout import DADOS_ENDERECO

from pages.navbar_page import NavBarPage
from pages.header_page import HeaderPage
from pages.catalog_page import CatalogPage
from pages.pdp_page import PdpPage
from pages.check_out1_page import CheckOut1Page
from pages.check_out_payment_page import CheckOutPaymentPage
from pages.confirmation_page import ConfirmationPage

from utils.evidencia import *
from utils.logger import configurar_logger

# ====================================================
# CONFIGURAÇÃO DA EXECUÇÃO
# ====================================================
def preparar_execucao(request):

    id_execucao = request.config.id_execucao

    pasta_evidencia = os.path.join(
        "evidências",
        id_execucao,
        "fluxo_compra"
    )

    pasta_log = os.path.join(
        "logs",
        id_execucao,
        "fluxo_compra"
    )

    os.makedirs(pasta_evidencia, exist_ok=True)
    os.makedirs(pasta_log, exist_ok=True)

    return pasta_evidencia, pasta_log

caminho_bdd = os.path.join(
    "cenarios",
    "CT-Fluxo-Compra-003.md"
)


# ====================================================
# TESTE - FLUXO COMPLETO DE COMPRA
# ====================================================

def test_fluxo_compra(navegador, request):

    pasta_evidencia, pasta_log = preparar_execucao(request)

    logger, caminho_log = configurar_logger(
        pasta_log
    )

    status = "FAIL"

    navbar = NavBarPage(navegador)
    header = HeaderPage(navegador)
    catalogo = CatalogPage(navegador)
    pdp = PdpPage(navegador)
    carrinho = CheckOut1Page(navegador)
    pagamento = CheckOutPaymentPage(navegador)
    confirmacao = ConfirmationPage(navegador)

    try:


        logger.info("========== INÍCIO DO TESTE DE FLUXO DE COMPRA ==========")

        navegador.maximize_window()

        # ====================================================
        # HOME
        # ====================================================

        logger.info("Home acessada - destaque do Catálogo na navbar")

        capturar_evidencia_destacada(
            navegador,
            pasta_evidencia,
            "01_Home acessada - destaque do Catálogo na navbar",
            navbar.CATALOGO
        )

        # ====================================================
        # CATÁLOGO - NAVBAR
        # ====================================================

        logger.info("Clique em catálogo na navbar")

        # O locator de Catálogo deve ser o mesmo
        # utilizado no teste anterior.
        navbar.acessar_catalogo()

        capturar_evidencia(
            navegador,
            pasta_evidencia,
            "02_Clique em catálogo na navbar"
        )

        # ====================================================
        # SELEÇÃO DO PRODUTO - STEP 1
        # ====================================================

        logger.info("Selecionando produto do primeiro step")

        catalogo.rolar_ate_produto(
            catalogo.CARD_BLACK_HEELS_COMPLET
        )

        capturar_evidencia_destacada(
            navegador,
            pasta_evidencia,
            "03_Selecionando produto do primeiro step",
            catalogo.CARD_BLACK_HEELS_COMPLET
        )

        catalogo.acessar_produto(
            catalogo.CARD_BLACK_HEELS_COMPLET
        )

        pdp.adicionar_ao_carrinho()
 
        # ====================================================
        # MINICART NO HEADER
        # ====================================================

        logger.info("Destaque do minicart no header")

        aguardar_atualizacao_minicart()

        capturar_evidencia_destacada(
            navegador,
            pasta_evidencia,
            "04_Destaque do minicart no header",
            header.MINI_CART
        )

        # ====================================================
        # CHECK OUT NO HEADER
        # ====================================================

        logger.info("Clique no CHECK OUT do header")

        capturar_evidencia_destacada(
            navegador,
            pasta_evidencia,
            "05_Clique no CHECK OUT do header",
            header.CHECK_OUT
        )

        header.acessar_checkout()

        # ====================================================
        # CARRINHO - CHECKOUT 1
        # ====================================================

        logger.info(
            "Destaque do Produto selecionado e preço total,clique no CHECK OUT no carrinho"
        )

        assert carrinho.produto_1_visivel(), (
            "Produto não encontrado no carrinho."
        )

        carrinho.destacar_elemento(carrinho.CONTAINER_PRODUT1)
        carrinho.destacar_elemento(carrinho.TOTAL_PRICE)

        capturar_evidencia(
            navegador,
            pasta_evidencia,
            "06_Destaque do Produto selecionado e preço total,clique no CHECK OUT no carrinho"
        )

         # O botão exige posicionamento do cursor.
        carrinho.acessar_checkout()

       
        # ====================================================
        # CHECKOUT PAGAMENTO - STEP 1
        # ====================================================

        logger.info("Preenchimento do formulário - Step 1")

        pagamento.rolar_para_step_1()

        pagamento.preencher_email(CHECKOUT_EMAIL)

        pagamento.preencher_primeiro_nome(
            DADOS_ENDERECO["nome"]
        )

        pagamento.preencher_sobrenome(
            DADOS_ENDERECO["sobrenome"]
        )

        pagamento.preencher_cep(
            DADOS_ENDERECO["cep"]
        )

        pagamento.preencher_rua(
            DADOS_ENDERECO["rua"]
        )

        pagamento.preencher_numero(
            DADOS_ENDERECO["numero"]
        )

        pagamento.preencher_bairro(
            DADOS_ENDERECO["bairro"]
        )

        pagamento.preencher_cidade(
            DADOS_ENDERECO["cidade"]
        )

        capturar_evidencia(
            navegador,
            pasta_evidencia,
            "07_Preenchimento do formulário - Step 1"
        )

        # ====================================================
        # CHECKOUT PAGAMENTO - STEP 2
        # ====================================================

        logger.info("Preenchimento do formulário - Step 2")

        pagamento.rolar_para_step_2()

        # Cidade já preenchida conforme exploração.
        pagamento.preencher_telefone(
            DADOS_ENDERECO["telefone"]
        )

        capturar_evidencia(
            navegador,
            pasta_evidencia,
            "08_Preenchimento do formulário - Step 2"
        )

        # ====================================================
        # CHECKOUT PAGAMENTO - STEP 3
        # ====================================================

        logger.info("Preenchimento do formulário - Step 3")

        pagamento.rolar_para_step_3()

        pagamento.preencher_numero_cartao(CHECKOUT_CARD_NUMBER)

        pagamento.preencher_validade_cartao(CHECKOUT_CARD_EXPIRATION)

        pagamento.preencher_codigo_seguranca(CHECKOUT_CARD_CVV)
        
        pagamento.preencher_nome_cartao(CHECKOUT_CARD_NAME)
        
        # CPF: requer CHECKOUT_CPF em configuracoes.py
        # e preencher_cpf() no Page Object.
        pagamento.preencher_cpf(CHECKOUT_CPF)

        # Não capturar dados completos do cartão ou CVV.
        # Evidência do Step 3 deve ser mascarada.

        capturar_evidencia(
            navegador,
            pasta_evidencia,
            "09_Preenchimento do formulário - Step 3"
        )

        # ====================================================
        # FINALIZAR PAGAMENTO
        # ====================================================

        logger.info("Clique no botão PAY NOW")

        pagamento.finalizar_pagamento()

        # ====================================================
        # CONFIRMAÇÃO DA COMPRA
        # ====================================================

        logger.info("Validação da confirmação de compra")

        mensagem = confirmacao.obter_mensagem_confirmacao()

        assert mensagem, (
            "Mensagem de confirmação da compra não encontrada."
        )

        confirmacao.destacar_confirmacao()

        capturar_evidencia(
            navegador,
            pasta_evidencia,
            "10_Mensagem de confirmação da compra encontrada."
        )

        logger.info("Compra confirmada: %s", mensagem)

        status = "PASS"

        logger.info("Teste de fluxo de compra executado com sucesso")

   
    except Exception as erro:

        logger.error(
            f'Falha na execução do teste | '
            f'Tipo: {type(erro).__name__} | '
            f'Detalhe: {str(erro).splitlines()[0]}'
        )

        if navegador is not None:
            capturar_evidencia(
                navegador,
                pasta_evidencia,
                'erro_fluxo_compra'
            )

        raise

    finally:

        logger.info("Status final: %s", status)
        logger.info("========== FIM DO TESTE ==========")
    
    