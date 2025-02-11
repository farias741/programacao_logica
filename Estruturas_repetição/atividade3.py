# Atividade 3: Impressão de Tabuada

# O programa deve imprimir as tabuadas do 1 ao 10
# Cada tabuada deve ser emoldurada


tabuada = 1
while tabuada < 11:
    print("-----------------------")
    for x in range(1,11):
        resp =  "|" +  str(x) +  " x " + str(tabuada) + " = " + str( x * tabuada )
        esp = "  " * (14 - len(resp)) + "|"
        print(resp + esp)
        if x == 10:
            tabuada = tabuada + 1
            break
    print("----------------------")
