# Escrever conteúdo em um arquivo (sobrescrevendo).
with open("texto.txt", "w") as file:
    file.write("Arquivo sobreescrito\n")
    file.close()

with open("texto.txt", "r") as file:
    for i in file:
        print(i)
    file.close()