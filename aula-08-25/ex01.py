# Estudo de Caso 1 – Temperaturas da Semana
# Enunciado:
# Crie um programa que:
# 1. Receba as temperaturas de 7 dias e armazene em uma lista.
# 2. Mostre a média das temperaturas da semana.
# 3. Informe o dia mais quente e o dia mais frio.
# 4. Mostre quantos dias ficaram acima da média

def mediaTemperatura(temperaturas):
    somaTemps = 0
    for t in temperaturas:
        somaTemps += t
    return somaTemps/len(temperaturas)

def acimaMedia(temperaturas):
    mediaTemp = mediaTemperatura(temperaturas)
    contador = 0
    for t in temperaturas:
        if t > mediaTemp:
            contador += 1
    return contador

temperaturas = []

for dia in range(1, 8):
    temp = float(input(f"temperatura dia {dia}º: "))
    temperaturas.append(temp)

media = mediaTemperatura(temperaturas)
maior = max(temperaturas)
menor = min(temperaturas)
diasAcimaMedia = acimaMedia(temperaturas)

print("="*50)
print(f"Medias da temperaturas: {media:.2f} °C")
print(f"Dia mais quente: {maior} °C")
print(f"Dia mais frio: {menor} °C")
print(f"Dias acima da média: {diasAcimaMedia} °C")