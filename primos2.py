x = int(input("Digite um número: "))
y = int(input("Digite outro número: "))
primos = 0
cont = 1

print(f"Os números primos entre {x} e {y} são:")

while x <= y:
    while cont <= x:
        if x % cont == 0:
            primos += 1
        cont += 1
    if primos == 2 and x != 1:
        print(x)
    x += 1
    cont = 1
    primos = 0    