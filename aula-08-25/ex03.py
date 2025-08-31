# Estudo de Caso 3 – Analisando números pares e ímpares
# Enunciado:
# Escreva um programa que:
# 1. Receba 10 números inteiros digitados pelo usuário.
# 2. Separe-os em duas listas: pares e ímpares.
# 3. Exiba quantos números pares e ímpares foram digitados.

def numerosImpares(lista):
    impares = []
    for i in lista:
        if i % 2 == 1:
            impares.append(i)
    return impares

def numeroPares(lista):
    pares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
    return pares

numeros = []
for i in range(1, 11):
    numero = int(input(f"digite o {i}º número: "))
    numeros.append(numero)

pares = numeroPares(numeros)
impares = numerosImpares(numeros)

print(f"pares: {pares}")
print(f"impares: {impares}")
print(f"número de pares digitados: {len(pares)}")
print(f"número de impares digitados: {len(impares)}")