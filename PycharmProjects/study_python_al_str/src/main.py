'''
url = 'https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=1500'

indice = url.find('?')
print(url[indice + 1:])
'''


from src.extratorArgumentosUrl import ExtratorArgumentosUrl

url = 'https://www.bytebank.com.br/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=1500'
url2 = 'https://www.bytebank.com.br/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=1000'

argumentos_url = ExtratorArgumentosUrl(url)
# argumentos_url2 = ExtratorArgumentosUrl(url2)
'''
'''
moeda_origem, moeda_destino = argumentos_url.extrai_argumentos()
valor_origem = argumentos_url.extrai_valor()

print(moeda_origem, moeda_destino, valor_origem)

#print(len(argumentos_url))
print(argumentos_url)

#ExtratorArgumentosUrl.extraiArgumentos()


