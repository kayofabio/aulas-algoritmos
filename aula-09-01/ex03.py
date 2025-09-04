# Estudo de Caso 2: Agenda Telefônica
# Uma agenda pode ser representada como um dicionário em que as chaves são os nomes
# das pessoas e os valores são os números de telefone.
# Exemplo:
# agenda = {"Maria": "99999-1234", "João": "98888-5678"}
# print("Telefone da Maria:", agenda["Maria"])

agenda = {}


print("===== ADICIONAR CONTATOS =====")
while True:
    nome = input("nome: ")
    numero = input("número: ")

    numero = list(numero)
    numero.insert(5, "-")
    numero = "".join(numero)

    agenda.update({nome: {"numero": numero}})

    parar = input("Adicionar mais pessoas? [s/n]")
    if parar.lower() not in ["s", "si", "sim"]:
        break

print("===== AGENDA =====")
for key, value in agenda.items():
    print(f"{key}: {value["numero"]}")
