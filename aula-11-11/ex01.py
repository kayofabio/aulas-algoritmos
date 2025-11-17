# Ler todo o conteúdo de um arquivo de texto.
with open("texto.txt", "r") as file:
    conteudo = file.read()
    print(conteudo)