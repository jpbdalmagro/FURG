print("-"*30)
print("Verificador de números primos")
print("-"*30)

n = int(input("Digite o valor de n: "))
primos = 0
cont = 1

while cont <= n:
    if n % cont == 0:
        primos += 1
    cont  += 1

if primos == 2 and n != 1:
    print(f"{n} é um número primo")
else:
    print(f"{n} não é um número primo")
