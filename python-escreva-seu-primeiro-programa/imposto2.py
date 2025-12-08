imposto = float(input("Imposto: "))
if imposto < 1002:
    print("Baixo")
elif imposto >= 1002. and imposto <= 2027.:
    print("Medio")
elif imposto >= 2027. and imposto < 10000:
    print("Alto")
else:
    print("Imposto invalido")