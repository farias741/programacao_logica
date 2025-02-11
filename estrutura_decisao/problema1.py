# Entrar na faculdade

# O sistema deve ler alguns dados de um candidato para entrar em uma faculdade
    # Idade - inteiro
    # Nota no Enem - real
    # Brasileiro - lógico
# Se todas as condições lógicas abaixo forem atingidas,
# o candidato deve ser aprovado:
    # Menos que 25 anos
    # Nota mínima no Enem de 70 pontos
    # Ser brasileiro
# O sistema deve emitir uma mensagem informando se ele foi ou não aprovado

idade = int(input("Informe a Idade: "))
nota = float(input("Informe a nota do Enem: "))
brasileiro = input("Digite \"S\" se é brasileiro ou \"N\" caso não seja: ")
brasileiro = brasileiro.upper()

if idade<25 and nota>=70 and brasileiro=="S":
    print("Aprovado!")
else:
    print("Reprovado!")