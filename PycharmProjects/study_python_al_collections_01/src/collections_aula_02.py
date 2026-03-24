class ContaCorrente:

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return '[>>Codigo {} - Saldo {}<<]'.format(self.codigo, self.saldo)

'''
conta_do_gui = ContaCorrente(12321)
conta_do_gui.deposita(300)

conta_da_dani = ContaCorrente(600)
conta_da_dani.deposita(100)

#print(conta_da_dani)
#print(conta_do_gui)

contas = [conta_do_gui, conta_da_dani]

for conta in contas:
    print(conta)
'''
guilherme = ('Guilherme', 37, 1981)
daniela = ('Daniela', 31, 1981)

#print(guilherme)
#print(daniela)

usuarios = [guilherme, daniela]

paulo = ('Paulo', 35, 1983)
print(usuarios)

usuarios.append(paulo)
print(usuarios)

