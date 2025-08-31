# Caso6: Sistema de Biblioteca
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

class Livro:
    def __init__(self, titulo, usuario, diasEmprestados):
        self.titulo = titulo
        self.usuario = usuario
        self.diasEmprestados = diasEmprestados

def acimaDe7(livros):
    lista = []
    for l in livros:
        if l.diasEmprestados > 7:
            lista.append(l)
    return lista

def usuariosNomes(livros):
    lista = []
    for l in livros:
        lista.append(l.usuario)
    return lista

def maiorEmprestimo(livros):
    maior = livros[0]
    for l in livros:
        if l.diasEmprestados > maior.diasEmprestados:
            maior = l
    return maior

def mediaEmprestimo(livros):
    soma = 0
    for l in livros:
        soma += l.diasEmprestados
    return soma/len(livros)


livros = []
print("===== BIBLIOTECA =====")
print("adicionar livros:")
while True:
    titulo = input("Titulo do livro: ")
    usuario = input("usuário: ")
    dias = int(input("dias emprestados: "))
    livro = Livro(titulo, usuario, dias)
    livros.append(livro)

    fimDeLista = input("adicionar mais livros? [s/n] ")
    if fimDeLista.lower() not in ["s", "si", "sim"]:
        break

lAcimaDe7 = acimaDe7(livros)
lMaiorEmprestimo = maiorEmprestimo(livros)
media = mediaEmprestimo(livros)
usuarios = usuariosNomes(livros)

print(f"\nlivros com mais de 7 dias emprestados: ")
for p in lAcimaDe7:
    print(p.titulo)

print(f"\nLivro emrpestado a mais tempo: {lMaiorEmprestimo.titulo} - {lMaiorEmprestimo.diasEmprestados}")

print(f"\nUsuários:")
for u in usuarios:
    print(u)

print(f"\nMédia de dias de empréstimo: {media:.2f}")