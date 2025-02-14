# Descontos

# O programa deve ler a quantidade de produtos comprados(int) e o valor
# total(float)
# Deverá imprimir
    # O valor total da compra - sem desconto
    # O valor total da compra - com desconto
    # O valor da economia

# Quantidade | Desconto
# 2 | 2%
# >2 e <=5 | 5%
# >5 e <10 |10%
# >=10 |15%

quantidade = int(input("Informe a quantidade de produtos: "))
total = float(input("Informe o valor total da compra: "))
desconto = 0
if quantidade == 2:
    desconto = 0.02
elif quantidade > 2 and quantidade <= 5:
    desconto = 0.05
elif quantidade > 5 and quantidade < 10:
    desconto = 0.1
elif quantidade >= 10:
    desconto = 0.15

calcdesc = total - (total * desconto)

print("Valor Total da Compra: ", total)
print("Valor Total com Desconto: ", calcdesc)
print("Economia: ", total - calcdesc)