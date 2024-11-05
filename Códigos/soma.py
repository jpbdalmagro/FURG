cont = 0
n = int(input("Digite o valor de N: "))
soma = 0

while cont <= n:
    soma += cont
    cont += 1

print("A soma dos números de 1 a", n, "é:", soma)