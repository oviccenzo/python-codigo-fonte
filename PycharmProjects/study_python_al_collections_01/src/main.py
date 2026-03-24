idades = [39, 30, 27, 18]

print(len(idades))

print(idades[2])

idades.append(17)

print(idades)

idades.remove(30)
print(idades)

#idades.clear()
#print(idades)

print(15 in idades)
print(17 in idades)

idades.insert(1, 21)

print(idades)

idades_ano_que_vem = [(idade + 1) for idade in idades]
print(idades_ano_que_vem)

idades_maior_que_21 = [(idade) for idade in idades if idade > 21]
print(idades_maior_que_21)