# Caso3: Supermercado – Controle de Estoque
# Um supermercado mantém uma lista de produtos e seus preços.
# • Cada item será representado como [nome, quantidade, preco_unitario].
# • O sistema deve:
# 1. Calcular o valor total em estoque.
# 2. Encontrar o produto de maior valor total (quantidade × preço).
# 3. Gerar uma lista apenas com os nomes dos produtos com estoque abaixo de 5
# unidades.
# 4. Permitir buscar um produto pelo nome e retornar seus dados.

class Produto:

    def __init__(self, nome, preco, qtd):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd
    
    def total(self):
        return self.qtd * self.preco

def valorTotal(produtos):
    soma = 0
    for p in produtos:
        soma += p.total()
    return soma

def filtarPorQtd(produtos, qtdMax):
    lista = []
    for p in produtos:
        if p.qtd < qtdMax:
            lista.append(p)
    return lista

def produtoMaiorValorTotal(produtos):
    item = produtos[0]
    for p in produtos:
        if p.total() > item.total():
            item = p
    return item

def pesquisarProduto(nome, produtos):
    for p in produtos:
        if p.nome.lower() == nome.lower():
            return p
    return None

print("===== ADICIONAR ITEM EM ESTOQUE =====")
produtos = []
while True:
    nome = input("nome do produto: ")
    preco = float(input("preço do produto: "))
    qtd = int(input("Quantidade do produto: "))
    produto = Produto(nome, preco, qtd)
    produtos.append(produto)

    fimDeLista = input("Guardar mais produtos? [s/n] ")
    if fimDeLista.lower() not in ["s", "si", "sim"]:
        break

pTotal = valorTotal(produtos)
pMaiorValor = produtoMaiorValorTotal(produtos)
pQtdAbaixo5 = filtarPorQtd(produtos, 5)

print("="*50)
print(f"valor total em estoque: R$ {pTotal:.2f}")
print(f"Produto com maior valor total: {pMaiorValor.nome} - R$ {pMaiorValor.total():.2f}")
print("produtos com qunatidade menor que 5:")
for p in pQtdAbaixo5:
    print(f"{p.nome}: {p.qtd}")
print("="*50)
pesquisa = input("consultar item em estoque: ")
consulta = pesquisarProduto(pesquisa, produtos)
if consulta != None:
    print(f"Produto: {consulta.nome}\nPreço: R$ {consulta.preco:.2f}\nquantidade: {consulta.qtd}\nValor total: R$ {consulta.total():.2f}")
else:
    print("Item não encontrado!")