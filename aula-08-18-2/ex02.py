# 2. Validação de Login
# Implemente um algoritmo que simule um sistema de login:
# • O usuário tem 3 tentativas para digitar a senha correta (senha123).
# • Caso erre todas, mostre "Acesso bloqueado".
# • Caso acerte, mostre "Bem-vindo!".

def checkSenha(senha):
    if senha == senhaCorreta:
        return True
    return False

senhaCorreta = "senha123"

print("Sistema de login")

for i in range(1, 4):
    if i > 1:
        print("Senha incorreta. Tente novamente!")
    senha = input("Digite sua senha: ")
    if checkSenha(senha):
        print("Bem-vindo!")
        break
    if i == 3:
        print("Acesso negado!")
