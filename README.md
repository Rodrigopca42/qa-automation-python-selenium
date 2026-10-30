# 🤖 Automação de Testes Web com Python, Selenium e Pytest

**Projeto de automação funcional web | Python • Selenium WebDriver • Pytest • Page Object Model • GitHub Actions**

**Status:** Versão 1.0 — Concluída

## 📖 Apresentação do projeto

Este projeto apresenta uma solução de automação de testes funcionais para uma aplicação web de e-commerce, desenvolvida com **Python, Selenium WebDriver e Pytest**.

A implementação utiliza o padrão arquitetural **Page Object Model (POM)** para organizar as interações com a aplicação, separar responsabilidades e facilitar a manutenção dos testes automatizados.

Além da execução dos cenários funcionais, a solução contempla captura de evidências, registros de logs, geração de relatórios consolidados em PDF e execução automatizada por meio do **GitHub Actions**.

O projeto foi desenvolvido de forma independente, com o objetivo de aplicar e demonstrar competências práticas em automação de testes e engenharia de qualidade de software.

A aplicação utilizada nos testes pertence a terceiros e funciona exclusivamente como ambiente de referência para a automação.

---

## 🎯 Objetivo do projeto

Desenvolver uma estrutura de automação capaz de validar fluxos funcionais de uma aplicação web, mantendo organização, rastreabilidade e informações suficientes para analisar os resultados das execuções.

### Objetivos específicos

- Automatizar cenários funcionais de navegação, catálogo, carrinho e checkout.
- Organizar o código utilizando Page Object Model.
- Separar os cenários de teste da implementação das interações com a interface.
- Utilizar Pytest para executar os testes e validar seus resultados.
- Documentar os cenários funcionais utilizando BDD/Gherkin.
- Registrar evidências das etapas executadas.
- Gerar logs técnicos para acompanhamento e investigação de falhas.
- Consolidar os resultados em relatórios PDF.
- Organizar os artefatos por identificação de execução.
- Integrar a suíte de testes a uma pipeline CI/CD.

A solução foi estruturada para que os testes possam ser executados localmente ou em ambiente de integração contínua.

---

## 🛠️ Tecnologias e dependências

| Tecnologia | Responsabilidade |
|---|---|
| Python | Linguagem utilizada no desenvolvimento |
| Selenium WebDriver | Automação das interações com o navegador |
| Pytest | Execução, organização e validação dos testes |
| Page Object Model | Separação das responsabilidades de cada página |
| BDD/Gherkin | Documentação dos cenários funcionais |
| ReportLab | Geração dos relatórios em PDF |
| Logging | Registro das operações e resultados |
| python-dotenv | Leitura das variáveis de ambiente |
| Google Chrome | Navegador utilizado nas execuções |
| Git/GitHub | Controle de versão e hospedagem do código |
| GitHub Actions | Execução automatizada em CI/CD |

As dependências Python são gerenciadas pelo arquivo `requirements.txt`, permitindo a instalação dos pacotes necessários ao projeto.

---

## 🏗️ Arquitetura da automação

<img width="1536" height="1024" alt="Python_Selenium Test Automation Flow" src="https://github.com/user-attachments/assets/c024ea8a-2c5d-4d6f-ba9a-c04108ef259a" />

A arquitetura foi organizada em módulos com responsabilidades específicas, evitando concentrar toda a implementação em um único arquivo de teste.

O principal padrão utilizado é o **Page Object Model (POM)**, que separa os métodos de interação com a aplicação dos cenários responsáveis pelas validações.

### 1. Camada de testes — `tests/`

Contém os testes automatizados executados pelo Pytest.

Cada teste representa um fluxo funcional e utiliza os métodos disponibilizados pelos Page Objects para realizar suas operações.

Essa camada é responsável por:

- Organizar a sequência de execução do cenário.
- Chamar os métodos necessários para interagir com a aplicação.
- Realizar as validações funcionais.
- Registrar as etapas relevantes da execução.
- Identificar falhas e resultados dos testes.

### 2. Camada de páginas — `pages/`

Contém os Page Objects que representam as diferentes áreas da aplicação.

Cada classe concentra os locators e os métodos necessários para interagir com os elementos de sua respectiva página ou componente.

Entre os módulos implementados estão os responsáveis por:

- Navegação e menu.
- Header.
- Catálogo de produtos.
- Página de detalhes do produto (PDP).
- Carrinho.
- Checkout e pagamento.
- Confirmação da compra.

Essa separação permite reutilizar métodos em diferentes testes e concentrar alterações de elementos da interface nos Page Objects correspondentes.

### 3. Camada de configuração — `config/`

Centraliza as configurações utilizadas durante a execução.

O projeto utiliza variáveis de ambiente para separar parâmetros e dados de teste da implementação dos cenários.

Entre as configurações estão:

- URL da aplicação.
- Ambiente de execução.
- Timeout.
- Credenciais e dados necessários aos testes.
- Informações utilizadas no fluxo de checkout.

O arquivo `configuracoes.py` concentra o acesso às configurações utilizadas pela automação.

### 4. Camada de utilitários — `utils/`

Reúne funcionalidades compartilhadas que dão suporte à execução dos testes.

**`evidencia.py`**

Responsável pela captura e organização das evidências visuais. Inclui o tratamento dos nomes dos arquivos para evitar caracteres incompatíveis com o armazenamento de artefatos.

**`logger.py`**

Responsável pela configuração e pelo registro dos logs, permitindo acompanhar as operações executadas e identificar falhas.

**`relatorio_pdf.py`**

Responsável pela geração do relatório consolidado, reunindo os cenários BDD, as evidências e os logs da execução.

### 5. Orquestração — Pytest

O Pytest é utilizado para executar a suíte de testes, realizar as validações e consolidar os resultados individuais.

Os testes são executados de maneira independente, permitindo identificar qual cenário apresentou falha sem confundir seu resultado com o dos demais.

### 6. Integração contínua — GitHub Actions

A pipeline executa a automação em um ambiente de integração contínua.

O projeto contempla ajustes específicos para o ambiente CI, incluindo a padronização da resolução do navegador, reduzindo diferenças de comportamento relacionadas à área de visualização.

Os resultados e artefatos gerados ficam disponíveis para análise das execuções.

---

## 📁 Organização do projeto

A estrutura está dividida conforme a responsabilidade dos módulos.

| Diretório ou arquivo | Finalidade |
|---|---|
| `.github/workflows/` | Definição da pipeline CI/CD |
| `tests/` | Testes automatizados |
| `pages/` | Page Objects e métodos de interação |
| `cenarios/` | Cenários documentados em BDD |
| `config/` | Configurações e variáveis de ambiente |
| `utils/` | Utilitários compartilhados |
| `evidencias/` | Capturas de tela organizadas por execução |
| `logs/` | Logs técnicos das execuções |
| `reports/` | Relatórios consolidados em PDF |
| `requirements.txt` | Dependências Python |
| `.gitignore` | Arquivos e diretórios ignorados pelo Git |
| `README.md` | Documentação do projeto |

A organização permite manter o código dos testes separado dos recursos de configuração, interação e geração de artefatos.

---

## 🧪 Cenários automatizados

A versão 1.0 contempla três testes funcionais que representam diferentes etapas da jornada de compra.

### CT-01 — Catálogo e detalhes do produto

**Teste:** `test_acessar_catalogo_e_visualizar_produto`

**Objetivo:** validar a navegação até o catálogo e a interação com a página de detalhes de um produto.

**Fluxo:**

1. Acessar a página inicial.
2. Selecionar a opção de catálogo.
3. Verificar a apresentação dos produtos.
4. Localizar e selecionar o produto definido no cenário.
5. Acessar a página de detalhes do produto.
6. Acionar a opção de adicionar ao carrinho.
7. Validar o resultado esperado.

### CT-02 — Adicionar produtos ao carrinho

**Teste:** `test_adicionar_produtos_ao_carrinho`

**Objetivo:** validar a seleção de diferentes produtos e sua permanência no carrinho.

**Fluxo:**

1. Acessar o catálogo.
2. Selecionar o primeiro produto.
3. Acessar sua página de detalhes.
4. Adicionar o produto ao carrinho.
5. Retornar ao catálogo.
6. Selecionar um segundo produto.
7. Adicioná-lo ao carrinho.
8. Acessar o carrinho.
9. Verificar os produtos adicionados.

### CT-03 — Fluxo de compra

**Teste:** `test_fluxo_compra`

**Objetivo:** validar a jornada de compra, desde a seleção do produto até a confirmação da transação.

**Fluxo:**

1. Acessar o catálogo.
2. Selecionar um produto.
3. Adicioná-lo ao carrinho.
4. Acessar o checkout.
5. Validar a presença do produto no resumo da compra.
6. Preencher os dados obrigatórios de contato e entrega.
7. Preencher as informações de pagamento.
8. Preencher e validar o CPF.
9. Acionar o botão de finalização do pagamento.
10. Verificar a mensagem de confirmação da compra.

O fluxo de checkout inclui tratamento de validações dinâmicas da interface, utilizando interações do Selenium e esperas específicas para acompanhar a atualização dos elementos.

---

## 🧩 Documentação dos cenários BDD

Os cenários funcionais são documentados separadamente da implementação dos testes.

A documentação utiliza a estrutura BDD/Gherkin para representar as condições iniciais, as ações realizadas e os resultados esperados.

Exemplo simplificado:

```gherkin
Feature: Fluxo de compra

  Scenario: Finalizar a compra de um produto

    Given que o usuário acessou a aplicação
    When seleciona um produto no catálogo
    And adiciona o produto ao carrinho
    And preenche os dados obrigatórios do checkout
    And finaliza o pagamento
    Then a confirmação da compra deve ser apresentada
```

Os arquivos de cenário são utilizados como documentação e também compõem o relatório consolidado.

O projeto não depende da execução direta de arquivos `.feature` por um framework BDD. A automação é executada pelo Pytest.

---

## ⚙️ Configuração do ambiente local

### Pré-requisitos

Para executar o projeto localmente, são necessários:

- Python instalado.
- Google Chrome.
- Git.
- Acesso à aplicação utilizada nos testes.
- Configuração dos dados necessários à execução.

### 1. Clonar o repositório

```bash
git clone https://github.com/Rodrigopca42/qa-automation-python-selenium.git
cd qa-automation-python-selenium
```

### 2. Criar o ambiente virtual

```powershell
python -m venv .venv
```

### 3. Ativar o ambiente virtual

No Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Instalar as dependências

```powershell
pip install -r requirements.txt
```

### 5. Configurar as variáveis de ambiente

O projeto utiliza configurações centralizadas em `config/configuracoes.py`, com leitura de variáveis de ambiente.

Para a execução local, os valores necessários devem ser definidos no ambiente ou em um arquivo `.env` na raiz do projeto.

O arquivo `.env` não deve ser enviado ao GitHub.

### 6. Executar a suíte completa

```powershell
python -m pytest tests/ -v
```

### 7. Executar um teste específico

Exemplo para o fluxo de compra:

```powershell
python -m pytest tests/test_fluxo_compra.py -v
```

Ao final da execução, os resultados são apresentados pelo Pytest e os artefatos são organizados nos diretórios correspondentes.

---

## 📸 Evidências de teste

O Selenium captura evidências visuais em etapas relevantes dos cenários.

As capturas documentam o estado da aplicação durante a execução, permitindo verificar as ações realizadas e auxiliar a análise de falhas.

As evidências podem incluir:

- Página inicial.
- Catálogo e seleção de produtos.
- Página de detalhes.
- Carrinho.
- Etapas do checkout.
- Resultado da compra.
- Estado da aplicação quando ocorre uma falha.

Os arquivos são organizados por execução para evitar a sobrescrita dos registros anteriores.

---

## 📝 Logs e tratamento de falhas

Os logs registram informações técnicas sobre o andamento dos testes.

Entre os registros estão:

- Início do cenário.
- Ações executadas.
- Navegação entre páginas.
- Validações realizadas.
- Erros e exceções.
- Resultado final.

Quando uma falha ocorre, o objetivo é registrar informações suficientes para identificar a etapa afetada e auxiliar o diagnóstico.

A estrutura diferencia a falha de execução da automação de um possível defeito funcional da aplicação. Um teste marcado como `FAIL` não significa, necessariamente, que foi encontrado um bug no sistema.

---

## 📄 Relatório consolidado em PDF

O projeto gera automaticamente um relatório consolidado com os resultados dos testes.

O relatório apresenta:

- Identificação da execução.
- Ambiente de teste.
- Resumo quantitativo dos resultados.
- Percentuais de aprovação e reprovação.
- Resultado e duração de cada teste.
- Cenários BDD.
- Evidências visuais.
- Logs técnicos.

### Organização do relatório

Cada teste inicia em uma nova página e segue a sequência:

**Cenário BDD → Evidências → Logs**

Essa organização facilita a leitura e mantém relacionados o comportamento esperado, as evidências produzidas e os registros técnicos da execução.

O relatório é gerado tanto para execuções aprovadas quanto para execuções com falhas.

---

## 🆔 Identificação e rastreabilidade

Cada execução recebe um identificador baseado em data e horário.

**Formato:**

`YYYY-MM-DD_HH-MM-SS`

**Exemplo:**

`2026-10-30_13-38-09`

O identificador é utilizado na organização dos artefatos, permitindo relacionar os registros pertencentes à mesma execução.

| Diretório | Conteúdo |
|---|---|
| `evidencias/<ID_EXECUCAO>/` | Capturas de tela |
| `logs/<ID_EXECUCAO>/` | Logs da execução |
| `reports/<ID_EXECUCAO>/` | Relatório consolidado |

---

## 🚀 Integração contínua — GitHub Actions

A suíte de testes está integrada ao GitHub Actions.

A pipeline permite executar os cenários automatizados no ambiente de CI/CD e acompanhar seus resultados diretamente pelo repositório.

### Funcionamento

1. O workflow é iniciado conforme sua configuração.
2. O ambiente de execução é preparado.
3. As dependências do projeto são instaladas.
4. Os dados necessários são disponibilizados por meio das configurações do ambiente.
5. O Pytest executa a suíte automatizada.
6. Os resultados são registrados.
7. Os relatórios e as evidências são disponibilizados como artefatos da execução.

O projeto também contempla tratamento de nomes de arquivos para garantir compatibilidade dos artefatos com o GitHub Actions.

### Validação da versão 1.0

A suíte foi validada localmente e na pipeline.

Na etapa final de validação, foram registradas **três execuções consecutivas aprovadas no GitHub Actions**.

Esses resultados demonstram o funcionamento da solução nas execuções observadas, sem representar garantia de ausência de falhas futuras.

---

## 🔐 Segurança e gerenciamento de dados

O projeto separa os dados de configuração do código-fonte.

As informações utilizadas localmente são gerenciadas por variáveis de ambiente, enquanto o GitHub Actions utiliza configurações e secrets para disponibilizar os dados necessários à pipeline.

O arquivo `.gitignore` evita o versionamento de arquivos locais que não devem integrar o repositório, como o ambiente virtual, arquivos de cache e configurações sensíveis.

Os dados utilizados nos cenários de pagamento devem ser apropriados ao ambiente de homologação.

Relatórios e evidências também devem ser revisados antes de compartilhamento público, evitando a exposição de informações pessoais ou confidenciais.

---

## 📊 Resultados da versão 1.0

A versão 1.0 foi concluída com três cenários funcionais automatizados.

| Indicador | Resultado |
|---|---|
| Cenários automatizados | 3 |
| Testes aprovados na execução consolidada | 3 |
| Testes reprovados | 0 |
| Taxa de aprovação observada | 100% |
| Execuções consecutivas aprovadas no CI/CD | 3 |
| Integração com GitHub Actions | Implementada |
| Relatório consolidado PDF | Implementado |
| Captura de evidências e logs | Implementada |

Os resultados representam a execução dos cenários implementados, não a cobertura funcional completa da aplicação.

---

## 📌 Escopo e considerações

Este projeto foi desenvolvido de forma independente, para demonstrar a aplicação prática de conhecimentos em automação de testes e qualidade de software.

A aplicação web utilizada como referência pertence a terceiros. O repositório não representa o código-fonte da aplicação nem uma participação em seu desenvolvimento.

A solução automatiza fluxos funcionais selecionados e não pretende substituir uma estratégia completa de testes, que pode envolver outras modalidades de validação.

A arquitetura permite manutenção e evolução futura, mas o escopo definido para a versão 1.0 está concluído.

---

## 👨‍💻 Conclusão

O desenvolvimento deste projeto permitiu construir uma solução de automação funcional que integra organização arquitetural, execução
