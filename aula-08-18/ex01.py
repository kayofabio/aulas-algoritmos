# 1. Faça um programa que leia dois números e mostre qual é o maior.

def maxNumber(n1, n2):
    if n1 > n2:
        return n1
    elif n2 > n1:
        return n2
    else:
        return None
    
n1 = int(input("digite um número: "))
n2 = int(input("digite outro número: "))

resultado = max(n1, n2)
if resultado == None:
    print("São iguais")
else:
    print(f"Maior número: {resultado}")