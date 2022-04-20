from clientes import Cliente
class Conta:

    def __init__(self, clientes, numero, saldo = 0):
        self.saldo = saldo
        self.clientes= clientes
        self.numero = numero
        self.operaçoes = []


    def resumo(self):
        print('CC numero: %s Saldo : %10.2f'%
              (self.numero, self.saldo, ))

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operaçoes.append(['SAQUE', valor])





    def deposito(self, valor):
        self.saldo += valor
        self.operaçoes.append(['DEPOSITO', valor])

    def extrato(self):
        print('Extrato CC n %s\n'% self.numero)
        for o in self.operaçoes:
            print('%10s %10.2f' % (o [0], o [1]) )


class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo = 0, limite = 0):
        Conta.__init__(self, clientes, numero, saldo)
        self.limite = limite

    def saque(self, valor):
        if self.saldo + self.limite>=valor:
            self.saldo -= valor
            self.operaçoes.append(['SAQUE', valor])
    def extrato(self):
        print(f' extrato CE: limite: {self.limite}, total disponivel {self.saldo}')