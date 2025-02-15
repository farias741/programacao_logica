# Módulos

# O programa deve solicitar a entrada de dois números inteiros
# O programa deve garantir que o segundo número seja maior que o primeiro
# O programa deve imprimir o intervalo de números em ordem crescente e decrescente
# A função de impressão deve estar em outro arquivo py, que deve ser importada e executada pelo
# programa principal

from impressao import imprime

valido = False

while valido == False:
    int1 = int(input("Informe o primeiro valor: "))
    int2 = int(input("Informe o segundo valor: "))
    if int2 <= int1:
        print("Valores inválidos! Tente novamente!")
    else:
        valido = True

imprime(int1, int2)