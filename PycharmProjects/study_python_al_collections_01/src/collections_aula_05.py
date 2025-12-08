idades = [15, 87, 32, 65, 56, 32, 49, 37]

for posicao in range(len(idades)):
    print(posicao)

print(list(enumerate(idades)))

for valor in enumerate(idades):
    print(valor)

for indice, idade in enumerate(idades):
    print(indice, idade)

usuarios = [
    ('Guilherme', 37, 1981),
    ('Daniela', 31, 1981),
    ('Paulo', 39, 1979)
]

for nome, idade, nascimento in usuarios:
    #print(nome)
    print(nome, idade)

for nome, _, _ in usuarios:
    print(nome)

#print(' '.join(str(idade) for idade in reversed(idades)))

#print(*sorted(idades), sep = ' ')

print(*sorted(idades), sep = '  ') ### ordena a lista

print(*reversed(idades), sep = '  ') ### nao ordena a lista em ordem reversa, mas apenas retorna a lista em ordem reversa

print(*sorted(idades, reverse = True), sep = '  ') ### ordena em ordem reversa
