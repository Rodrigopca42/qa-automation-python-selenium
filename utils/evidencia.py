import os
import time
import re

from config.configuracoes import (
    TEMPO_ESPERA_EVIDENCIA,
    TEMPO_ATUALIZACAO_MINICART
)

def normalizar_nome_evidencia(nome):
    nome = re.sub(r'[<>:"/\\|?*\r\n]', "_", nome)
    return nome.strip().rstrip(". ")

def aguardar_carregamento():
    time.sleep(TEMPO_ESPERA_EVIDENCIA)

def aguardar_atualizacao_minicart():
    time.sleep(TEMPO_ATUALIZACAO_MINICART)


def capturar_evidencia(driver, pasta_execucao, nome):
    os.makedirs(pasta_execucao, exist_ok=True)

    aguardar_carregamento()

    nome_arquivo = normalizar_nome_evidencia(nome)

    caminho = os.path.join(
        pasta_execucao,
        f"{nome_arquivo}.png"
    )

    sucesso = driver.save_screenshot(caminho)

    if sucesso:
        return caminho

    return None


def destacar_elemento(driver, locator):
    elemento = driver.find_element(*locator)

    driver.execute_script(
        """
        arguments[0].style.border = '5px solid green';
        arguments[0].style.boxSizing = 'border-box';
        """,
        elemento
    )


def capturar_evidencia_destacada(
    driver,
    pasta_execucao,
    nome,
    locator
):
    os.makedirs(pasta_execucao, exist_ok=True)

    destacar_elemento(driver, locator)

    aguardar_carregamento()

    nome_arquivo = normalizar_nome_evidencia(nome)

    caminho = os.path.join(
        pasta_execucao,
        f"{nome_arquivo}.png"
    )

    sucesso = driver.save_screenshot(caminho)

    if sucesso:
        return caminho

    return None