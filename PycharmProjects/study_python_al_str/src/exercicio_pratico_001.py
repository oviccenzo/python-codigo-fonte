texto = 'Izuku Midoriya'
texto[0:10]

texto2 = texto[:4]
print( texto2)
print(texto)


celular = "(41) 96574-1728"

x = celular.find('(') + 1
y = celular.find(')')

indiceInicialCodigoArea = x
indiceFinalCodigoArea = y

print(celular[indiceInicialCodigoArea:indiceFinalCodigoArea])