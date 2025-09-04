# Caso6: Sistema de Biblioteca (com dicionario)
# Uma biblioteca mantém uma lista de livros emprestados, onde cada item é representado por
# [titulo, usuario, dias_emprestado].
# Exemplo:
# [
#  ["Dom Casmurro", "Ana", 5],
#  ["1984", "Carlos", 12],
#  ["O Hobbit", "Marina", 3]
# ]
# O sistema precisa:
# 1. Listar apenas os livros que estão emprestados há mais de 7 dias.
# 2. Encontrar o livro emprestado há mais tempo.
# 3. Gerar uma lista apenas com os nomes dos usuários que têm livros emprestados.
# 4. Calcular a média de dias de empréstimo.

def acimaDe7(livros: dict):
    dic = {}
    for k, v in livros.items():
        if v["dias_emprestados"] > 7:
            dic.update({k: v})
    return dic

def usuariosNomes(livros: dict):
    dic = {}
    for i, v in enumerate(livros.values()):
        nome = f"nome{i}"
        dic.update({nome: v["usuario"]})
    return dic

def maiorEmprestimo(livros: dict):
    key = None
    for k in livros:
        key = k
        break
    maior = {key: livros[key]}
    for k, v in livros.items():
        if v["dias_emprestados"] > maior[key]["dias_emprestados"]:
            maior = {k: v}
            key = k
    return maior

def mediaEmprestimo(livros: dict):
    soma = 0
    for v in livros.values():
        soma += v["dias_emprestados"]
    return soma/len(livros)

livros = {}

while True:
    titulo = input("Titulo do livro: ")
    usuario = input("usuário: ")
    dias = int(input("dias emprestados: "))
    livro = {titulo: {"usuario": usuario, "dias_emprestados": dias}}
    livros.update(livro)

    fimDeLista = input("adicionar mais livros? [s/n] ")
    if fimDeLista.lower() not in ["s", "si", "sim"]:
        break

lAcimaDe7 = acimaDe7(livros)
lMaiorEmprestimo = maiorEmprestimo(livros)
media = mediaEmprestimo(livros)
usuarios = usuariosNomes(livros)

print(f"\nlivros com mais de 7 dias emprestados: ")
for k, v in lAcimaDe7.items():
    print(f"{k}: {v["dias_emprestados"]}")

k = next(iter(lMaiorEmprestimo))
print(f"\nLivro emrpestado a mais tempo: {k} - {lMaiorEmprestimo[k]["dias_emprestados"]} dias")

print(f"\nUsuários:")
for v in usuarios.values():
    print(v)

print(f"\nMédia de dias de empréstimo: {media:.2f}")