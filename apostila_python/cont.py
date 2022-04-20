

class Conta:

    _total_contas = 0

def __init__(self, saldo):
    self._saldo = saldo
Conta.total_contas +=1

@staticmethod
def get_total_contas():
    return Conta._total_contas

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if(saldo < 0 ):
            print('saldo n pode ser negativo')
        else:
            self._saldo = saldo

    def set_saldo(self, saldo):
        if (saldo < 0):
            print('saldo n pode ser menor que 0')
        else:
            self.saldo = saldo


    def get_saldo(self):
        return self._saldo


    def get_titular(self):
        return self._titular
    def set_titular(self, titular):

        self._titular = titular

    def deposita(self, valor):
        self.saldo += valor

    def saca (self, valor):
        if (self.saldo < valor):
            return False
        else:
            self.saldo -= valor
        return True

    def extrato (self, numero, saldo):
        print('numero: {} \nsaldo: {}'.format(self.numero, self.saldo))

    def tranfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            return True

    def pega_saldo(self):
        return self.saldo





