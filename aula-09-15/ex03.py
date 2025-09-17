# Problema 3 – Loja de Música Online com Estatísticas
# Uma loja virtual armazena músicas em uma lista de dicionários, cada música com:
# titulo, artista, downloads, avaliacoes (lista de notas de 1 a 5).
# Tarefas:
# 1. Crie uma função que calcule a nota média de avaliação de cada música.
# 2. Crie uma função que mostre qual artista tem o maior número total de downloads
# somando todas as suas músicas.
# 3. Monte um ranking das músicas mais bem avaliadas (ordem decrescente da média das
# notas).

def mediaMusicas(musicas):
    medias = {}
    for musica in musicas:
        media = round(sum(musica["avaliacoes"])/len(musica["avaliacoes"]), 1)
        medias.update({musica["titulo"]: media})
    return medias

def maiorDownload(musicas):
    maior = musicas[0]
    for musica in musicas:
        if musica["downloads"] > maior["downloads"]:
            maior = musica
    return maior

def rankingMusicas(musicas):
    ranking = mediaMusicas(musicas)
    return dict(sorted(ranking.items(), key=lambda x: x[1], reverse=True))

musicas = [
    {
        "titulo": "Back in Black",
        "artista": "AC/DC",
        "downloads": 6800,
        "avaliacoes": [5, 4, 5, 5, 4, 5]
    },
    {
        "titulo": "Stairway to Heaven",
        "artista": "Led Zeppelin",
        "downloads": 8900,
        "avaliacoes": [5, 5, 4, 5, 5, 5]
    },
    {
        "titulo": "Enter Sandman",
        "artista": "Metallica",
        "downloads": 8100,
        "avaliacoes": [5, 5, 5, 4, 4, 5, 5]
    }
]

medias = mediaMusicas(musicas)
maior = maiorDownload(musicas)
ranking = rankingMusicas(musicas)

print("MÉDIA DAS AVALIAÇÕES:")
for key, value in medias.items():
    print(f"{key}: {value}")
print("="*50)

print("\nMAIOR DOWNLOAD:")
print(f"{maior["artista"]}: {maior["downloads"]} downloads")
print("="*50)

print("\nRANKING DE MÚSICAS MAIS AVALIADAS:")
for key, value in ranking.items():
    print(f"{key}: {value}")
print("="*50)