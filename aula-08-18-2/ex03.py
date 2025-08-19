# 3. Estatísticas de Notas
# Leia as notas de uma turma e:
# • Calcule a média;
# • Mostre a maior e a menor nota;
# • Exiba o percentual de alunos acima da média.

def calcMedia(notas):
    resultado = 0
    for n in notas:
        resultado += n
    return resultado/len(notas)

def maiorNota(notas):
    maior = notas[0]
    for n in notas:
        if n > maior:
            maior = n
    return maior

def menorNota(notas):
    menor = notas[0]
    for n in notas:
        if n < menor:
            menor = n
    return menor

def pocentagemAcimaDaMedia(media, notas):
    qtdAcimaMedia = 0
    for n in notas:
        if n > media:
            qtdAcimaMedia += 1
    return qtdAcimaMedia*100/len(notas)

print("Média da turma")
alunos = int(input("quantos alunos tem a turma? "))
notasAlunos = []

for i, aluno in enumerate(range(alunos), start=1):
    n = float(input(f"Nota do {i}º aluno: "))
    notasAlunos.append(n)

media = calcMedia(notasAlunos)
maior = maiorNota(notasAlunos)
menor = menorNota(notasAlunos)
mediaPorcentagem = pocentagemAcimaDaMedia(media, notasAlunos)

print("="*50)
print(f"Media da turma: {media:.2f}")
print(f"Maior nota: {maior}")
print(f"Menor nota: {menor}")
print(f"percentual de alunos acima da média: {mediaPorcentagem:.2f}%")