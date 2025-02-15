# Impressão

# Escreva um programa em que usuário informe a quantidade de números
# que irá entrar
# O programa deve garantir que quantidade seja igual ou maior que dois
# O programa deve imprimir
    # A soma do primeiro e do último número
    # O produto do primeiro e segundo número informado
# Deve usar listas

qnt  = int(input("Informe a quantidade de números: "))

while qnt < 2:
    print("Quantidade inválida, tente novamente")
    qnt = int(input())

lista = list(range(0, qnt))

for x in range(0, qnt):
    print("Informe o número da posição ", x + 1)
    lista[x] = int(input())
 
print(lista)

soma  = lista[0] +  lista[ len(lista)-1] 
print("Soma do primeiro e do último número", lista[0] +  lista[ len(lista)-1]   )
print("Produto do primeiro e segundo número",  lista[0]  *  lista[1]    )