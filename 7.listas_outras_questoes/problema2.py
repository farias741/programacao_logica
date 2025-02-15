# Maior e Menor

# Escreva um programa que leia 10 números
# Imprima o maior e o menor número
# Deve usar listas

lista = list(range(1,11))

for x in range(0,10):
    print("Informe o número da posição: ", x+1)
    lista[x] = int(input())

lista2 = sorted(lista)
print("O maior valor é : ", lista2[9])
print("O menor valor é: ", lista2[0])

# outra forma
print("O maior valor é : ", max(lista))
print("O menor valor é: ", min(lista))