# Problema 1 – Restaurante Inteligente
# Um restaurante armazena os pedidos do dia em uma lista de dicionários, onde cada pedido tem:
# cliente, itens (lista de dicionários com prato e preco).
# Tarefas:
# 1. Crie uma função que receba o nome de um cliente e retorne o valor total gasto (somando
# todos os itens pedidos).
# 2. Crie uma função que descubra qual prato foi o mais vendido no dia.
# 3. Mostre um ranking com os 3 clientes que mais gastaram, em ordem decrescente.

from collections import Counter

def valorTotal(pedidos, nomeCliente):
    resultado = 0
    for pedido in pedidos:
        if pedido["cliente"].lower() == nomeCliente.lower():
            for pratos in pedido["itens"]:
                resultado += pratos["preco"]
            return resultado
    return None

def pratoMaisVendido(pedidos):
    pratosTotal = []
    for pedido in pedidos:
        for item in pedido["itens"]:
            pratosTotal.append(item["prato"])
    return Counter(pratosTotal).most_common(1)

def rankingClientes(pedidos):
    ranking = {}
    for pedido in pedidos:
        ranking.update({pedido["cliente"]: valorTotal(pedidos, pedido["cliente"])})
    ranking = sorted(ranking.items(), key=lambda x: x[1], reverse=True)
    return ranking[0:3]

pedidos = [
    {
        "cliente": "Ana",
        "itens": [
            {"prato": "Lasanha", "preco": 30},
            {"prato": "Suco de Laranja", "preco": 8}
        ],
    },
    {
        "cliente": "Bruno",
        "itens": [
            {"prato": "Pizza", "preco": 40},
            {"prato": "Refrigerante", "preco": 6},
            {"prato": "Sobremesa", "preco": 12}
        ],
    },
    {
        "cliente": "Carla",
        "itens": [
            {"prato": "Pizza", "preco": 40},
            {"prato": "Suco de Laranja", "preco": 8}
        ],
    }
]

nomeCliente = input("Digite nome de um cliente para saber total gasto: ")
total = valorTotal(pedidos ,nomeCliente)
maisVendido = pratoMaisVendido(pedidos)
ranking = rankingClientes(pedidos)
if total:
    print(f"{nomeCliente} gastou R$ {total:.2f}\n")
else:
    print("cliente não encontrado\n")
print(f"Prato mais vendido: {maisVendido[0][0]} - quantidade: {maisVendido[0][1]}\n")

print("TOP três clientes:")
for i, (cliente, total) in enumerate(ranking, start=1):
    print(f"{i}º {cliente}: R$ {total}")