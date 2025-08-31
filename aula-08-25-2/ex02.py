# Caso2: Distâncias em Km
# 1. Receba as distâncias percorridas em 6 viagens e armazene em uma lista.
# 2. Calcule a distância total percorrida.
# 3. Mostre a maior e a menor distância.
# 4. Calcule a média das distâncias arredondada para cima (use math.ceil).

import math

def total(distancias):
    soma = 0
    for d in distancias:
        soma += d
    return soma

def media(distancias):
    return total(distancias)/len(distancias)

print("===== distâncias percorridas em 6 viagens (Km) =====")
distancias = []
for i in range(1, 7):
    distancia = float(input(f"Distância N {i}º: "))
    distancias.append(distancia)

dTotal = total(distancias)
dMenor = min(distancias)
dMaior = max(distancias)
dMedia = math.ceil(media(distancias))

print("="*50)
print(f"Distância total percorrida: {dTotal:.2f} Km")
print(f"Menor distância: {dMenor:.2f} Km\nMaior distância: {dMaior:.2f} Km")
print(f"Média das distâncias: {dMedia:.2f} Km")