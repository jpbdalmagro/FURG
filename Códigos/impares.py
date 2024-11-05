cont = 0
num = int(input("Digite um número: "))

if num % 2 == 0:
    num += 1

while cont < 6:
    print(num)
    num += 2
    cont += 1