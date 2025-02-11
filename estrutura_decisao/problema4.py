# Exame

# Faça a leitura da nota do aluno
# Se a nota for maior ou igual a 7, imprima aprovado
# Se a nota for menor que 7, faça a leitura da nota do exame
# Se a nota do aluno mais a nota do exame, divididos por 2, forem menor que 6, imprima
# reprovado, caso contrário imprima aprovado.

nota = float(input("Informe a nota do aluno: "))
if nota >= 7:
    print("Aprovado!")
else:
    exame = float(input("Informe a nota do exame: "))
    if (nota + exame) / 2 < 6:
        print("Reprovado!")
    else:
        print("Aprovado!")