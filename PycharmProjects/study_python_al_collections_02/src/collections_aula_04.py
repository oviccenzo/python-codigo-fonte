from collections import  defaultdict

meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
meu_texto_preparado = meu_texto.lower()
print(meu_texto_preparado)

aparicoes = {}
for palavra in meu_texto_preparado.split():
    ate_agora = aparicoes.get(palavra, 0)
    aparicoes[palavra] = ate_agora + 1

print(aparicoes)

aparicoes = defaultdict(int)
for palavra in meu_texto_preparado.split():
    ate_agora = aparicoes[palavra]
    aparicoes[palavra] = ate_agora + 1
print(aparicoes)



aparicoes = defaultdict(int)
for palavra in meu_texto_preparado.split():
    aparicoes[palavra] += 1
print(aparicoes)

###########
from collections import Counter
aparicoes = Counter(meu_texto_preparado.split())

print(aparicoes)
