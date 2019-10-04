import pytest
from com.kuma.conta_corrente import ContaCorrente

conta_corrente = ContaCorrente(1,'Luis',0.0)

def test_alterarN():
    conta_corrente.alterarNome('Luis')
    assert conta_corrente.nomeCorrentista == 'Luis'

def test_deposito():
    conta_corrente.deposito(100)
    assert conta_corrente.saldo == 100

def test_saque():
    conta_corrente.saque(100)
    assert conta_corrente.saldo == 0