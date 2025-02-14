# Conversor de Temperatura

# O Programa deve converter graus célsius para fahrenheit e vice versa
# através de uma função
# Os números e o tipo de conversão devem ser informados como parâmetro da função
# A função deve retornar o resultado
# O programa deve chamar a função e imprimir o resultado

def converte(tipo,tempo):
    if tipo == 1:
        tempo = (tempo * 9/5) + 32
    else:
        tempo = ((tempo - 32)* 5) /9
    return tempo

tp = int(input("Informe o tipo de conversão 1 para Celsius para Fahrenheit e 2 para Fahrenheit para Celsius : "))
temperatura = int(input("Informe a temperatura para converter: "))

print("O resultado é: ", converte(tp,temperatura ))