# Números Pares

# Escreva um programa em que usuário informe 5 números inteiros
# O programa deve garantir que os valores informados são maiores que zero
# O programa faz leitura dos números
# O programa faz leitura dos números
# O progrma imprime apenas os números pares, infomando sua posição
# Deve usar listas

lista = list(range(0,5))

invalido = False

for x in range(0, 5):
    print("Informe o número da posição ", x + 1)
    lista[x] = int(input())
    while invalido == True:
        if lista[x] <=0:
            print("Valor inválido, tente novamente!")
            lista[x] = int(input())
        else:
            invalido = False


for x in range(0, 5):
    if lista[x] % 2 == 0:
        print("Número na posição ", x + 1, " é igual a ", lista[x], " e é par.")
        