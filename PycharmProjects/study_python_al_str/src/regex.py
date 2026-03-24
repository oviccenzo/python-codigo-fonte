import re

email1 = 'Meu numero é 1234-4321'
email2 = 'Fale comigo em 1234-4321 esse é o meu telefone'
email3 = '1234-4321 é o meu celular'
email4 = 'lalalala 0980-08978 asdas 1345-6443 ijlkjdasldkjas 99999-3455 dasdasdas asdasd 98789-1231  kjaslkd 34234323'

padrao = '[0-9]{4,5}-?[0-9]{4}'

#retorno = re.search(padrao, email1)
retorno = re.findall(padrao, email4)

#print(retorno.group())
print(retorno)