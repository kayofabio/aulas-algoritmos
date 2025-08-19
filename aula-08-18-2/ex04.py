# 4. Busca Linear
# Dada uma lista de nomes, implemente uma função que busque um nome digitado pelo usuário.
# Informe a posição em que ele aparece ou diga que não foi encontrado.

def nomeExiste(nomes, busca):
    if busca not in nomes:
        return False
    return True

def nomePosicao(nomes, busca):
    for i, n in enumerate(nomes):
        if n == busca:
            return i

nomes = ["lucas", "juliana", "fernando", "amanda", "diego", "ana", "carlos", "maria"]

print(nomes)
busca = input("Digite um nome: ").lower()

if nomeExiste(nomes, busca):
    # print(f"posição: {nomes.index(busca)}")
    print(f"posição: {nomePosicao(nomes, busca)}")
else:
    print("Nome não encontrado")