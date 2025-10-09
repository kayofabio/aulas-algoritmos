# Nível 3 – Desafios
# 11. Busca em Lista de Dicionários
#   • Dada uma lista de dicionários representando pessoas ({"nome": "Ana", "idade":25}), 
#   implemente uma busca linear para encontrar a pessoa com nome "João".
# 12. Jogo: Adivinhe o Número (Busca Binária)
#   • O computador escolhe um número entre 1 e 100. O jogador tenta adivinhar, e o
#   computador responde se é maior ou menor. Use lógica de busca binária para resolver
#   com o menor número de tentativas.
# 13. Buscar Produtos por Preço
#   • Dada uma lista de produtos com preços, implemente uma busca para encontrar todos os
#   produtos com um determinado preço.
# 14. Implementar sua própria função index()
#   • Crie uma função meu_index(lista, valor) que funcione como o método
#   list.index(), usando busca sequencial.

import random

def busca_linear_pessoa(lista, alvo):
    for indice, elemento in enumerate(lista):
        if elemento["nome"].lower() == alvo.lower():
            return indice
    return -1

def busca_linear_produto(lista, alvo):
    resultados = []
    for indice, elemento in enumerate(lista):
        if elemento["preco"] == alvo:
            resultados.append(indice)
    return resultados

def meu_index(lista, valor):
    for indice, elemento in enumerate(lista):
        if elemento == valor:
            return indice
    return -1

print("Busca de dicionários\n")
pessoas = [
    {"nome": "Ana", "idade":25},
    {"nome": "João", "idade":26},
]

alvo = "joão"

res_linear = busca_linear_pessoa(pessoas, alvo)
print(f"lista: {pessoas}, alvo: {alvo}")
print(f"índice: {res_linear}\n")

print("="*100)
print("Jogo de adivinha\n")
print("Adivinhe o número de 1 a 100")
numero = random.randint(1, 100)
n_tentativas = 0
while True:
    tentativa = int(input("tentativa: "))
    n_tentativas += 1
    if tentativa == numero:
        print(f"{numero} é o número certo!\nNúmero de tentativas: {n_tentativas}")
        break
    if tentativa > numero:
        print("O número é MENOR")
    if tentativa < numero:
        print("O número é MAIOR")

print("="*100)
print("Busca de produtos\n")

produtos = [
    {"nome": "mouse", "preco": 30},
    {"nome": "monitor", "preco": 150},
    {"nome": "pendrive", "preco": 30},
    {"nome": "teclado", "preco": 80},
]
alvo = 30

print(f"lista: {produtos}")
print(f"alvos com preço: R$ {alvo}")

res_linear = busca_linear_produto(produtos, alvo)
print(f"indice dos alvos: ")
for i in res_linear:
    print(i)

print("="*100)
print("Busca de index\n")

lista = ["prato", "colher", "faca", "panela"]
valor = "faca"
print(f"lista: {lista}, valor: {valor}")
index = meu_index(lista, valor)
print("indice: ", index)