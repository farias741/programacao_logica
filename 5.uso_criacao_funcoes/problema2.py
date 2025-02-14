# Impressão de Intervalo

# Crie uma função que solicite a entrada de dois números inteiros
# A função deve imprimir o intevalo dos números informados:
    # Primeiramente em ordem crescente
    # Em seguida, em ordem decrescente

def impressao(int1, int2):
    for x in range(int1, int2 + 1):
        print(x)
    for int2 in range(int2, int1 - 1, -1):
        print(int2)

int1 = int(input("Informe o primeiro valor: "))
int2 = int(input("Informe o segundo valor: "))
impressao(int1, int2)