saldo = input("Informe o saldo da conta: ")
trasnferencia = input("Informe valor a ser transferido: ")
try:
    if not saldo.isdigit() or not trasnferencia.isdigit():
        raise ValueError("Saldo e/ou tranferencia inválidos")
    saldo = float(saldo)
    trasnferencia = float(trasnferencia)
    if trasnferencia > saldo:
        raise ValueError("Saldo insuficiente!")
    saldo = saldo - trasnferencia
    print(f"saldo atual: {saldo}")
except ValueError as erro:
    print(f"erro: {erro}")
else:
    print("Transferência realizada com sucesso")
finally:
    print("Fim do programa")