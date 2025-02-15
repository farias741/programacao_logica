# Calculadora de Média

# Escreva um programa que leia 10 números inteiros
# Os números devem ser maiores que zero, caso contrário a entrada
# é rejeitada e deve ser repetida
# Imprima a média destes números
# Deve usar listas

from statistics import mean # importando a função mean

lista = list(range(1,11))

for x in range(0,10):
    print("Informeo número na posição: ", x+1)
    lista[x] = int(input())
    while lista[x] <= 0:
        print("Entrada inválida, por favor repita!")
        lista[x] = int(input())

soma = 0
for x in range(0,10):
    soma += lista[x]

print("Média calculada \"manualmente\" igual a: ", soma / 10)
print("Média calculada \"por função\" igual a: ", mean(lista))
