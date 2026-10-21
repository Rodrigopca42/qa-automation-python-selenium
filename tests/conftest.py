import pytest
from selenium import webdriver
from config.configuracoes import *
from datetime import datetime
import os


@pytest.fixture
def navegador():
    driver = webdriver.Chrome()
    driver.get(URL_HOME)

    yield driver

    driver.quit()


# ====================================================
# COLETA DOS RESULTADOS DOS TESTES
# ====================================================

def pytest_configure(config):
    config.resultados_testes = []
    config.id_execucao = datetime.now().strftime(
    "%Y-%m-%d_%H-%M-%S"
    )

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    resultado = yield
    relatorio = resultado.get_result()

    resultados = item.config.resultados_testes

    if relatorio.when == "setup":
        item._resultado_teste = {
            "teste": item.nodeid,
            "status": "PASSED",
            "duracao": 0.0
        }

    dados = item._resultado_teste
    dados["duracao"] += relatorio.duration

    if relatorio.failed:
        dados["status"] = (
            "ERROR" if relatorio.when != "call" else "FAILED"
        )

    elif relatorio.skipped and dados["status"] == "PASSED":
        dados["status"] = "SKIPPED"

    if relatorio.when == "teardown":
        dados["duracao"] = round(dados["duracao"], 2)
        resultados.append(dados)


def pytest_sessionfinish(session, exitstatus):
    resultados = session.config.resultados_testes

    total = len(resultados)

    aprovados = sum(
        r["status"] == "PASSED" for r in resultados
    )

    reprovados = sum(
        r["status"] == "FAILED" for r in resultados
    )

    erros = sum(
        r["status"] == "ERROR" for r in resultados
    )

    ignorados = sum(
        r["status"] == "SKIPPED" for r in resultados
    )

    percentual_aprovados = (
        aprovados / total * 100 if total else 0
    )

    percentual_reprovados = (
        reprovados / total * 100 if total else 0
    )

    resumo = {
    "total": total,
    "aprovados": aprovados,
    "reprovados": reprovados,
    "erros": erros,
    "ignorados": ignorados,
    "percentual_aprovados": percentual_aprovados,
    "percentual_reprovados": percentual_reprovados,
    "resultados": resultados
    }

    session.config.resumo_execucao = resumo

    print("\n========== RESULTADO CONSOLIDADO ==========")

    for resultado in resultados:
        duracao = resultado["duracao"]

        minutos = int(duracao // 60)
        segundos = duracao % 60

        tempo_formatado = f"{minutos:02d}:{segundos:05.2f}"

        print(
            f"{resultado['teste']} | "
            f"{resultado['status']} | "
            f"{tempo_formatado}"
    )

    print(f"\nTotal: {total}")
    print(f"Aprovados: {aprovados} ({percentual_aprovados:.1f}%)")
    print(f"Reprovados: {reprovados} ({percentual_reprovados:.1f}%)")
    print(f"Erros: {erros}")
    print(f"Ignorados: {ignorados}")

    print("==========================================")