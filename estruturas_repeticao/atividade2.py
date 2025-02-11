# Atividade 2: Soma

# Crie um programa que faça a leitura de 5 números inteiros
# O programa deve imprimir a soma dos números

soma = 0
for x in range(0,5):
    soma = soma + int(input("Informe o " + str(x+1) + "° número: "))