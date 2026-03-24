import numpy as np
from abc import ABCMeta, abstractmethod
from operator import attrgetter
from functools import total_ordering

@total_ordering
class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, other):
        if not isinstance(other, ContaSalario):
            return False
        # pode checar se sao mesmo tipo por isinstance ou type(other)
        #if type(other) != ContaSalario:
        #    return False
        return self._codigo == other._codigo and self._saldo == other._saldo

    def __lt__(self, other):
        if self._saldo != other._saldo:
            return self._saldo < other._saldo
        return self._codigo < other._codigo

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return '[>> Codigo {} - Saldo {} <<]'.format(self._codigo, self._saldo)

conta_gui = ContaSalario(3)
conta_gui.deposita(200)
conta_dani = ContaSalario(17)
conta_dani.deposita(300)
conta_paulo = ContaSalario(133)
conta_paulo.deposita(200)

print(conta_dani == conta_gui)

contas = [conta_dani, conta_gui, conta_paulo]
print(*contas, sep='  ')
print('   ')

def extrai_saldo(conta):
    return conta._saldo

# print(*sorted(contas, key=extrai_saldo), sep='  ')
for conta in contas:
    print(conta)
print('   ')

for conta in sorted(contas, key=attrgetter('_saldo', '_codigo')):
    print(conta)
print('   ')

for conta in sorted(contas):
    print(conta)
print('   ')

for conta in sorted(contas, reverse=True):
    print(conta)

print(conta_paulo <=  conta_dani)
print(conta_paulo <=  conta_gui)
print(conta_gui <= conta_paulo)
print(conta_gui <= conta_gui)


