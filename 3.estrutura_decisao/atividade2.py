# Atividade 2: Alistamento

# O programa deve ler o ano de nascimento de uma pessoa
# O sistema deve imprimir informando se ela está na idade de se alistar ou não
# (considerando que se tiver mais de 18 anos, deva se alistar)


from datetime import date
dn = float(input("Informe o ano de nascimento "))
anoatual = float(date.today().year)
if anoatual - dn > 18:
    print("Deve se alistar!")
else:
    print("Não deve se alistar!")