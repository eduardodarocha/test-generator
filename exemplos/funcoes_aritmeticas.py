def soma(a, b):
    """Retorna a soma de dois números."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Ambas as entradas devem ser numéricas.")
    return a + b


def subtracao(a, b):
    """Retorna a subtração de dois números."""
    return a - b


def divisao(a, b):
    """Retorna a divisão de a por b. Lança uma exceção para divisão por zero."""
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b
