# 2. Escreva um algoritmo que calcule a tabuada de um número digitado pelo usuário.

def tabuda(num, qtd):
    resultado = []
    for x in range(1, qtd+1):
        resultado.append(num*x)
    return resultado

numero = int(input("Digite um número para ter sua tabuada: "))
limite = int(input("Até onde irá a tabuada? "))

for i, x in enumerate(tabuda(numero, limite), start=1):
    print(f"{numero} X {i} = {x}")