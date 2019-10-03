import pytest
from com.bbjp.calcula_parcela import valorPagamento


def test_valor0():
        assert valorPagamento(-1, 5) == None


def test_valor2():
        assert valorPagamento(500, 50) == 765.0


def test_valor1():
        assert valorPagamento(500, -1) == 500



