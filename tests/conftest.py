import pytest
from selenium import webdriver
from config.configuracoes import *
from datetime import datetime
from utils.relatorio_pdf import gerar_relatorio_consolidado
from utils.email_sender import enviar_relatorio_email
from selenium.webdriver.chrome.options import Options
import os


@pytest.fixture
def navegador():

    options = Options()

    if os.getenv("CI") == "true":
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
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

        nome_arquivo = item.path.stem

        pastas_testes = {
            "test_adicionar_produtos_carrinho": "adicionar_produtos_carrinho",
            "test_catalogo_pdp": "catalogo_pdp",
            "test_fluxo_compra": "fluxo_compra"
        }

        arquivos_testes = {
            "test_adicionar_produtos_carrinho": {
                "cenario": "CT-Adicionar-Produtos-Carrinho-002.md",
                "log": "teste_adicionar_produtos_carrinho.log"
            },
            "test_catalogo_pdp": {
                "cenario": "CT-Catalogo-PDP-001.md",
                "log": "teste_catalogo_pdp.log"
            },
            "test_fluxo_compra": {
                "cenario": "CT-Fluxo-Compra-003.md",
                "log": "teste.log"
            }
        }

        pasta_teste = pastas_testes.get(nome_arquivo, nome_arquivo)

        arquivos = arquivos_testes.get(nome_arquivo, {})

        id_execucao = item.config.id_execucao

        item._resultado_teste = {
            "teste": item.name,
            "status": "PASSED",
            "duracao": 0.0,
            "pasta_evidencias": os.path.join(
                "evidências", id_execucao, pasta_teste
            ),
            "pasta_logs": os.path.join(
                "logs", id_execucao, pasta_teste
            ),
            "caminho_cenario": os.path.join(
                "cenarios",
                arquivos.get("cenario", "")
            ),
            "nome_log": arquivos.get("log")
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

    aprovados = sum(r["status"] == "PASSED" for r in resultados)
    reprovados = sum(r["status"] == "FAILED" for r in resultados)
    erros = sum(r["status"] == "ERROR" for r in resultados)
    ignorados = sum(r["status"] == "SKIPPED" for r in resultados)

    percentual_aprovados = aprovados / total * 100 if total else 0
    percentual_reprovados = reprovados / total * 100 if total else 0

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

    # GERAÇÃO AUTOMÁTICA DO RELATÓRIO CONSOLIDADO
    if total > 0:
        try:
            caminho_pdf = gerar_relatorio_consolidado(
                id_execucao=session.config.id_execucao,
                resumo=resumo,
                ambiente="Homologação"
            )

            print(f"\nRelatório consolidado gerado: {caminho_pdf}")

        except Exception as erro:
            print(f"\nErro ao gerar relatório consolidado: {erro}")

        else:
            # ENVIO DO RELATÓRIO CONSOLIDADO POR E-MAIL
            try:
                enviar_relatorio_email(
                    caminho_pdf=caminho_pdf,
                    destinatario=EMAIL_DESTINATARIO,
                    assunto=f"Relatório de Testes - {session.config.id_execucao}",
                    corpo=(
                        "Olá,\n\n"
                        "Segue em anexo o relatório consolidado "
                        "da execução dos testes automatizados.\n\n"
                        f"Total de testes: {total}\n"
                        f"Aprovados: {aprovados}\n"
                        f"Reprovados: {reprovados}\n"
                        f"Erros: {erros}\n"
                        f"Ignorados: {ignorados}\n\n"
                        "Relatório gerado automaticamente pelo Pytest."
                    )
                )

                print("\nRelatório consolidado enviado por e-mail.")

            except Exception as erro:
                print(f"\nErro ao enviar relatório por e-mail: {erro}")










