# Estudo de Caso : Cadastro de Produtos
# Um supermercado deseja armazenar informações sobre seus produtos. Cada produto deve
# conter: nome, preço e quantidade em estoque. Utilize um dicionário para representar e
# manipular essas informações.
# Exemplo:
# produto = {"nome": "Arroz", "preco": 25.90, "estoque": 100}
# print(f"O produto {produto["nome"]} custa R${produto["preco"]}")

produtos = {}

print("===== ADICIONAR PRODUTOS =====")
while True:
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: "))
    estoque = int(input("quantidade em estoque: "))

    produtos.update({nome: {"preco": preco, "estoque": estoque}})

    parar = input("Adicionar mais produtos? [s/n]")
    if parar.lower() not in ["s", "si", "sim"]:
        break

print("===== PRODUTOS =====")
for key, value in produtos.items():
    print(f"{key}: R$ {value["preco"]:.2f} / estoque: {value["estoque"]}")