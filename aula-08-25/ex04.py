# Estudo de Caso 4 - Controle de Vendas em uma Loja de Eletrônicos
# Contexto do Problema
# Imagine que você trabalha em uma loja de eletrônicos que precisa organizar melhor o registro
# diário de vendas. Até então, os vendedores anotavam em papel ou planilhas, mas o dono pediu
# para criar um programa simples em Python para armazenar, analisar e gerar pequenos
# relatórios sobre as vendas do dia.
# O sistema precisa:
# 1. Guardar os produtos vendidos (nome e preço).
# 2. Mostrar o valor total arrecadado.
# 3. Identificar o produto mais caro e o mais barato do dia.
# 4. Permitir consultar se um produto específico foi vendido.

class Produto:
    def __init__(self, nome, preco, vendido):
        self.nome = nome
        self.preco = preco
        self.vendido = vendido

def valorTotal(listaProdutos):
    total = 0
    for p in listaProdutos:
        if p.vendido:
            total += p.preco
    return total

def maisCaro(listaProduto):
    item = listaProduto[0]
    for p in listaProduto:
        if p.preco > item.preco:
            item = p
    return item

def menosCaro(listaProduto):
    item = listaProduto[0]
    for p in listaProduto:
        if p.preco < item.preco:
            item = p
    return item

def pesquisarProduto(nome, listaProduto):
    for p in listaProduto:
        if p.nome.lower() == nome.lower():
            return p
    return None

produtos = []

print("===== Guardar produtos =====")
while True:
    nome = input("nome do produto: ")
    preco = float(input("preco do produto: "))
    vendidoCheck = input("Item foi vendido? [s/n] ")
    vendido = None
    if vendidoCheck.lower() in ["s", "si", "sim"]:
        vendido = True
    else:
        vendido = False
    produto = Produto(nome, preco, vendido)
    produtos.append(produto)

    fimDeLista = input("Guardar mais produtos? [s/n] ")
    if fimDeLista.lower() not in ["s", "si", "sim"]:
        break

total = valorTotal(produtos)
pCaro = maisCaro(produtos)
pBarato = menosCaro(produtos)

print("="*50)
print(f"Total arrecadado: {total}")
print(f"Produto mais caro: {pCaro.nome} - {pCaro.preco:.2f} - {'vendido' if pCaro.vendido else 'não vendido'}")
print(f"Produto mais barato: {pBarato.nome} - {pBarato.preco:.2f} - {'vendido' if pBarato.vendido else 'não vendido'}")
print("="*50)

pesquisa = input("consultar produto, digite um produto(nome): ")
consulta = pesquisarProduto(pesquisa, produtos)
if consulta != None:
    print(f"Produto: {consulta.nome} - {consulta.preco:.2f} - {'vendido' if consulta.vendido else 'não vendido'}")
else:
    print("Produto não encontrado")