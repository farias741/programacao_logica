# Conceito Final

# O professor deve entrar uma nota no sistema (float)
# O programa deve imprimir o conceito final de acordo com a nota,
# de acordo com a tabela abaixo:

# >90 conceito A
# >=75 e <=90 conceito B
# >=60 e <75 conceito C
# >=40 e <60 conceito D
# >=20 e <40 conceito E
#<20 conceito F

nota = float(input("Informe a nota do aluno: "))
if nota > 90:
    print("Conceito A")
elif nota >= 75 and nota <= 90:
    print("Conceito B")
elif nota >= 60 and nota < 75:
    print("Conceito C")
elif nota >= 40 and nota < 60:
    print("Conceito D")
elif nota >= 20 and nota < 40:
    print("Conceito E")
else:
    print("Conceito E")