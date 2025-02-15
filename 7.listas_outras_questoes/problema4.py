# Comparando Vetores

# Escreva um programa que leia dois vetores de 5 números inteiros
# O programa deve imprimir:
    # Os números cujas posições nos vetores coincidem, e em que posição se encontram
    # Os demais números, que estão na mesma posição mas cujos valores não coincidem,
    # com o valor de cada vetor e a posição
# Deve usar listas

lista1 = list(range(1,6))
lista2 = list(range(1,6))

for x in range(0,5):
    print("Informe o número da posição ", x + 1, " da primeira lista")
    lista1[x] = int(input())

for x in range(0,5):
    print("Informe o número da posição ", x + 1, " da segunda lista")
    lista2[x] = int(input())

for x in range(0,5):
    if lista1[x] == lista2[x]:
        print("Coincidência do valor ", lista1[x], "posição ", x + 1)
    else:
        print("Valores ", lista1[x], " e ", lista2[x], "diferentes na posição ", x + 1)