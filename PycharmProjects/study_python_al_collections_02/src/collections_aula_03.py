aparicoes = {
    'Guilherme': 1,
    'cachorro': 2,
    'nome': 2,
    'vindo': 1,
}

print(aparicoes)

print(aparicoes['nome'])

print(aparicoes['cachorro'])

print(aparicoes.get('xpto', 0))

print(aparicoes.get('Guilherme', 0))

print(type(aparicoes))

#adicionando elementos no dicionario
aparicoes['Carlos'] = 3

print(aparicoes)

for k in aparicoes.keys():
    print(f'{k}')
print('    ')

for v in aparicoes.values():
    print(f'{v}')
print('    ')

for k, v in aparicoes.items():
    print(f'{k} - {v}')
print('    ')

for item in aparicoes.items():
    print(item)
print('    ')

print([f'palavra {chave}' for chave in aparicoes.keys()])

print(['word {}'.format(chave) for chave in aparicoes.keys()])
