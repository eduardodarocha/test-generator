# Desafio: Gerador de Testes Unitários com IA

Este projeto implementa um agente de Inteligência Artificial que gera automaticamente testes unitários em Python usando a biblioteca `pytest`. O agente é construído com LangChain e se conecta a um modelo de linguagem hospedado no Azure OpenAI.

## Descrição do Projeto

O objetivo principal deste agente é acelerar o ciclo de desenvolvimento de software, automatizando a criação de testes básicos e complexos. Ao fornecer um arquivo Python contendo uma ou mais funções, o agente analisa o código e gera um arquivo de teste correspondente, cobrindo casos de sucesso, falhas e casos extremos (edge cases).

### Funcionalidades

- Recebe um arquivo Python como entrada via linha de comando.
- Utiliza a plataforma Azure OpenAI para gerar código de alta qualidade.
- Orquestra as chamadas de API através da biblioteca LangChain.
- Gera um arquivo `test_*.py` seguindo as convenções do `pytest`.
- Cria automaticamente testes para:
  - Casos de sucesso (caminho feliz).
  - Casos de falha (ex: entradas inválidas, erros esperados).
  - Casos extremos (ex: zero, números negativos, strings vazias).

## Estrutura do Projeto

```
desafio-ia-testes/
├── agente/
│   └── gerador_testes.py   # O código principal do agente
├── exemplos/
│   ├── funcoes_aritmeticas.py  # Código de exemplo para testar
│   └── funcoes_string.py       # Outro código de exemplo
├── .env.example                # Template para as variáveis de ambiente
├── README.md                   # Este arquivo
└── requirements.txt            # Dependências do Python
```

## Passo a Passo para Execução

### 1. Pré-requisitos

- Python 3.8 ou superior
- Acesso a um recurso do Azure OpenAI com um modelo de chat (como GPT-3.5-Turbo ou GPT-4) implantado.
- `git` instalado.

### 2. Configuração do Ambiente

Primeiro, clone o repositório e navegue até a pasta do projeto:

```bash
git clone <URL_DO_SEU_REPOSITORIO>
cd teste-generator
```

Crie e ative um ambiente virtual. Isso isola as dependências do projeto.

**No Linux/macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**No Windows:**

```bash
python -m venv venv
.\venv\Scripts\activate
```

Instale as bibliotecas Python necessárias:

```bash
pip install -r requirements.txt
```

### 3. Configuração das Variáveis de Ambiente

O agente precisa das credenciais para se conectar ao serviço Azure OpenAI. Copie o arquivo de exemplo `.env.example` para um novo arquivo chamado `.env`:

```bash
cp .env.example .env
```

Agora, edite o arquivo `.env` e preencha com suas informações do Azure OpenAI.

#### `.env.example`

```ini
# Azure OpenAI Service Keys
# Substitua os valores abaixo pelas suas credenciais do Azure

# Sua chave de API do Azure OpenAI
AZURE_OPENAI_API_KEY="SUA_CHAVE_API_AQUI"

# O endpoint do seu serviço Azure OpenAI (ex: [https://seu-recurso.openai.azure.com/](https://seu-recurso.openai.azure.com/))
AZURE_OPENAI_ENDPOINT="SEU_ENDPOINT_AQUI"

# A versão da API que você está usando (consulte a documentação da Azure)
AZURE_OPENAI_API_VERSION="2023-12-01-preview"

# O nome da implantação (deployment) do seu modelo de chat no Azure
AZURE_OPENAI_DEPLOYMENT_NAME="NOME_DA_SUA_IMPLANTACAO_AQUI"
```

### 4. Como Rodar o Agente

Para gerar os testes, execute o script `gerador_testes.py` a partir da pasta raiz do projeto, passando o caminho do arquivo Python que você deseja testar como argumento.

**Exemplo:**

```bash
python agente/gerador_testes.py exemplos/funcoes_aritmeticas.py
```

Após a execução, um novo arquivo chamado `test_funcoes_aritmeticas.py` será criado dentro da pasta `exemplos/`.

### 5. Executando os Testes Gerados

Para verificar se os testes gerados funcionam corretamente, utilize o `pytest`. Navegue até a pasta onde os testes foram salvos e execute o comando:

```bash
cd exemplos/
pytest
```

Você deverá ver uma saída indicando que todos os testes passaram com sucesso.

```
============================= test session starts ==============================
platform linux -- Python 3.10.12, pytest-7.4.3, pluggy-1.3.0
rootdir: /path/to/desafio-ia-testes/exemplos
collected N items

test_funcoes_aritmeticas.py ......... [100%]

============================== N passed in X.XXs ===============================
```
