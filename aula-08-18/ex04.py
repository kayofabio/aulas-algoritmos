# 4. Desenvolva um programa que leia uma lista de números e mostre a média deles.

def averageList(numsList):
    numsSum = 0
    for x in numsList:
        numsSum += x
    return numsSum/len(numsList)

print("Média de uma lista de números")
sizeList = int(input("Qual o tamanho da lista? "))
nums = []
for i, n in enumerate(range(sizeList), start=1):
    n = float(input(f"Digite o {i}º número: "))
    nums.append(n)
average = averageList(nums)
print(f"A média dos números é {average:.2f}")