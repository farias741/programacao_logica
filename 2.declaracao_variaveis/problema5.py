# Percentuais

# O programa deve ler a quantidade total de alunos de uma escola
# O programa deve ler a quantidade de alunos do sexo masculino
# O programa deve imprimir o percentual de alunos do sexo masculino e feminino


total =  input("Informe o total de alunos: ")
total = int(total)
masculino =  input("Informe o total de alunos do sexo masculino: ")
masculino = int(masculino)
print("Percentual de alunos do sexo masculino: ",masculino * 100 / total )
print("Percentual de alunos do sexo feminino: ", (total  - masculino) * 100 / total)
