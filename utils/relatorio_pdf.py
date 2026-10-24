from pathlib import Path
import os

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import *

from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie


# ============================================================
# CONFIGURAÇÕES VISUAIS
# ============================================================

LARANJA = colors.HexColor("#F36B21")
LARANJA_CLARA = colors.HexColor("#FCE7D8")
CINZA = colors.HexColor("#666666")
CINZA_CLARO = colors.HexColor("#F2F2F2")
CINZA_BORDA = colors.HexColor("#BDBDBD")
PRETO = colors.HexColor("#222222")
VERDE = colors.HexColor("#16803A")
VERMELHO = colors.HexColor("#B42318")

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR.parent / "assets"

LOGO_PATH = ASSETS_DIR / "logo.png"
MARCA_DAGUA_PATH = ASSETS_DIR / "marca_dagua.png"


# ============================================================
# FONTE
# ============================================================

def configurar_fontes():
    """
    Tenta usar Arial do Windows.
    Se não encontrar, o ReportLab usa Helvetica normalmente.
    """
    fontes = {
        "Arial": Path(r"C:\Windows\Fonts\arial.ttf"),
        "Arial-Bold": Path(r"C:\Windows\Fonts\arialbd.ttf"),
    }

    for nome, caminho in fontes.items():
        if caminho.exists():
            try:
                pdfmetrics.registerFont(TTFont(nome, str(caminho)))
            except Exception:
                pass

    if "Arial" in pdfmetrics.getRegisteredFontNames():
        return "Arial", "Arial-Bold" if "Arial-Bold" in pdfmetrics.getRegisteredFontNames() else "Helvetica-Bold"

    return "Helvetica", "Helvetica-Bold"


FONT_NORMAL, FONT_BOLD = configurar_fontes()


# ============================================================
# UTILITÁRIOS
# ============================================================

def ler_arquivo(caminho):
    """
    Lê um arquivo de texto e retorna seu conteúdo.
    """
    caminho = Path(caminho)

    if not caminho.exists():
        return "Arquivo não encontrado."

    try:
        return caminho.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return caminho.read_text(encoding="cp1252")


def escapar_html(texto):
    """
    Escapa caracteres que poderiam ser interpretados
    pelo ReportLab como HTML.
    """
    return (
        str(texto)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def estilo_status(status):
    status = str(status).upper().strip()

    if status == "PASS":
        return VERDE

    if status == "FAIL":
        return VERMELHO

    return CINZA


def criar_estilos():
    estilos = getSampleStyleSheet()

    return {
        "titulo": ParagraphStyle(
            "TituloCustomizado",
            parent=estilos["Title"],
            fontName=FONT_BOLD,
            fontSize=18,
            leading=22,
            textColor=PRETO,
            alignment=TA_LEFT,
            spaceAfter=12,
        ),

        "secao": ParagraphStyle(
            "SecaoCustomizada",
            parent=estilos["Heading2"],
            fontName=FONT_BOLD,
            fontSize=12,
            leading=15,
            textColor=PRETO,
            spaceBefore=10,
            spaceAfter=7,
        ),

        "normal": ParagraphStyle(
            "NormalCustomizado",
            parent=estilos["BodyText"],
            fontName=FONT_NORMAL,
            fontSize=9.5,
            leading=13,
            textColor=PRETO,
            spaceAfter=4,
        ),

        "normal_bold": ParagraphStyle(
            "NormalBoldCustomizado",
            parent=estilos["BodyText"],
            fontName=FONT_BOLD,
            fontSize=9.5,
            leading=13,
            textColor=PRETO,
        ),

        "bdd": ParagraphStyle(
            "BDD",
            parent=estilos["BodyText"],
            fontName=FONT_NORMAL,
            fontSize=11,
            leading=13,
            textColor=PRETO,
            leftIndent=8,
            rightIndent=8,
            spaceAfter=2,
        ),

        "log": ParagraphStyle(
            "Log",
            parent=estilos["Code"],
            fontName="Courier",
            fontSize=11,
            leading=10,
            textColor=PRETO,
            leftIndent=5,
            rightIndent=5,
            spaceAfter=1,
        ),

        "evidencia": ParagraphStyle(
            "Evidencia",
            parent=estilos["BodyText"],
            fontName=FONT_BOLD,
            fontSize=11,
            leading=12,
            textColor=PRETO,
            spaceAfter=5,
        ),

        "rodape": ParagraphStyle(
            "Rodape",
            parent=estilos["BodyText"],
            fontName=FONT_NORMAL,
            fontSize=8,
            textColor=CINZA,
        ),
    }


# ============================================================
# CABEÇALHO / RODAPÉ / MARCA D'ÁGUA
# ============================================================

def desenhar_fundo(canvas, doc):
    """
    Desenha a identidade visual do modelo em todas as páginas.
    """
    largura, altura = A4
    canvas.saveState()

    # -------------------------
    # Cabeçalho
    # -------------------------

    canvas.setFont(FONT_BOLD, 9.5)
    canvas.setFillColor(PRETO)

    canvas.drawString(
        1.5 * cm,
        altura - 1.25 * cm,
        "Projeto: Automação Python/Pytest/Selenium",
    )

    # Logo
    if LOGO_PATH.exists():
        canvas.drawImage(
            str(LOGO_PATH),
            largura - 5.0 * cm,
            altura - 2.0 * cm,
            width=4.3 * cm,
            height=1.8 * cm,
            preserveAspectRatio=True,
            mask="auto",
        )

    # Linha do cabeçalho
    canvas.setStrokeColor(PRETO)
    canvas.setLineWidth(1.2)

    canvas.line(
        1.5 * cm,
        altura - 2.15 * cm,
        largura - 1.5 * cm,
        altura - 2.15 * cm,
    )

    # -------------------------
    # Marca d'água
    # -------------------------

    if MARCA_DAGUA_PATH.exists():
        # A imagem já foi preparada com fundo transparente.
        canvas.drawImage(
            str(MARCA_DAGUA_PATH),
            5.0 * cm,
            8.0 * cm,
            width=11.0 * cm,
            height=11.0 * cm,
            preserveAspectRatio=True,
            mask="auto",
        )

    # -------------------------
    # Rodapé
    # -------------------------

    canvas.setFont(FONT_NORMAL, 7.5)
    canvas.setFillColor(CINZA)

    canvas.drawString(
        1.5 * cm,
        0.9 * cm,
        f"{doc.page}",
    )

    canvas.restoreState()


# ============================================================
# EVIDÊNCIA
# ============================================================

def criar_imagem_evidencia(caminho_imagem, largura_max, altura_max):
    """
    Cria a imagem mantendo a proporção original.
    Não depende do Pillow; usa o próprio ReportLab.
    """
    from reportlab.lib.utils import ImageReader

    try:
        imagem = ImageReader(str(caminho_imagem))
        largura_original, altura_original = imagem.getSize()
    except Exception:
        largura_original, altura_original = 16, 9

    proporcao = largura_original / altura_original

    largura = largura_max
    altura = largura / proporcao

    if altura > altura_max:
        altura = altura_max
        largura = altura * proporcao

    return Image(
        str(caminho_imagem),
        width=largura,
        height=altura,
        hAlign="CENTER",
    )


# ============================================================
# RELATÓRIO
# ============================================================

def gerar_relatorio_pdf(
    id_execucao,
    caminho_cenario,
    pasta_evidencias,
    caminho_log,
    pasta_relatorio,
    status,
    ambiente="Homologação",
):
    """
    Gera o relatório PDF da execução mantendo a identidade visual
    do modelo fornecido.

    O conteúdo continua sendo dinâmico:
    - informações da execução
    - cenário BDD
    - evidências
    - log
    - resultado

    A quantidade de evidências e páginas não é fixa.
    """

    pasta_relatorio = Path(pasta_relatorio)
    pasta_evidencias = Path(pasta_evidencias)
    caminho_cenario = Path(caminho_cenario)
    caminho_log = Path(caminho_log)

    pasta_relatorio.mkdir(parents=True, exist_ok=True)

    caminho_pdf = pasta_relatorio / f"relatorio_{id_execucao}.pdf"

    # Área útil entre o cabeçalho e o rodapé.
    documento = SimpleDocTemplate(
        str(caminho_pdf),
        pagesize=A4,
        rightMargin=1.5 * cm,
        leftMargin=1.5 * cm,
        topMargin=2.65 * cm,
        bottomMargin=1.55 * cm,
        title="Relatório de Execução de Testes",
        author="Automação Python/Pytest/Selenium",
    )

    estilos = criar_estilos()
    elementos = []

    # ========================================================
    # TÍTULO
    # ========================================================

    elementos.append(
        Paragraph(
            "RELATÓRIO DE EXECUÇÃO DE TESTES",
            estilos["titulo"],
        )
    )

    # Linha laranja abaixo do título
    elementos.append(
        Table(
            [[""]],
            colWidths=[17.0 * cm],
            rowHeights=[0.10 * cm],
            style=TableStyle([
                ("BACKGROUND", (0, 0), (-1, -1), LARANJA),
                ("LINEBELOW", (0, 0), (-1, -1), 0, LARANJA),
            ]),
        )
    )

    elementos.append(Spacer(1, 8))

    # ========================================================
    # INFORMAÇÕES DA EXECUÇÃO
    # ========================================================

    elementos.append(
        Paragraph(
            "Informações da execução",
            estilos["secao"],
        )
    )

    cor_status = estilo_status(status)

    dados_execucao = [
        [
            Paragraph("<b>ID da execução</b>", estilos["normal"]),
            Paragraph(escapar_html(id_execucao), estilos["normal"]),
        ],
        [
            Paragraph("<b>Ambiente</b>", estilos["normal"]),
            Paragraph(escapar_html(ambiente), estilos["normal"]),
        ],
        [
            Paragraph("<b>Status</b>", estilos["normal"]),
            Paragraph(
                f'<font color="{cor_status.hexval()}"><b>{escapar_html(status)}</b></font>',
                estilos["normal"],
            ),
        ],
    ]

    tabela_execucao = Table(
        dados_execucao,
        colWidths=[5.0 * cm, 12.0 * cm],
        repeatRows=0,
    )

    tabela_execucao.setStyle(
        TableStyle([
            ("GRID", (0, 0), (-1, -1), 0.5, CINZA_BORDA),
            ("BACKGROUND", (0, 0), (0, -1), CINZA_CLARO),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("LEFTPADDING", (0, 0), (-1, -1), 7),
            ("RIGHTPADDING", (0, 0), (-1, -1), 7),
            ("TOPPADDING", (0, 0), (-1, -1), 5),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ])
    )

    elementos.append(tabela_execucao)

    # ========================================================
    # CENÁRIO BDD
    # ========================================================

    elementos.append(
        Paragraph(
            "Cenário de teste BDD",
            estilos["secao"],
        )
    )

    cenario = ler_arquivo(caminho_cenario)

    # Cada linha vira um Paragraph separado.
    # Isso permite que o ReportLab quebre páginas corretamente.
    linhas_cenario = cenario.splitlines()

    if linhas_cenario:
        for linha in linhas_cenario:
            linha = linha.strip()

            if not linha:
                elementos.append(Spacer(1, 4))
                continue

            elementos.append(
                Paragraph(
                    escapar_html(linha),
                    estilos["bdd"],
                )
            )
    else:
        elementos.append(
            Paragraph(
                "Cenário BDD não encontrado.",
                estilos["normal"],
            )
        )

    # ========================================================
    # EVIDÊNCIAS
    # ========================================================

    elementos.append(PageBreak())

    elementos.append(
        Paragraph(
            "Evidências da execução",
            estilos["secao"],
        )
    )

    imagens = []

    if pasta_evidencias.exists():
        imagens = sorted(
            arquivo
            for arquivo in pasta_evidencias.iterdir()
            if arquivo.is_file()
            and arquivo.suffix.lower() in (".png", ".jpg", ".jpeg")
        )

    if imagens:

        for indice, caminho_imagem in enumerate(imagens, start=1):

            nome = caminho_imagem.name

            bloco = [
                Paragraph(
                    f"EVIDÊNCIA {indice:02d} — {escapar_html(nome)}",
                    estilos["evidencia"],
                )
            ]

            try:
                bloco.append(
                    criar_imagem_evidencia(
                        caminho_imagem,
                        largura_max=16.5 * cm,
                        altura_max=8.7 * cm,
                    )
                )
            except Exception:
                bloco.append(
                    Paragraph(
                        "Não foi possível carregar esta evidência.",
                        estilos["normal"],
                    )
                )

            bloco.append(Spacer(1, 10))

            # O KeepTogether tenta manter título + screenshot juntos.
            elementos.append(KeepTogether(bloco))

    else:
        elementos.append(
            Paragraph(
                "Nenhuma evidência encontrada.",
                estilos["normal"],
            )
        )

    # ========================================================
    # LOG
    # ========================================================

    elementos.append(PageBreak())

    elementos.append(
        Paragraph(
            "Log da execução",
            estilos["secao"],
        )
    )

    log = ler_arquivo(caminho_log)

    linhas_log = log.splitlines()

    if linhas_log:

        # Cada linha separada permite quebra automática de página.
        for linha in linhas_log:

            linha_escapada = escapar_html(linha)

            elementos.append(
                Paragraph(
                    linha_escapada if linha_escapada else "&nbsp;",
                    estilos["log"],
                )
            )

    else:
        elementos.append(
            Paragraph(
                "Log não encontrado.",
                estilos["normal"],
            )
        )

    # ========================================================
    # RESULTADO
    # ========================================================

    elementos.append(Spacer(1, 15))

    elementos.append(
        Paragraph(
            "Resultado da execução",
            estilos["secao"],
        )
    )

    resultado = Table(
        [[
            Paragraph(
                f'<font color="{cor_status.hexval()}">'
                f'<b>STATUS: {escapar_html(status)}</b>'
                f'</font>',
                estilos["normal"],
            )
        ]],
        colWidths=[17.0 * cm],
    )

    resultado.setStyle(
        TableStyle([
            ("BOX", (0, 0), (-1, -1), 1, cor_status),
            ("BACKGROUND", (0, 0), (-1, -1), colors.white),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING", (0, 0), (-1, -1), 10),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ])
    )

    elementos.append(resultado)

    # ========================================================
    # GERAÇÃO DO PDF
    # ========================================================

    documento.build(
        elementos,
        onFirstPage=desenhar_fundo,
        onLaterPages=desenhar_fundo,
    )

    return str(caminho_pdf)

# ============================================================
# RELATÓRIO CONSOLIDADO DA SUÍTE
# ============================================================

def gerar_relatorio_consolidado(
    id_execucao,
    resumo,
    ambiente="Homologação"
):
    """
    Gera um único relatório PDF para a suíte de testes.

    O relatório utilizará:
    - Resultados consolidados do Pytest
    - Duração individual dos testes
    - Cenários BDD
    - Evidências
    - Logs
    - Gráfico de resultados
    """

    pasta_relatorio = Path("reports") / id_execucao

    pasta_relatorio.mkdir(
        parents=True,
        exist_ok=True
    )

    caminho_pdf = (
        pasta_relatorio /
        f"relatorio_consolidado_{id_execucao}.pdf"
    )

    # Configurações visuais existentes
    configurar_fontes()
    estilos = criar_estilos()

    # Configuração do documento
    documento = SimpleDocTemplate(
        str(caminho_pdf),
        pagesize=A4,
        rightMargin=2 * cm,
        leftMargin=2 * cm,
        topMargin=3 * cm,
        bottomMargin=2 * cm
    )

    elementos = []

    # Título
    elementos.append(
        Paragraph(
            "RELATÓRIO CONSOLIDADO DE TESTES",
            estilos["titulo"]
        )
    )

    elementos.append(Spacer(1, 0.5 * cm))

    # Identificação da execução
    elementos.append(
        Paragraph(
            f"<b>Execução:</b> {id_execucao}",
            estilos["normal"]
        )
    )

    elementos.append(
        Paragraph(
            f"<b>Ambiente:</b> {ambiente}",
            estilos["normal"]
        )
    )

    elementos.append(Spacer(1, 0.5 * cm))

    # Resumo consolidado da execução
    elementos.append(
        Paragraph(
            "RESUMO DA EXECUÇÃO",
            estilos["secao"]
        )
    )

    dados_resumo = [
        ["Indicador", "Resultado"],
        ["Total de testes", str(resumo.get("total", 0))],
        ["Aprovados", str(resumo.get("aprovados", 0))],
        ["Reprovados", str(resumo.get("reprovados", 0))],
        ["Erros", str(resumo.get("erros", 0))],
        ["Ignorados", str(resumo.get("ignorados", 0))],
        [
            "Percentual de aprovação",
            f'{resumo.get("percentual_aprovados", 0):.1f}%'
        ],
        [
            "Percentual de reprovação",
            f'{resumo.get("percentual_reprovados", 0):.1f}%'
        ]
    ]

    tabela_resumo = Table(
        dados_resumo,
        colWidths=[10 * cm, 6 * cm]
    )

    tabela_resumo.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), LARANJA),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, 0), FONT_BOLD),
            ("BACKGROUND", (0, 1), (-1, -1), CINZA_CLARO),
            ("GRID", (0, 0), (-1, -1), 0.5, CINZA_BORDA),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING", (0, 0), (-1, -1), 8),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 8)
        ])
    )

    elementos.append(tabela_resumo)

    # Gráfico consolidado dos resultados
    elementos.append(Spacer(1, 0.5 * cm))

    elementos.append(
        Paragraph(
            "DISTRIBUIÇÃO DOS RESULTADOS",
            estilos["secao"]
        )
    )

    valores = [
        resumo.get("aprovados", 0),
        resumo.get("reprovados", 0),
        resumo.get("erros", 0),
        resumo.get("ignorados", 0)
    ]

    if sum(valores) > 0:
        grafico = Drawing(400, 200)

        pizza = Pie()
        pizza.x = 120
        pizza.y = 10
        pizza.width = 180
        pizza.height = 180

        pizza.data = valores
        pizza.labels = [
            "Aprovados",
            "Reprovados",
            "Erros",
            "Ignorados"
        ]

        pizza.slices[0].fillColor = VERDE
        pizza.slices[1].fillColor = VERMELHO
        pizza.slices[2].fillColor = LARANJA
        pizza.slices[3].fillColor = CINZA

        grafico.add(pizza)
        elementos.append(grafico)

    # Resultados individuais dos testes
    elementos.append(Spacer(1, 0.5 * cm))

    titulo_resultados = Paragraph(
        "RESULTADOS INDIVIDUAIS",
        estilos["secao"]
    )

    dados_testes = [
        ["Teste", "Status", "Duração"]
    ]

    for resultado in resumo.get("resultados", []):
        nome_teste = resultado.get("teste", "")
        status = resultado.get("status", "")
        duracao = resultado.get("duracao", 0)

        minutos, segundos = divmod(duracao, 60)
        tempo_formatado = f"{int(minutos):02d}:{segundos:05.2f}"

        dados_testes.append([
            Paragraph(
                escapar_html(nome_teste),
                estilos["normal"]
            ),
            status,
            tempo_formatado
        ])

    tabela_testes = Table(
        dados_testes,
        colWidths=[10 * cm, 3 * cm, 3 * cm],
        repeatRows=1
    )

    tabela_testes.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), LARANJA),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, 0), FONT_BOLD),
            ("BACKGROUND", (0, 1), (-1, -1), CINZA_CLARO),
            ("GRID", (0, 0), (-1, -1), 0.5, CINZA_BORDA),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING", (0, 0), (-1, -1), 8),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 8)
        ])
    )

    elementos.append(
        KeepTogether([
            titulo_resultados,
            Spacer(1, 0.2 * cm),
            tabela_testes
        ])
    )

    # Detalhamento dos cenários BDD
    for resultado in resumo.get("resultados", []):

        nome_teste = resultado.get("teste", "")
        caminho_cenario = resultado.get("caminho_cenario", "")

        elementos.append(PageBreak())

        elementos.append(
            Paragraph(
                escapar_html(nome_teste),
                estilos["secao"]
            )
        )

        elementos.append(Spacer(1, 0.3 * cm))

        elementos.append(
            Paragraph(
                "CENÁRIO BDD",
                estilos["normal_bold"]
            )
        )

        elementos.append(Spacer(1, 0.2 * cm))

        if caminho_cenario and os.path.isfile(caminho_cenario):

            conteudo_bdd = ler_arquivo(caminho_cenario)

            for linha in conteudo_bdd.splitlines():

                if not linha.strip():
                    elementos.append(Spacer(1, 0.15 * cm))
                    continue

                elementos.append(
                    Paragraph(
                        escapar_html(linha),
                        estilos["bdd"]
                    )
                )

        else:
            elementos.append(
                Paragraph(
                    "Cenário BDD não encontrado.",
                    estilos["normal"]
                )
            )

        # Evidências do teste
        elementos.append(Spacer(1, 0.5 * cm))

        elementos.append(
            Paragraph(
                "EVIDÊNCIAS",
                estilos["normal_bold"]
            )
        )

        pasta_evidencias = resultado.get("pasta_evidencias", "")

        if pasta_evidencias and os.path.isdir(pasta_evidencias):

            imagens = sorted(
                [
                    arquivo for arquivo in Path(pasta_evidencias).iterdir()
                    if arquivo.is_file()
                    and arquivo.suffix.lower() in (".png", ".jpg", ".jpeg")
                ],
                key=lambda arquivo: arquivo.name
            )

            for imagem in imagens:

                bloco_evidencia = [
                    Paragraph(
                        escapar_html(imagem.name),
                        estilos["evidencia"]
                    ),
                    criar_imagem_evidencia(
                        str(imagem),
                        16 * cm,
                        12 * cm
                    ),
                    Spacer(1, 0.3 * cm)
                ]

                elementos.append(
                    KeepTogether(bloco_evidencia)
                )

        else:
            elementos.append(
                Paragraph(
                    "Pasta de evidências não encontrada.",
                    estilos["normal"]
                )
            )

    # Logs do teste
        elementos.append(Spacer(1, 0.5 * cm))

        elementos.append(
            Paragraph(
                "LOGS DA EXECUÇÃO",
                estilos["normal_bold"]
            )
        )

        pasta_logs = resultado.get("pasta_logs", "")
        nome_log = resultado.get("nome_log", "")

        caminho_log = (
            os.path.join(pasta_logs, nome_log)
            if pasta_logs and nome_log
            else ""
        )

        if caminho_log and os.path.isfile(caminho_log):
            conteudo_log = ler_arquivo(caminho_log)

            for linha in conteudo_log.splitlines():
                if linha.strip():
                    elementos.append(
                        Paragraph(
                            escapar_html(linha),
                            estilos["log"]
                        )
                    )
        else:
            elementos.append(
                Paragraph(
                    "Arquivo de log não encontrado.",
                    estilos["normal"]
                )
            )    

    # Geração do documento
    documento.build(
        elementos,
        onFirstPage=desenhar_fundo,
        onLaterPages=desenhar_fundo
    )

    return str(caminho_pdf)

