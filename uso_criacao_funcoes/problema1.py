# Calculador de Média

# O progrma deve calcular a média de dois números informados pelo usuário
# Os números devem ser informados como parâmetro da função
# A função deve retornar o cálculo
# O programa que chamar a função e deve inprimir o resultado

def media(x,y):
    return (x+ y) / 2

valor1 = int(input("Informeo primeiro valor: "))
valor2 = int(input("Informeo segundo valor: "))
resultado = media(valor1, valor2)
print("O calculo da média é: ", resultado)