# Estudo de Caso 2 – Lista de compras interativa
# Enunciado:
# Faça um programa que:
# 1. Permita ao usuário adicionar itens a uma lista de compras.
# 2. Caso o usuário digite "sair", o programa encerra.
# 3. Mostre a lista final de compras organizada em ordem alfabética.

lista = []
while True:
    item = input("adicione um item a lista(digite sair para parar): ")
    if item.lower() == "sair":
        break
    lista.append(item)

lista.sort()
for item in lista:
    print(item)