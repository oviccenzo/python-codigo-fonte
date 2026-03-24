class ExtratorArgumentosUrl:
    def __init__(self, url):
        if self.url_eh_valida(url):
            self.url = url.lower()
        else:
            raise LookupError('Url inválida!!!')


    def __len__(self):
        return len(self.url)


    def __str__(self):
        moeda_origem, moeda_destino = self.extrai_argumentos()
        valor = self.extrai_valor()

        #return 'Valor: {} \nMoeda Origem: {} \nMoeda Destino: {}\n'.format(valor, moeda_origem, moeda_destino)
        return f'Valor: {valor} \nMoeda Origem: {moeda_origem} \nMoeda Destino: {moeda_destino}\n'

    def __eq__(self, other):
        return self.url == other.url


    @staticmethod
    def url_eh_valida(url):
        if url and url.startswith('https://www.bytebank.com.br'):
            return True
        else:
            return False


    def extrai_argumentos(self):
        busca_moeda_origem = 'moedaorigem='.lower()
        busca_moeda_destino = 'moedadestino='.lower()
        busca_valor_origem = '&valor='

        if self.url.count('moedadestino') > 1:
            self.troca_moeda_origem()

        indice_inicial_moeda_origem = self.encontra_indice_inicial(busca_moeda_origem)
        indice_final_moeda_origem = self.url.find('&')

        indice_inicial_moeda_destino = self.encontra_indice_inicial(busca_moeda_destino)
        indice_final_moeda_destino = self.url.find(busca_valor_origem)

        moeda_origem = self.url[indice_inicial_moeda_origem:indice_final_moeda_origem]
        moeda_destino = self.url[indice_inicial_moeda_destino:indice_final_moeda_destino]

        return moeda_origem, moeda_destino


    def extrai_valor(self):
        busca_valor_origem = 'valor='
        indice_valor_origem = self.encontra_indice_inicial(busca_valor_origem)
        return self.url[indice_valor_origem:]


    def encontra_indice_inicial(self, moeda_buscada):
        return self.url.find(moeda_buscada) + len(moeda_buscada)

    def troca_moeda_origem(self):
        self.url = self.url.replace('moedadestino', 'real', 1)

