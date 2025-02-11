# Impressão de Intervalo

# Crie um programa que solicite a entrada de dois números inteiros
# O programa deve garantir que os números sejam positivos,
# e que o segundo número deve ser maior que o primeiro
# O programa deveimprimir o intervalo dos números informados:
    # Primeiramente em ordem crescente
    # Em seguida, em ordem decrescente

valido = False
while valido == False:
    int1 = int(input("Informe o primeiro valor: "))
    int2 = int(input("Informe o segundo valor: "))
    if int1 > 0 and int2 >0 and int1 < int2:
        valido = True

for x in range(int1, int2+1): # coloca int2+1  pois é na forma crescente
    print(x)

for int2 in range(int2, int1-1, -1):
    print(int2)
