# Buscar uma palavra em um arquivo e exibir as linhas onde ela aparece.
with open("texto.txt", "r") as file:
    busca = "linha"
    linhas = []
    for i, l in enumerate(file, start=1):
        if busca in l:
            linhas.append(i)
    if linhas:
        print(f"A palavra '{busca}' aparece nas linhas: ", end="")
        [print(l, end=" | ") for l in linhas]
    else:
        print(f"A palavra '{busca}' não foi encontrada no arquivo.")
