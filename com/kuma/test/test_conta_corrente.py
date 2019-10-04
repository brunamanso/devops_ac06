"""arquivo de calculo de parcela"""
def test_alterarN():
    conta_corrente.alterarNome('Luis')
    assert conta_corrente.nomeCorrentista == 'Luis'


"""arquivo de calculo de parcela"""
def test_deposito():
    conta_corrente.deposito(100)
    assert conta_corrente.saldo == 100


"""arquivo de calculo de parcela"""
def test_saque():
    conta_corrente.saque(100)
    assert conta_corrente.saldo == 0
