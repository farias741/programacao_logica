# Maior Valor e Posição

# Escreva um programa que leia 5 nomes
# Independente da forma como foram digitados, o programa deve imprimir os 5 nomes:
    # Com a primeira letra em maiúsculas 
    # Com as demais letras em minúsculas
# Deve usar listas

lista = list(range(0,5))

for x in range(0, 5):
    print("Informe o número da posição ", x+1)
    lista[x] = input()

for x in range(0, 5):
    nometmp = lista[x][0].upper() + lista[x][ 1 : len(lista[x])   ].lower()
    print("Nome na posição ", x+1, lista[x])