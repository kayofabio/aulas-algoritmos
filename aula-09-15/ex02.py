# Problema 2 – Academia e Desempenho dos Atletas
# A academia guarda os atletas em uma lista de dicionários, cada um com:
# nome, idade, modalidades (lista de esportes), treinos (dicionário com o nome do esporte como
# chave e a quantidade de treinos realizados como valor).
# Tarefas:
# 1. Crie uma função que calcule a média de idade dos atletas que praticam um esporte
# específico.
# 2. Crie uma função que, dado um atleta, informe qual esporte ele mais treinou.
# 3. Monte uma lista com os atletas que praticam mais de 2 modalidades e exiba seus
# nomes.

def mediaIdade(atletas):
    resultado = 0
    for atleta in atletas:
        resultado += atleta["idade"]
    return resultado/len(atletas)

def esporteMaisTreinado(atletas,nomeAtleta):
    for atleta in atletas:
        if atleta["nome"].lower() == nomeAtleta.lower():
            return max(atleta["treinos"])
    return None

def maisDe2Modalidades(atletas):
    resultado = []
    for atleta in atletas:
        if len(atleta["modalidades"]) > 2:
            resultado.append(atleta)
    return resultado

atletas = [
    {
        "nome": "Lucas",
        "idade": 20,
        "modalidades": ["Natação", "Corrida"],
        "treinos": {"Natação": 12, "Corrida": 8}
    },
    {
        "nome": "Mariana",
        "idade": 25,
        "modalidades": ["Musculação", "Yoga", "Pilates"],
        "treinos": {"Musculação": 15, "Yoga": 10, "Pilates": 5}
    },
    {
        "nome": "João",
        "idade": 22,
        "modalidades": ["Corrida", "Ciclismo"],
        "treinos": {"Corrida": 20, "Ciclismo": 18}
    }
]

media = mediaIdade(atletas)
print("="*50)
print(f"Idade média dos atletas: {media:.2f}")

print("="*50)
nomeAtleta = input("digite um nome de atleta para ver o esporte mais treinado: ")
esporte = esporteMaisTreinado(atletas ,nomeAtleta)
print(f"esporte mais treinado: {esporte}")

print("="*50)
print("atletas que fazem mais de duas modalidades:")
atletasModalidades = maisDe2Modalidades(atletas)
for atleta in atletasModalidades:
    print(atleta["nome"])