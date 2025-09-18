import os
import argparse
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser

# --- CONFIGURAÇÃO INICIAL ---
# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Validação das variáveis de ambiente essenciais
required_env_vars = [
    "AZURE_OPENAI_API_KEY",
    "AZURE_OPENAI_ENDPOINT",
    "AZURE_OPENAI_API_VERSION",
    "AZURE_OPENAI_DEPLOYMENT_NAME",
]

for var in required_env_vars:
    if not os.getenv(var):
        raise ValueError(
            f"A variável de ambiente '{var}' não foi definida. Por favor, configure o arquivo .env.")

# --- LÓGICA DO AGENTE ---


def criar_agente_gerador_testes():
    """
    Configura e retorna uma cadeia (chain) da LangChain pronta para gerar testes.
    """
    # Template do prompt, instruindo o modelo sobre como gerar os testes
    prompt_template = """
    Você é um especialista em desenvolvimento de software e testes de qualidade (QA) em Python.
    Sua tarefa é criar um arquivo de teste unitário completo usando a biblioteca pytest para o código Python fornecido.

    Diretrizes para a geração dos testes:
    1.  O arquivo de teste deve começar com 'import pytest'.
    2.  Importe as funções necessárias do módulo original. O nome do módulo é '{module_name}'.
    3.  Crie funções de teste seguindo o padrão 'def test_<nome_da_funcao>_<cenario>()'.
    4.  Para cada função no código fornecido, gere os seguintes cenários:
        - Pelo menos um teste de "caminho feliz" (caso de sucesso com entradas válidas).
        - Testes para casos de falha e exceções (ex: divisão por zero, tipos de dados inválidos). Utilize 'pytest.raises' para capturar exceções.
        - Testes para casos extremos (edge cases), como números negativos, zero, strings vazias, etc.
    5.  O código gerado deve ser um arquivo Python puro e completo, sem nenhuma explicação ou comentário extra fora do código.
    6.  Não envolva o código em blocos de markdown como ```python ... ```.

    Abaixo está o código Python para o qual você deve gerar os testes:
    ---
    {python_code}
    ---
    """

    # Modelo da Azure OpenAI
    llm = AzureChatOpenAI(
        azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
        openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    )

    # Criação do prompt a partir do template
    prompt = ChatPromptTemplate.from_template(prompt_template)

    # Parser para extrair a string de resultado
    output_parser = StrOutputParser()

    # Montagem da cadeia (chain) que conecta o prompt, o modelo e o parser
    chain = prompt | llm | output_parser

    return chain


def limpar_bloco_de_codigo(texto_gerado: str) -> str:
    """
    Remove os marcadores de bloco de código (```python e ```) da string gerada pelo LLM.
    """
    # Remove ```python do início, ignorando espaços em branco
    texto_limpo = texto_gerado.strip()
    if texto_limpo.startswith("```python"):
        texto_limpo = texto_limpo[9:]  # Remove os 9 primeiros caracteres
    # Remove ``` do início (caso não tenha o 'python')
    elif texto_limpo.startswith("```"):
        texto_limpo = texto_limpo[3:]

    # Remove ``` do final
    if texto_limpo.endswith("```"):
        texto_limpo = texto_limpo[:-3]

    return texto_limpo.strip()


def gerar_arquivo_testes(caminho_arquivo_python: str):
    """
    Lê um arquivo Python, gera os testes e salva em um novo arquivo.
    """
    print(f"Lendo o arquivo de entrada: {caminho_arquivo_python}")

    try:
        with open(caminho_arquivo_python, 'r', encoding='utf-8') as f:
            codigo_python = f.read()
    except FileNotFoundError:
        print(
            f"Erro: O arquivo '{caminho_arquivo_python}' não foi encontrado.")
        return

    # Extrai o nome do módulo (sem a extensão .py)
    nome_modulo = os.path.splitext(os.path.basename(caminho_arquivo_python))[0]

    # Define o nome do arquivo de saída
    diretorio = os.path.dirname(caminho_arquivo_python)
    nome_arquivo_teste = f"test_{nome_modulo}.py"
    caminho_saida = os.path.join(diretorio, nome_arquivo_teste)

    print("Iniciando a geração de testes com a IA...")

    # Cria o agente e invoca com o código
    agente = criar_agente_gerador_testes()
    testes_gerados_brutos = agente.invoke({
        "module_name": nome_modulo,
        "python_code": codigo_python
    })

    # PASSO DE LIMPEZA ADICIONADO AQUI
    testes_limpos = limpar_bloco_de_codigo(testes_gerados_brutos)

    print(f"Testes gerados com sucesso. Salvando em: {caminho_saida}")

    # Salva o resultado no arquivo de teste
    # Salva o resultado LIMPO no arquivo de teste
    with open(caminho_saida, 'w', encoding='utf-8') as f:
        f.write(testes_limpos)

    print("\nProcesso concluído!")


# --- EXECUÇÃO DO SCRIPT ---

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Agente de IA para gerar testes unitários com Pytest a partir de um arquivo Python."
    )
    parser.add_argument(
        "arquivo",
        type=str,
        help="Caminho para o arquivo Python que contém as funções a serem testadas."
    )

    args = parser.parse_args()
    gerar_arquivo_testes(args.arquivo)
