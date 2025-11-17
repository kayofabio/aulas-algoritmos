# Adicionar conteúdo ao final de um arquivo.
with open("texto.txt", "a") as file:
    file.write("Nova linha do texto\n")
    file.write("mais uma linha ae")
    file.close()

with open("texto.txt", "r") as file:
    for i in file:
        print(i)
    file.close()