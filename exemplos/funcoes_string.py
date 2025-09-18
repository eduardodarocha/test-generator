# funcoes_string.py

def inverter_string(s: str) -> str:
    """Inverte uma string."""
    return s[::-1]


def eh_palindromo(s: str) -> bool:
    """Verifica se uma string é um palíndromo, ignorando espaços e caixa."""
    s_normalizada = "".join(filter(str.isalnum, s)).lower()
    return s_normalizada == s_normalizada[::-1]
