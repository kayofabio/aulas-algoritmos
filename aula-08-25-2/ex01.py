# Caso1: Controle de Presença em Sala de Aula
# Uma professora precisa registrar a presença dos alunos durante a semana.
# • Cada dia da semana terá uma lista com os nomes dos presentes.
# • No final, ela precisa:
# 1. Saber quais alunos estiveram presentes todos os dias.
# 2. Saber quais alunos faltaram em pelo menos um dia.
# 3. Saber o número total de presenças por aluno.

alunos = ["Lucas", "Maria", "João", "Ana", "Felipe", "Gustavo"]

segunda = ["Lucas", "Maria", "Ana", "Felipe"]
terca = ["Maria", "João", "Ana", "Felipe"]
quarta = ["Lucas", "Maria", "Gustavo", "Felipe"]
quinta = ["Maria", "Ana", "Felipe"]
sexta = ["Maria", "João", "Felipe"]

def presencaPerfeita(alunos, segunda, terca, quarta, quinta, sexta):
    lista = []
    for a in alunos:
        if a in segunda and a in terca and a in quarta and a in quinta and a in sexta:
            lista.append(a)
    return lista

def faltouUmDia(alunos, segunda, terca, quarta, quinta, sexta):
    lista = []
    for a in alunos:
        if (a not in segunda) or (a not in terca) or (a not in quarta) or (a not in quinta) or (a not in sexta):
            lista.append(a)
    return lista

def totalPresencaPorAluno(alunos, segunda, terca, quarta, quinta, sexta):
    lista = []
    for a in alunos:
        presencas = 0
        if a in segunda:
            presencas += 1
        if a in terca:
            presencas += 1
        if a in quarta:
            presencas += 1
        if a in quinta:
            presencas += 1
        if a in sexta:
            presencas += 1
        lista.append(presencas)
    return lista

presencaPerfeitaLista = presencaPerfeita(alunos, segunda, terca, quarta, quinta, sexta)
faltouUmDiaLista = faltouUmDia(alunos, segunda, terca, quarta, quinta, sexta)
totalPresencaPorAlunoLista = totalPresencaPorAluno(alunos, segunda, terca, quarta, quinta, sexta)

print("alunos:")
for a in alunos:
    print(a)
print("\nalunos presentes todos os dias")
for i in presencaPerfeitaLista:
    print(i)
print("\nfaltaram pelo menos 1 dia:")
for i in faltouUmDiaLista:
    print(i)
print("\ntotal de presenças por aluno")
for i, p in enumerate(totalPresencaPorAlunoLista):
    print(f"{alunos[i]}: {p}")