# Problema 4 – Ranking de Filmes
# Você recebeu uma lista de filmes (cada filme é um dicionário) com os campos:
# • titulo → nome do filme
# • diretor → nome do diretor
# • bilheteria → valor em milhões de dólares
# • avaliacoes → lista de notas de 1 a 10
# Tarefas:
# 1. Top 3 maiores bilheterias
# o Crie uma função top_bilheteria(filmes) que retorne os 3 filmes com maior
# bilheteria.
# 2. Top 3 melhores avaliados
# o Crie uma função top_avaliacao(filmes) que calcule a média das avaliações de
# cada filme e retorne os 3 melhores.
# 3. Bilheteria por diretor
# o Crie uma função bilheteria_por_diretor(filmes) que retorne um dicionário onde a
# chave é o diretor e o valor é o total de bilheteria de todos os seus filmes.
# 4. Campeão absoluto
# o Crie uma função campeao(filmes) que mostre qual filme é a melhor combinação
# de bilheteria alta e avaliação média alta.

def top_bilheteria(filmes):
    ranking = {}
    for filme in filmes:
        ranking.update({filme["titulo"]: filme["bilheteria"]})
    ranking = dict(sorted(ranking.items(), key=lambda x: x[1], reverse=True))
    return dict(list(ranking.items())[0:3])

def top_avaliacao(filmes):
    avaliacoes = media_filme(filmes)
    avaliacoes = dict(sorted(avaliacoes.items(), key=lambda x: x[1], reverse=True))
    return dict(list(avaliacoes.items())[0:3])

def bilheteria_por_diretor(filmes):
    resultado = {}
    for filme in filmes:
        if filme["diretor"] in resultado:
            resultado[filme["diretor"]] += filme["bilheteria"]
            continue
        resultado[filme["diretor"]] = filme["bilheteria"]
    return resultado

def campeao(filmes):
    ranking = {}
    maior_bilheteria = next(iter(top_bilheteria(filmes).values()))
    maior_avaliacao = next(iter(top_avaliacao(filmes).values()))
    medias = media_filme(filmes)
    for filme in filmes:
        nota_bilheteria = filme["bilheteria"]/maior_bilheteria
        nota_avaliacao = medias[filme["titulo"]]/maior_avaliacao
        ranking[filme["titulo"]] = (nota_avaliacao+nota_bilheteria)/2
    ranking = dict(sorted(ranking.items(), key=lambda x: x[1], reverse=True))
    return dict(list(ranking.items())[0:1])


def media_filme(filmes):
    medias = {}
    for filme in filmes:
        media = round(sum(filme["avaliacoes"])/len(filme["avaliacoes"]), 1)
        medias.update({filme["titulo"]: media})
    return medias

filmes = [
    {
        "titulo": "Inception",
        "diretor": "Christopher Nolan",
        "bilheteria": 830,
        "avaliacoes": [9, 10, 8, 9, 10]
    },
    {
        "titulo": "Avengers: Endgame",
        "diretor": "Anthony Russo",
        "bilheteria": 2797,
        "avaliacoes": [9, 9, 10, 10, 9]
    },
    {
        "titulo": "The Dark Knight",
        "diretor": "Christopher Nolan",
        "bilheteria": 1005,
        "avaliacoes": [10, 10, 9, 10, 10]
    },
    {
        "titulo": "Jurassic Park",
        "diretor": "Steven Spielberg",
        "bilheteria": 1029,
        "avaliacoes": [8, 9, 9, 8, 9]
    }
]

ranking_bilheteria = top_bilheteria(filmes)
print("TOP 3 MAIORES BILHETERIAS:")
for i, (key, value) in enumerate(ranking_bilheteria.items(), start=1):
    print(f"{i}º {key}: {value} milhões")
print("="*50)

ranking_avaliacoes = top_avaliacao(filmes)
print("\nTOP 3 MAIORES AVALIAÇÕES:")
for i, (key, value) in enumerate(ranking_avaliacoes.items(), start=1):
    print(f"{i}º {key}: {value}")
print("="*50)

bilheterias = bilheteria_por_diretor(filmes)
print("\nBILHETERIA POR DIRETOR:")
for key, value in bilheterias.items():
    print(f"{key}: {value} milhões")

print("\nFILME CAMPEÃO")
filme, nota = next(iter(campeao(filmes).items()))
print(f"{filme}\nnota: {nota:.2f}")
