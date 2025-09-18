import pytest
from funcoes_string import inverter_string, eh_palindromo

def test_inverter_string_caminho_feliz():
    assert inverter_string("python") == "nohtyp"
    assert inverter_string("abc") == "cba"

def test_inverter_string_string_vazia():
    assert inverter_string("") == ""

def test_inverter_string_uma_letra():
    assert inverter_string("a") == "a"

def test_inverter_string_espacos():
    assert inverter_string("   ") == "   "

def test_inverter_string_caracteres_especiais():
    assert inverter_string("@#%") == "%#@"
    assert inverter_string("123!abc!") == "!cba!321"

def test_eh_palindromo_caminho_feliz():
    assert eh_palindromo("radar") is True
    assert eh_palindromo("A man a plan a canal Panama") is True
    assert eh_palindromo("aba") is True

def test_eh_palindromo_nao_palindromo():
    assert eh_palindromo("python") is False
    assert eh_palindromo("abc") is False

def test_eh_palindromo_string_vazia():
    assert eh_palindromo("") is True

def test_eh_palindromo_uma_letra():
    assert eh_palindromo("a") is True
    assert eh_palindromo("Z") is True

def test_eh_palindromo_caracteres_especiais():
    assert eh_palindromo("!!!") is True
    assert eh_palindromo("123, 321") is True

def test_eh_palindromo_com_espacos():
    assert eh_palindromo("  ") is True
    assert eh_palindromo(" A  B A ") is True