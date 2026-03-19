from collections import Counter

texto_01 = '''
Nesse artigo conto como decidimos parar de seguir essa metodologia em cascata e seguir uma metodologia mais fluída.

Uma vez fui contratada por uma empresa que desenvolvia softwares e aplicativos para outras empresas. Nela, um dos meus primeiros trabalhos era auxiliar no desenvolvimento de um aplicativo que visa permitir que as pessoas encontrem restaurantes baratos perto de onde ela se encontra.

Quando conheci o time, já me explicaram que eles seguiam uma estrutura clássica: planejamento, análise, design, documentação, codificação, realizar testes, implementar e, caso necessário, fazer a manutenção do aplicativo.

Essa é uma metodologia de desenvolvimento chamada em cascata, que significa que o processo é realizado por meio de fases e uma delas só é iniciada quando a anterior termina e, assim, não é necessário retornar a um trabalho, já que ele já foi completamente finalizado.

Porém, levamos muito tempo na etapa de planejamento, análise e documentação de todo o projeto e o cliente ficou impaciente de não mostrarmos nenhuma novidade à ele.

Além disso, o que havíamos feito não poderia ser apresentado para o cliente, já que a documentação é para consulta de analistas, arquitetos, desenvolvedores e testers do projeto, ou seja, não era para o cliente.

Então, ele nos informou que o software agora tinha uma finalidade diferente da inicial. Tentamos mudar, porém, precisaríamos analisar, planejar e começar a documentação toda de novo. Pensando no tempo que demoramos para fazer isso, o cliente cancelou e, assim, o trabalho inteiro foi jogado fora.

Vimos que este método não estava mais funcionando. E qual foi o nosso erro?
Como percebemos que estava havendo um obstáculo para a equipe falar para todos em que ponto estava tendo dificuldade, decidimos que deveríamos ter mais integração entre nós, por meio de almoços e conversas durante o café.

E, além disso, conhecer o trabalho um do outro, por meio de reuniões onde cada um poderia dizer o que estava fazendo, o que iria fazer a seguir e se estava tendo alguma dificuldade ou facilidade. Nelas planejamos o que iremos fazer a seguir, além de integrar toda a equipe no processo de desenvolvimento.

Pensamos que processos e ferramentas são importantes, mas eles são feitos e utilizados, respectivamente, pela equipe e a interação entre ela deve estar fluida e equilibrada para que a eficácia dos processos e ferramentas ocorra sem grandes problemas.

Além disso, para cada requisito, ao invés de escrevermos o que precisamos fazer, como por exemplo adicionar um campo de busca, escrevemos como aquilo ajudará o usuário, como por exemplo o usuário precisa pesquisar termos para encontrar as funcionalidades do software de maneira mais rápida.
'''

texto_02 = '''
O Go (ou golang) é uma linguagem criada em 2007 pela equipe de desenvolvimento do Google. Tinha como objetivo facilitar o desenvolvimento de sistemas sem a necessidade de se utilizar outras linguagens de programação.

Vamos ver neste artigo suas principais estruturas de controle, bem como a criação de funções.

Normalmente, o primeiro exercício em uma linguagem desconhecida da gente é o "olá mundo". Apenas escrevemos código na nova linguagem que exibe essa mensagem.

Embora não pareça nada demais, é um indicativo de que o seu ambiente foi corretamente construído, para que você possa realmente aprender a nova ferramenta.

No caso do Go, é um pouco simples que outras linguagens, como Java por exemplo:
Para rodarmos esse programa por linha de comando, não precisamos compilá-lo antes. Basta que salvemos esse código num arquivo .go (olamundo.go, por exemplo):
Repare que declaramos uma variável, mas esta não é usada em nenhuma parte do sistema, o que faz com que o interpretador go lance um erro de compilação. Esse recurso é bem interessante, pois disciplina o programador a manter somente o código que ele precisa. O time de criação da linguagem justifica a inclusão dessa característica no FAQ da linguagem. Basicamente:

The presence of an unused variable may indicate a bug, while unused imports just slow down compilation, an effect that can become substantial as a program accumulates code and programmers over time. For these reasons, Go refuses to compile programs with unused variables or imports, trading short-term convenience for long-term build speed and program clarity.

Logo, verificamos que eles se preocuparam não somente com variáveis que não são usadas, mas também com imports desnecessários, que podem fazer com que o processo de compilação fique mais lento. A explicação completa pode ser vista em https://golang.org/doc/faq#unused_variables_and_imports
'''

aparicoes = Counter(texto_01.lower())
total_caracteres = sum(aparicoes.values())
print(aparicoes)
print(total_caracteres)

#media = [f'{letra} => {frequencia / total_caracteres}' for letra, frequencia in aparicoes.items()]

#print(proporcoes)
#for letra, contador in aparicoes.items():
 #   print(f'{letra} => {contador}')

proporcoes = [(letra, (frequencia / total_caracteres) * 100) for letra, frequencia in aparicoes.items()]
proporcoes = Counter(dict(proporcoes))

for caracter, proporcao in proporcoes.most_common(10):
    print(f'{caracter} => {proporcao}')

print()
print('   >>> ############################# <<<   ')
print()
def analisa_frequencia_de_letras(texto):
    aparicoes = Counter(texto.lower())
    total_caracteres = sum(aparicoes.values())

    proporcoes = [(letra, (frequencia / total_caracteres) * 100) for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    for caractere, proporcao in proporcoes.most_common(10):
        print(f'{caractere} --> {proporcao:.4f}%')

analisa_frequencia_de_letras(texto_02)

print()
print('   >>> ############################# <<<   ')
print()

analisa_frequencia_de_letras(texto_01)
