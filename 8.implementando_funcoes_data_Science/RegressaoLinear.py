# Problema

# Vai solicitar a quantidade de variáveis
# Vai solicitar a entrada das variáveis dependentes e independentes para criar o modelo
# Vai solicitar o valor que queremos prever/estimar
# Vai executar as funções correlacao, inclinacao, interceptacao, previsao
# Vai mostra o resultado da previsão



from regressao import *

quantidade = int( input("Informe a quantidade de variáveis do modelo: "))
x_ = list(range(0,quantidade))
y_ = list(range(0,quantidade))

print("Informe as ", quantidade, " variaveis dependentes: ")      
for n in range(0, quantidade):
    print("Informe o valor ", n+1)
    y_[n] = int(input())

print("Informe as ", quantidade, " variaveis independentes:" )      
for n in range(0, quantidade):
    print("Informe o valor ", n+1)
    x_[n] = int(input())

print("Informe o valor que quer prever ")
prev = float(input())

cor = correlacao(x_,y_)
incl =  inclinacao(x_,y_,cor)
inter = interceptacao(x_,y_, incl)
result = previsao(inter, incl, prev)

print("Modelo: ")
print("Correlação: ", cor)
print("Inclinação: ", incl)
print("Interceptação: ", inter)
print("Valor para prever: ", prev)
print("Resultado: ", result)
