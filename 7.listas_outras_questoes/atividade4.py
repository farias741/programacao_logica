# Comparando Vetores

# O programa deve ler uma lista com 5 números inteiros
# O programa deve garantir que os números sejam entrados em ordem crecente
# Deve usar listas

lista = list(range(0,5))
anterior = 0
invalido = True

for x in range(0,5):
    print("Informe o número da posição ", x + 1, " da lista")
    lista[x] = int(input())
    while lista[x] <= anterior:
               print("Valor ", lista[x], " inválido, tente novamente")
               lista[x] = int(input())    
    anterior = lista[x]