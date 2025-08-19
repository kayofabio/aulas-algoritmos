# 3. Crie uma função que verifique se um número é primo.

def isOdd(x):
    y = abs(x)
    if y < 2:
        return False
    
    if y == 2:
        return True
    
    for n in range(2, y):
        if y % n == 0:
            return False
        
    return True

num = int(input("Digite um número: "))

if isOdd(num):
    print(f"O número {num} é primo")
else:
    print(f"O número {num} não é primo ")