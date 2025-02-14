# Impressão de Tabuada

# O usuário deve informar qual tabuada deve ser impressa
# O programa deve imprimir a tabuada na tela

tabuada = int(input("Informe a tabuada que quer imprimir: "))
for n in range(1,11):
    print(n, " X ", tabuada, " = ", n * tabuada)