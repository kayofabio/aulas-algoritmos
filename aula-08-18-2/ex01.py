# 1. Cálculo de Complexidade Simples
# Escreva um algoritmo que conte quantas operações básicas (somas) são executadas para
# calcular a soma dos números de 1 até n. Exiba o resultado e compare com a fórmula matemática
# n*(n+1)/2.

import math

def soma(n):
    resultado = n*(n+1)/2
    return resultado

def somaSemForm(n):
    resultado = 0
    for i in range(1, n+1):
        resultado += i
    return resultado

def qtdSomas(n):
    return n-1


num = int(input("Digite um núemero: "))
result = somaSemForm(num)
result2 = soma(num)
print(f"Soma de 1 a {num} é igual a:\nsem fórmula {result}\ncom fórmula {result2}\nQuantidade de somas feitas: {qtdSomas(num)}")