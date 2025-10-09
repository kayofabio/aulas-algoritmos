# Nível 1 – Fundamentos
# 1. Busca Linear Simples
#   o Dado um vetor de números inteiros e um número alvo, use busca sequencial para
#   verificar se o número está presente.
#   o Extra: informe o índice se encontrar.
# 2. Contar Ocorrências (Busca Linear)
#   o Conte quantas vezes um número aparece na lista usando busca sequencial.
# 3. Maior Número (Busca Linear)
#   o Use busca sequencial para encontrar o maior número em uma lista.
# 4. Menor Número (Busca Linear)
#   o Similar ao anterior, mas encontre o menor valor.
# 5. Verificar Elemento (Busca Binária)
#   o Dada uma lista ordenada, implemente a busca binária para verificar se o
#   elemento existe.

import random, time, tracemalloc

def busca_linear(lista, alvo):
    for indice, elemento in enumerate(lista):
        if elemento == alvo:
            return indice
    return -1

def ocorrencia_do_numero(lista, alvo):
    ocorrencia = 0
    for i in lista:
        if i == alvo:
            ocorrencia += 1
    return ocorrencia

def maior_numero(lista):
    maior = lista[0]
    for i in lista:
        if i > maior:
            maior = i
    return maior

def menor_numero(lista):
    menor = lista[0]
    for i in lista:
        if i < menor:
            menor = i
    return menor

def busca_binaria(lista, alvo):
    pos_inicial = 0
    pos_final = len(lista) - 1

    while pos_inicial <= pos_final:
        pos_meio = (pos_inicial+pos_final) // 2

        if lista[pos_meio] == alvo:
            return pos_meio
        if lista[pos_meio] > alvo:
            pos_final = pos_meio - 1
        if lista[pos_meio] < alvo:
            pos_inicial = pos_meio + 1
    return -1

lista = [random.randint(0, 1000) for i in range(1000000)]
numero = 100

res_linear = busca_linear(lista, numero)
ocorrencia = ocorrencia_do_numero(lista, numero)
maior = maior_numero(lista)
menor = menor_numero(lista)

print("Busca linear\n")

if res_linear > 0:
    print(f"Número {numero} está presente na lista!")
    print(f"Primeiro índice onde o número se encontra: {res_linear}")
else:
    print("Número não se encontra na lista!")
print(f"Total de vezes que o número {numero} aparece na lista: {ocorrencia} ocorrências")
print(f"Maior numero que aparece na lista: {maior}")
print(f"Menor número que aparece na lista: {menor}\n")

print("="*100)
print("Busca binária\n")

lista.sort()
res_binaria = busca_binaria(lista, numero)
if res_binaria > 0:
    print(f"Número {numero} está presente na lista!")
    print(f"Primeiro índice onde o número se encontra: {res_binaria}\n")
else:
    print("Número não se encontra na lista!\n")


print("="*100)
print("Comparação\n")

lista = [random.randint(0, 1000000) for i in range(1000000)]
numero = 100

tracemalloc.start()
time_inicio = time.time()
res_linear = busca_linear(lista, numero)
time_fim = time.time()
memoria_atual, memoria_pico = tracemalloc.get_traced_memory()
tracemalloc.stop()

time_execucao = time_fim - time_inicio
print(f"tempo de exucução busca linear: {time_execucao:.6f} segundos")
print(f"Pico de memória: {memoria_pico/1024:.3f} KB\n")

lista.sort()
tracemalloc.start()
time_inicio = time.time()
res_binaria = busca_binaria(lista, numero)
time_fim = time.time()
memoria_atual, memoria_pico = tracemalloc.get_traced_memory()
tracemalloc.stop()

time_execucao = time_fim - time_inicio
print(f"tempo de exucução busca binária: {time_execucao:.6f} segundos")
print(f"Pico de memória: {memoria_pico/1024:.3f} KB")
