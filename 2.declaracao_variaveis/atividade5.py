# Impostos

# O programa deve ler o valor total da manutenção de um veículo
# O programa deve ler o percentual de impostos de serviços
# O programa deve ler o percentual de impostos de produtos
# O programa deve imprimir o total a ser pago nos dois impostos,
# bem como o valor que sobra depois de descontados os impostos

total =  float(input("Informe o valor total da manutenção: "))
perims =  float(input("Informe o percentual de impostos sobre serviços: "))
perimp =  float(input("Informe o percentual de impostos sobre circulação de produtos: "))

totalperims = total * (perims/100)
totalperimp =total * (perimp /100)

print("O total de ISSQN é de  ", totalperims)
print("O total de ICMS é de  ", totalperimp)
print("O valor restante retirado os impostos é de   ",total -  totalperims - totalperimp) 