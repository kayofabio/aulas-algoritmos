# Caso4: Análise de Vendas Mensais
# Uma loja online registra o número de vendas de cada dia do mês em uma lista.
# • Exemplo: [10, 15, 20, 5, 0, 8, ...]
# O gerente precisa:
# 1. Calcular o total de vendas no mês.
# 2. Descobrir o dia com mais vendas e o dia com menos vendas.
# 3. Calcular a média de vendas por dia.
# 4. Listar os dias que tiveram vendas acima da média

def totalvendas(vendas):
    total = 0
    for v in vendas:
        total+=v
    return total

def mediaVendas(vendas):
    return totalvendas(vendas)/len(vendas)

def acimaMedia(vendas):
    acima = []
    media = mediaVendas(vendas)
    for v in vendas:
        if v > media:
            acima.append(v)
    return acima

vendas = []
diasTotal = int(input("Total de dias de vendas: "))
for i in range(1, diasTotal+1):
    venda = int(input(f"Número de vendas. {i}º dia: "))
    vendas.append(venda)

total = totalvendas(vendas)
maisVenda = max(vendas)
menosVenda = min(vendas)
media = mediaVendas(vendas)
acimasMedia = acimaMedia(vendas)

print("="*50)
print(f"Total de vendas: {total}")
print(f"Maior númeoro de vendas: {maisVenda}")
print(f"Menor númeoro de vendas: {menosVenda}")
print(f"Média de vendas por dia: {media}")
print("número de vendas acima da média:")
for v in acimasMedia:
    print(v, end=" ")