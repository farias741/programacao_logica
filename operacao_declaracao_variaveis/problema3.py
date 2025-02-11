# Inversao de variaveis

# O programa deve fazer a leitura de duas variáveis (string)
# Os valores devem ser registrados nas variáveis var1 e var2
# O sistema deve inverter os valores, colocar em var2 o valor de var1 e vice versa
# O sistema deve imprimiras variáveis invertidas

var1 = input("Informe a primeira variável: ")
var2 = input("Informe a segunda variável: ")
vartemp = var2
var2 = var1
var1 = vartemp
print("As variáveis invertidas são: ", var1, " e ", var2)