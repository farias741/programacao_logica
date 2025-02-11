# Atividade 5: Pares

# O programa deve solicitar a entrada de 5 valores inteiros
# O programa deve imprimir
    # A quantidade dos valores pares
    # A soma dos valores pares
    # O produtos dos valores pares

quantidade = 0
soma = 0
produto = 0

for x in range(0,5):
    print("Informe o " + str(x+1) + "º número: " )
    numero = int(input())
    if numero %  2 == 0:
        quantidade = quantidade + 1
        soma = soma + numero
        produto = produto * numero

print("Quantidade de valores pares: ", quantidade)
print("Soma de valores pares: ", soma)
print("Produto de valores pares: ", produto)