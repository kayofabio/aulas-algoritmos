# Caso5: Controle de Participação em um Evento
# Os organizadores de um evento registraram os nomes dos participantes de cada atividade em
# listas separadas.
# • Exemplo:
# o Palestra: ["Ana", "Carlos", "Marina"]
# o Workshop: ["Carlos", "João", "Ana"]
# o Mesa-redonda: ["Marina", "João", "Paula"]
# Eles precisam:
# 1. Saber quem participou de todas as atividades.
# 2. Saber quem participou de apenas uma atividade.
# 3. Gerar uma lista com todos os nomes únicos dos participantes.
# 4. Contar quantos participantes distintos houve no evento.

pessoas = ["Ana", "Carlos", "Mariana", "João", "Paula"]

palestra = ["Ana", "Carlos", "Marina"]
workshop = ["Carlos", "João", "Ana"]
mesaRedonda = ["Marina", "João", "Paula"]

def presenteEmTodos(pessoas, evento1, evento2, evento3):
    presentes = []
    for p in pessoas:
        if p in evento1 and p in evento2 and p in evento3:
            presentes.append(p)
    return presentes

def presenteUnico(pessoas, evento1, evento2, evento3):
    presentes = []
    for p in pessoas:
        if (p in evento1 and p not in evento2 and p not in evento3) or (p not in evento1 and p in evento2 and p not in evento3) or (p not in evento1 and p not in evento2 and p in evento3):
            presentes.append(p)
    return presentes

presentes = presenteEmTodos(pessoas, palestra, workshop, mesaRedonda)
presentesUnico = presenteUnico(pessoas, palestra, workshop, mesaRedonda)

print("Pessoas que participaram de todos os eventos:")
if presentes:
    for p in presentes:
        print(p)
else:
    print("Nimguém participou de todas as atividades")

print("\nPessoas que participaram de apenas um evento:")
if presentesUnico:
    for p in presentesUnico:
        print(p)
else:
    print("Nimguém participou de apenas uma atividade")

print("\nPessoas que participaram dos eventos: ")
for p in pessoas:
    print(p)

print(f"\ntotal de pessoas: {len(pessoas)}")