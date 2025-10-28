cores = {'vermelho': (255, 0, 0), 'verde': (0, 255, 0), 'azul': (0, 0, 255)}

try:
    cor_nome = input("Digite uma cor: ").strip().lower()
    print(f"RGB: {cores[cor_nome]}")
except KeyError:
    print("Cor não existente: ")
else:
    print("programa executado com sucesso!")
finally:
    print("Fim de programa")