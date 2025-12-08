from pip._vendor.distlib.compat import raw_input


def gera_nome_convite(nome_convidado):
    #convite = 'Flavio Henrique Almeida'
    pos_inicial = len(nome_convidado) - 4
    pos_final = len(nome_convidado)
    parte1 = nome_convidado[0:4]
    parte2 = nome_convidado[pos_inicial:pos_final]
    return "%s.%s" % (parte1, parte2)
    #print(parte1+parte2)
    #print("Robert")
    #print "%s %s" % (parte1, parte2)

def envia_convite(nome_convidado):
    print( "Enviando convite para %s" % (nome_convidado))

def processa_convite(nome_convidado):
    nome_formatado = gera_nome_convite(nome_convidado)
    envia_convite(nome_formatado)

def cadastrar_nomes(nomes):
    print ('Digite o nome:')
    nome = raw_input()
    nomes.append(nome)

def remover(nomes):
    print( 'Qual nome voce gostaria de remover?')
    print( nomes)
    nome = raw_input()
    nomes.remove(nome)
    print (nomes)