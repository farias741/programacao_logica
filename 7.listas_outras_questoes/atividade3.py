# Inversão

# O programa deve solicitar uma lista com 5 números reais
# Para cada número, deve informar:
    # A raiz quadrada
    # Se a raiz quadrada do número é um valor inteiro ou real (com casas decimais)
# Deve usar listas

from math import sqrt

lista = list(range(0,5))

for x in range(0,5):
    print("Informe o número da posição ", x + 1, " da primeira lista")
    lista[x] = float(input())

for x in range(0, 5):
    print("Raiz quadrada: ", sqrt(lista[x]))
    if sqrt(lista[x]) % 1 == 0 :
        print("Raiz quadrada é um valor inteiro")
    else:
        print("Raiz quadrada não é um valor inteiro")