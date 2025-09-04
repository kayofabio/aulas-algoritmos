# Lista de Exercícios
# 1. Crie um dicionário chamado aluno com as chaves "nome", "idade" e "curso".
# Em seguida, exiba apenas o nome do aluno.
# 2. Adicione uma nova chave "nota" com valor 9.5 ao dicionário aluno.
# Depois, remova a chave "idade".
# 3. Dado o dicionário abaixo, escreva um código que exiba cada produto e seu preço:
# produtos = {"Arroz": 15.90, "Feijão": 9.50, "Macarrão": 4.20}
# 4. Dado o dicionário aluno, verifique se existe a chave "curso".
# 5. Crie um dicionário chamado turma que contenha dois alunos, cada um com nome
# e nota.
# Depois, exiba o nome do primeiro aluno e a nota do segundo aluno.
# 6. Crie um dicionário representando um carro com as chaves: marca, modelo e ano.
# a. Adicione ao dicionário do carro a chave 'cor'.
# b. Crie um dicionário de notas de 3 alunos (nome como chave, nota como
# valor).
# c. Acesse a nota de um dos alunos e exiba.
# d. Remova um aluno do dicionário de notas.

aluno = {
    "nome": "Kayo",
    "idade": 22,
    "curso": "Engenharia Software"
    }

print(f"Nome do aluno: {aluno['nome']}")

aluno.update({"nota": 9.5})

print(aluno)

del aluno["idade"]
print(aluno)

produtos = {"Arroz": 15.90, "Feijão": 9.50, "Macarrão": 4.20}

print("="*50)
for key, value in produtos.items():
    print(f"{key}: R$ {value:.2f}")

if "curso" in aluno:
    print("\ntem chave curso\n")
else:
    print("\nNão tem chave curso\n")

print("="*50)
turma = {
    "aluno1": {"nome": "Carlos", "nota": 7},
    "aluno2": {"nome": "Junior", "nota": 6} 
    }

for value in turma.values():
    print(f"{value["nome"]}: {value["nota"]}")

print("="*50)
carro = {
    "marca": "Honda",
    "modelo": "civic",
    "ano": 1997
    }

carro.update({"cor": "vermelho"})

notas = {
    "Jorge": 7,
    "Vitor": 5,
    "Ana": 6
}
keysNotas = list(notas.keys())

print(f"\n{keysNotas[0]}, nota: {notas[keysNotas[0]]}")

del notas["Ana"]