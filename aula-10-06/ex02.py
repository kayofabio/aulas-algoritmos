# Nível 2 – Aplicações Práticas
# 6. Busca de Nome em Lista
#   o Peça ao usuário para digitar nomes e depois procure um nome específico usando
# busca linear.
# 7. Busca Binária Recursiva
#   o Implemente a versão recursiva da busca binária em uma lista ordenada.
# 8. Comparar Tempo de Execução
#   o Compare o tempo de execução da busca linear e busca binária em uma lista
# com 1 milhão de elementos. Use o módulo time.
# 9. Encontrar Primeira Ocorrência (Busca Binária Modificada)
#   o Dada uma lista ordenada com elementos repetidos, use busca binária modificada
# para encontrar o índice da primeira ocorrência de um número.
# 10. Localizar Intervalo de Índices
#   • Encontre o intervalo (início e fim) de um número que aparece mais de uma vez usando
# busca binária (ex: [1,2,2,2,3,4] > número 2 > índices 1 a 3).

import random, time

def busca_linear(lista, alvo):
    for indice, elemento in enumerate(lista):
        if elemento == alvo:
            return indice
    return -1

def busca_binaria(lista, alvo, pos_inicial=0, pos_final=None):
    if pos_final == None:
        pos_final = len(lista) -1
    if pos_inicial > pos_final:
        return -1

    pos_meio = (pos_inicial+pos_final) // 2

    if lista[pos_meio] == alvo:
        return pos_meio
    if lista[pos_meio] > alvo:
        pos_final = pos_meio - 1
    if lista[pos_meio] < alvo:
        pos_inicial = pos_meio + 1
    return busca_binaria(lista, alvo, pos_inicial, pos_final)
    
def busca_binaria_primeira_ocorrencia(lista, alvo):
    pos_inicial = 0
    pos_final = len(lista) - 1
    resultado = -1

    while pos_inicial <= pos_final:
        pos_meio = (pos_inicial+pos_final) // 2

        if lista[pos_meio] == alvo:
            resultado = pos_meio
            pos_final = pos_meio - 1
        if lista[pos_meio] > alvo:
            pos_final = pos_meio - 1
        if lista[pos_meio] < alvo:
            pos_inicial = pos_meio + 1
    return resultado

def busca_binaria_ultima_ocorrencia(lista, alvo):
    pos_inicial = 0
    pos_final = len(lista) - 1
    resultado = -1

    while pos_inicial <= pos_final:
        pos_meio = (pos_inicial+pos_final) // 2

        if lista[pos_meio] == alvo:
            resultado = pos_meio
            pos_inicial = pos_meio + 1
        if lista[pos_meio] > alvo:
            pos_final = pos_meio - 1
        if lista[pos_meio] < alvo:
            pos_inicial = pos_meio + 1
    return resultado

print("Adicionar nomes:")
nomes = []

while True:
    nome = input("Digite um nome para adiciona a lista: ")
    nomes.append(nome)
    continuar = input("Adionar mais nomes? [s/n] ").strip().lower()
    while continuar not in ["s", "si", "sim", "nao", "não", "na", "n"]:
        print("Respota inválida")
        continuar = input("Adionar mais nomes? [s/n] ").strip().lower()
    if continuar in ["s", "si", "sim"]:
        continue
    else:
        break

print("="*100)
print("Busca linear\n")
alvo = input("Digite um nome para buscar: ")
res_linear = busca_linear(nomes, alvo)
if res_linear > 0:
    print(f"{alvo} está presente na lista!")
    print(f"Índice onde o nome se encontra: {res_linear}\n")
else:
    print(f"{alvo} não se encontra na lista!\n")

lista = [random.randint(0, 100) for i in range(1000000)]
lista.sort()
alvo = 10

print("="*100)
print("Busca linear x binária\n")

t_inicio = time.time()
res_linear = busca_linear(lista, alvo)
t_fim = time.time()
t_linear = t_fim - t_inicio

if res_linear > 0:
    print(f"{alvo} está presente na lista!")
    print(f"Índice onde o nome se encontra: {res_linear}\n")
else:
    print(f"{alvo} não se encontra na lista!\n")

t_inicio = time.time()
res_binaria = busca_binaria(lista, alvo)
t_fim = time.time()
t_binaria = t_fim - t_inicio

print(f"Tempo de busca linear: {t_linear:.6f} segundos")
print(f"Tempo de busca binária: {t_binaria:.6f} segundos\n")

print("="*100)
print("Primeira ocorrência e intervalo\n")

lista = [1,2,2,2,3,4]
alvo = 2

primeira = busca_binaria_primeira_ocorrencia(lista, alvo)
ultima = busca_binaria_ultima_ocorrencia(lista, alvo)

print(f"lista: {lista}, alvo: {alvo}")
if primeira > 0:
    print(f"Primeira ocorrência: índice {primeira}")
    print(f"Intervalo: índices {primeira} a {ultima}")
else:
    print("número não encontrado!")