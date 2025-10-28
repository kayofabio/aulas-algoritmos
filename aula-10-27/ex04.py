senha = input("digite senha: ")

def verificar_senha(senha):
    try:
        if len(senha) < 8:
            raise Exception("Senha deve ter no minimo 8 caracters")
        if not any(char.isdigit() for char in senha):
            raise Exception("Senha deve ter pelo menos 1 digito")
        print("Senha válida")
    except Exception as erro:
        print(f"erro: {erro}")
    else:
        print("programa executado com sucesso!")
    finally:
        print("Fim de programa")

verificar_senha(senha)