# Atividade 1: Positivo ou Negativo

# O sistema deve ler um valor inteiro
# Imprimir positivo se o valor for positivo e negativo, se for
# negativo e neutro se for zero.

valor = int(input("Informe um valor: "))
if valor > 0:
    print("Número Positivo")
elif valor < 0:
    print("Número Negativo")
else:
    print("Número Neutro")