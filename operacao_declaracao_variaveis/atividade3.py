# Reajuste

# O programa deve ler o salário de um funcionário (float)
# O programa deve ler um percentual de reajuste (float)
# O sistema deve imprimir o salário reajustado


salario =  float(input("Informe o salário: "))
reajuste =  float(input("Informe o percentual de reajuste (%): "))
novosalario = salario + salario * (reajuste / 100)
print("O salário reajustado é igual a  ", novosalario)