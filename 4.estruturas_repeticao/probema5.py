# Calculador de Média

# O programa deve calcular a média dos números informados 
# pelo usuário
# Primeiramente o programa pergunta quantos números o usuário vai entrar
# Em seguida ele pede para o usuário entrar cadaum dos números
# Por fim, o programa imprime a média dos números

tab = int(input("Quantos números serão calculados? "))
soma = 0
for tab in range(1, tab+1):
    soma = soma + int(input("Informe o " + str(tab) + "° número: "))

print("A média é igual a: ", soma / tab)
