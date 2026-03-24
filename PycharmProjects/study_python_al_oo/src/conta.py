class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print('Contruindo um objeto... {}'.format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    def __pode_sacar(self, valor_a_sacar):
        return valor_a_sacar <= (self.__saldo + self.__limite)

    def extrato(self):
        print('Saldo de {} do titular {}'.format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor_a_sacar):
        if self.__pode_sacar(valor_a_sacar):
            self.__saldo -= valor_a_sacar
        else:
            print('O valor {} passou do limite'.format(valor_a_sacar))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @staticmethod
    def codigo_banco():
        return '001'

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}

