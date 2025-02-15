# Busca de Nomes

# O programa deve ter um lista com 10 nomes armazenados
# Deve em seguida, pedir ao usuário pra entrar um nome
# O programa deve informar se o  nome foi ou não encontrado
# O programa não deve fazer distinção entre letras maíusculas e minúsculas


lista_nomes = ["Hadassah", "Débora", "Antonio", "Dinalva", "Sara",
                "Noah", "Nicolas", "Bruna", "Aline", "Sabrina"]
print("Informe um nome para localização: ")
nome = input().strip().lower()

#encontrado = False

for x in range(0, len(lista_nomes)):
    print(f'[ {x}º ] : {lista_nomes[x]}')
    if nome == lista_nomes[x].lower():
        print(f'\nO nome {nome} foi encontrado na posição {x}º da lista')
        break
else: 
     print("Nome não encontrado")