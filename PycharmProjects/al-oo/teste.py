def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor
    return conta["saldo"]

def saca(conta, valor):
    conta["saldo"] -= valor
    return conta["saldo"]

def extrato(conta):
    print("O valor do saldo é {}".format(conta["saldo"]))