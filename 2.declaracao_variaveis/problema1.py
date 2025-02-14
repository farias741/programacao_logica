# Cotação de moeda

# O programa deve fazer a cotação de compra de moeda estrangeira
# O usuário deve entrar o valor de moeda estrangeira que quer comprar
# O sistema terá internamente uma variável com a cotação do dia 
# O sistema imprime o valor a ser pago em moeda local
# OBS: deve aceitar valores (float)

cotacao = 3.45
valor = input("Infome o valor da moeda estrangeira para compra: ")
valor = float(valor)
conversao = valor * cotacao
print("O valor total em moeda local é: ", conversao)