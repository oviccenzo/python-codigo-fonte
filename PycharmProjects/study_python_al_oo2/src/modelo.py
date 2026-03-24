class Programa:

    def __init__(self, nome, ano):
        self._nome = nome.title()
        self._ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, ano):
        self._ano = ano

    @property
    def likes(self):
        return self._likes

    @likes.setter
    def likes(self, likes):
        self._likes = likes

    def dar_likes(self):
        self._likes += 1


class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.__duracao = duracao

    @property
    def duracao(self):
        return self.__duracao

    @duracao.setter
    def duracao(self, duracao):
        self.__duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self._ano} - {self.__duracao} min - {self._likes} likes'


class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.__temporadas = temporadas

    @property
    def temporadas(self):
        return self.__temporadas

    @temporadas.setter
    def temporadas(self, temporadas):
        self.__temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self._ano} - {self.__temporadas} temporadas - {self._likes} likes'


class Playlist:

    def __init__(self, nome, programas):
        self._nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('Atlanta', 2018, 2)
argo = Filme('Argo', 2002, 160)
demolidor = Serie('demolidor', 2016, 3)


vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
argo.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()


filmes_e_series = [vingadores, atlanta, demolidor, argo]

playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'O tamanho da playlist é: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana:
    print(programa)
