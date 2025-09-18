import pytest
from funcoes_aritmeticas import soma, subtracao, divisao

def test_soma_caminho_feliz():
    assert soma(3, 5) == 8
    assert soma(-2, 2) == 0
    assert soma(3.5, 2.5) == 6.0

def test_soma_tipo_invalido():
    with pytest.raises(TypeError):
        soma(3, "5")
    with pytest.raises(TypeError):
        soma("a", "b")
    with pytest.raises(TypeError):
        soma(None, 5)

def test_soma_casos_extremos():
    assert soma(0, 0) == 0
    assert soma(-1000, -2000) == -3000
    assert soma(1e10, 1e10) == 2e10

def test_subtracao_caminho_feliz():
    assert subtracao(10, 5) == 5
    assert subtracao(-2, -3) == 1
    assert subtracao(7.5, 2.5) == 5.0

def test_subtracao_casos_extremos():
    assert subtracao(0, 0) == 0
    assert subtracao(-1000, -500) == -500
    assert subtracao(1e10, 1e5) == 9.9999e9

def test_divisao_caminho_feliz():
    assert divisao(10, 2) == 5
    assert divisao(7.5, 2.5) == 3.0
    assert divisao(-10, 5) == -2

def test_divisao_por_zero():
    with pytest.raises(ValueError):
        divisao(10, 0)
    with pytest.raises(ValueError):
        divisao(-5, 0)

def test_divisao_casos_extremos():
    assert divisao(0, 1) == 0
    assert divisao(1e10, 1e5) == 1e5
    assert divisao(-100, 20) == -5