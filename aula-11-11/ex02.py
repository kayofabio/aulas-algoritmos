# Ler um arquivo linha por linha.

with open("texto.txt", "r") as file:
    for linha in file:
        print(linha)