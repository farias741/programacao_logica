# Impressão de Tabuada II

# Este programa deve ser igual ao anterior, porém, após a impressão, o programa
# deve perguntar se o usuário quer imprimir uma nova tabuada
# Se ele informar que sim, o usuário deve informar a nova tabuada,
# que será impressa
# O programa só encerra quando o usuário informar que não quer nova impressão

impressao = True
while impressao == True:
    tabuada = int(input("Informe a tabuada que quer imprimir: "))
    for n in range(1,11):
        print(n, " X ", tabuada, " = ", n * tabuada)
    resp = input("Deseja imprimir uma nova tabuada? Informe S para sim e N para não: ")
    if resp.upper() == "N":
        impressao = False