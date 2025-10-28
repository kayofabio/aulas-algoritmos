try:
    numero = input("Digite um número: ")
    if numero <= 10:
        raise ValueError("Número deve ser maior que 10")
    if not numero.isdigit():
        raise ValueError("Valor deve ser um digito")

    print("Número válido")
except ValueError as erro:
    print(f"erro: {erro}")
else:
    print("programa executado com sucesso!")
finally:
    print("Fim de programa")