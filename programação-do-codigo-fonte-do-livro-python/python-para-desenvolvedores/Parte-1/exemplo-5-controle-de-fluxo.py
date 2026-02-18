# if <condicoes>:
#   <bloco de codigo>
# elif <condicoes>
#   <bloco de codigo>
# elif <condicoes>:
#   <bloco de codigo>
# else:
#   <bloco de codigo>

tempo = int(input("Entre com uma temperatura: "))

if tempo < 0:
    print('congelado')
elif 0 <= tempo <= 20:
    print('Frio')
elif 21 <= tempo <= 25:
    print('Normal')
elif 26 <= tempo <= 30:
    print('Quente')
else:
    print('Muito quente')