# Ativadade 5: Testes

# O programa deve ler dois valores inteiros
# Imprimir:
    # "Sãos iguais", se forem iguais
    # "São diferentes", se forem diferentes
    # "Primeiro é maior", se o primeiro for maior
    # "Segundo é maior" se o segundo for maior

primeirovalor = int(input("Informe o primeiro valor: "))
segundovalor = int(input("Informe o segundo valor: "))
if primeirovalor == segundovalor:
    print("São iguais")
else:
    print("São diferentes")

if primeirovalor > segundovalor:
    print("Primeiro é maior")
elif primeirovalor < segundovalor:
    print("Segundo é maior")