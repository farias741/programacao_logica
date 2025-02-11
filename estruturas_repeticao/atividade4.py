# Atividade 4: Validação de Valores

# O programa deve solicitar a entrada de dois valores inteiros
# Deve garantir que o primeiro valor é maior que 10, e o segundo valor é pelo
# 10 vezes maior que o primeiro valor
# O programa deve imprimir o produto do primeiro valor pelo segundo valor

valido = False
while valido == False:
    valor1 = int(input("Informe o primeiro valor: "))
    valor2 = int(input("Informe o segundo valor: "))
    if valor1 > 10 and valor2 > 10*valor1:
        valido = True
    else:
        print("Valores inválidos!")

print("Produto: ", valor1 * valor2)