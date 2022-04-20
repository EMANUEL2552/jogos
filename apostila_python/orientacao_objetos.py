def cria_conta(numero, titular, saldo, limite):
    conta = {'numero': numero, 'titular': titular, 'saldo': saldo, 'limite':, limite}
    return conta

conta1 = cria_conta('123-4', 'joao', 120.0, 1000.0)
conta2 = cria_conta('123-5', 'jose', 200.0, 1000.0)

def deposita (conta, valor):
    conta['saldo']+= valor
def saca(conta, valor):
    conta['saldo']-= valor

def extrato(conta):
    print('numero: {} \nsaldo: {}'.format(conta['numero'], conta['saldo']))

conta = cria_conta('123-4', 'joao', 120.0, 1000.0)
deposita(conta, 15.0)
extrato(conta)