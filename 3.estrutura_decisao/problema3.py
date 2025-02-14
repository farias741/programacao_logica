# Habilitação para Vaga

# Para se habilitar a uma vaga de trabalho, o candidato deve cumprir PELO MENOS
# um dos requisitos abaixo:
    # Ter menos de 70 anos de idade
    # Ter pelo menos de 25 anos de atividade profissional
    # Ter mais de 70 anos e pelo menos 30 anos de atividade profissional
# O programa deve ler estas infomações(todas do tipo inteiro) e imprimir se o candidato
# está ou não habilitado a vaga de trabalho


idade = int(input("Informe a idade: "))
atividade = float(input("Informe o tempo de atividade profissional:"))
if (idade < 70) or (atividade >= 25) or (idade >= 70 and atividade >=30):
    print("Habilitado!")
else:
    print("Não Habilitado!")