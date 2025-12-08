numero = 0
qtdepos = 0
qtdeneg = 0

while(numero != 10):
    numero = int(input("Digite um número (Digite 10 para parar): "))
    if numero > 0:
        qtdepos = qtdepos + 1
    elif numero < 0:
        qtdeneg = qtdeneg + 1

print("A quantidade de numero positivo: ",qtdepos)
print("A quantidade de numero negativo: ",qtdeneg)
