try:
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))
    print(f"{n1} : {n2} = {(n1/n2):.2f}")
except ZeroDivisionError:
    print("Nenhum número pode ser divisivel por zero")
except ValueError:
    print("Somente digitos são aceitos")
else:
    print("Divisão feita com sucesso!")
finally:
    print("Fim de programa!")