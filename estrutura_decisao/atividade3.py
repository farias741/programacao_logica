# Atividade 3: Soma dos Maiores

# Faça a leitura de 2 valores inteiros
# Imprima os valores em ordem crescente

primeiro = int(input("Informe o primeiro valor: "))
segundo = int(input("Informe o segundo valor: "))
if primeiro < segundo:
    print(primeiro, " ", segundo)
else:
    print(segundo, " ", primeiro)