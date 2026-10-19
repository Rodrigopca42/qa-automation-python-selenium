

import os
from dotenv import load_dotenv

load_dotenv()


URL_LOGIN = "https://sauce-demo.myshopify.com/account/login"

URL_HOME = 'https://sauce-demo.myshopify.com/'

AMBIENTE = "Homologação"

TIMEOUT = 4

TEMPO_ESPERA_EVIDENCIA = 2

TEMPO_ATUALIZACAO_MINICART = 6

USUARIO_TESTE = os.getenv('USUARIO_TESTE')
if not USUARIO_TESTE:
    raise ValueError(
        'A variável USUARIO_TESTE não foi configurada no arquivo .env'
    )

SENHA_TESTE = os.getenv('SENHA_TESTE')
if not SENHA_TESTE:
    raise ValueError(
        'A variável SENHA_TESTE não foi configurada no arquivo .env'
    )

EMAIL_DESTINATARIO = os.getenv(
    'EMAIL_DESTINATARIO'
)

if not EMAIL_DESTINATARIO:
    raise ValueError(
        'A variável EMAIL_DESTINATARIO não foi configurada no arquivo .env'
    ) 

# DADOS DE CONTATO
CHECKOUT_EMAIL = os.getenv("CHECKOUT_EMAIL")

# PAGAMENTO SIMULADO
CHECKOUT_CARD_NUMBER = os.getenv("CHECKOUT_CARD_NUMBER")
CHECKOUT_CARD_EXPIRATION = os.getenv("CHECKOUT_CARD_EXPIRATION")
CHECKOUT_CARD_CVV = os.getenv("CHECKOUT_CARD_CVV")
CHECKOUT_CARD_NAME = os.getenv("CHECKOUT_CARD_NAME")
CHECKOUT_CPF = os.getenv("CHECKOUT_CPF")

