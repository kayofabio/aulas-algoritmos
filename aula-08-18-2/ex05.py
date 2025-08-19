# 5. Verificação de CPF (simplificado)
# Peça ao usuário um número de 11 dígitos e:
# • Verifique se todos os caracteres são dígitos;
# • Verifique se o tamanho é válido (11);
# • Mostre "CPF válido" ou "CPF inválido".
# (Não precisa calcular os dígitos verificadores ainda — é apenas validação estrutural.)

def checkCPF(cpf):
    if cpf.isdigit():
        if len(cpf) == 11:
            return True
    return False

numero = input("Digite um número de 11 digitos: ")
if checkCPF(numero):
    print("CPF válido")
else:
    print("CPF inválido")