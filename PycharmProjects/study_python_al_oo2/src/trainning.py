class Pessoa:

    TAMANHO_CPF = 11

    def __init__(self, cpf, nome):
        self.__cpf = cpf
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    def valida_cpf(self):
        return True if len(self.__cpf) == __class__.TAMANHO_CPF else False

pf = Pessoa('99999999999', 'Ruby')
print(pf.valida_cpf())

pj = Pessoa('999999999999999', 'Cristal')
print(pj.valida_cpf())