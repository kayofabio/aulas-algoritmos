# Ler um arquivo CSV e retornar os dados como lista de dicionários.

def criar_lista_alunos(arquivo_csv):
    lista = []
    with open(arquivo_csv, "r") as f:
        for i, linha in enumerate(f):
            if i != 0:
                matricula, nome, nota = linha.strip().split(",")
                lista.append({"matricula": matricula, "nome": nome, "nota": float(nota)})
    return lista

alunos = criar_lista_alunos("alunos.csv")
[print(f"Matrícula: {x["matricula"]} | Nome: {x["nome"]} | Nota: {x["nota"]}") for x in alunos]