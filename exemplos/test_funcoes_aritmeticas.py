import pytest
from funcoes_aritmeticas import soma, subtracao, divisao

def test_soma_caminho_feliz():
    assert soma(2, 3) == 5
    assert soma(10.5, 4.5) == 15

def test_soma_tipos_invalidos():
    with pytest.raises(TypeError):
        soma("2", 3)
    with pytest.raises(TypeError):
        soma(2, None)
    with pytest.raises(TypeError):
        soma([], {})

def test_soma_casos_extremos():
    assert soma(-10, 20) == 10
    assert soma(0, 0) == 0
    assert soma(1000000000, -1000000000) == 0

def test_subtracao_caminho_feliz():
    assert subtracao(10, 5) == 5
    assert subtracao(7.5, 2.5) == 5.0

def test_subtracao_casos_extremos():
    assert subtracao(-10, 5) == -15
    assert subtracao(0, 0) == 0
    assert subtracao(1000000000, -1000000000) == 2000000000

def test_divisao_caminho_feliz():
    assert divisao(10, 2) == 5
    assert divisao(7.5, 2.5) == 3.0

def test_divisao_divisao_por_zero():
    with pytest.raises(ValueError):
        divisao(10, 0)

def test_divisao_casos_extremos():
    assert divisao(-10, 2) == -5
    assert divisao(0, 100) == 0
    assert divisao(1, 1e-9) == 1e9