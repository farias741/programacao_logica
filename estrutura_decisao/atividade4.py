# Ativdade 4: Habilitação para Vaga

# O programa deve perguntar a idade de um candidato a vaga
# O programa ainda deve perguntar escolaridade, imprimindo as
# seguintes opções:
    # 1 - ensino fundamental
    # 2 - ensino médio
    # 3 - ensino superior
# O candidato é habilitado a concorrer a vaga se:
    # Tem ensino superior completo ou
    # Tem ensino médio e mais de 60 anos
# Imprimir mensagem informando se o candidato está habilitado ou não

idade = int(input("Informe a idade do candidato: "))
print("Informe a escolaridade: ")
print("1 - Ensino Fundamental")
print("2 - Ensino Médio")
print("3 - Ensino Superior")
escolaridade = float(input())
if (escolaridade == 3) or (escolaridade == 2 and idade > 60):
    print("Habilitado!")
else:
    print("Não Habilitado!")