# Contar o número de linhas em um arquivo.
with open("texto.txt", "r") as file:
    linhas = 0
    for i in file:
        linhas += 1
    print(f"Numero de linhas: {linhas}")