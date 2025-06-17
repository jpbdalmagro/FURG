cont = 0
num = 1
soma = 0

while num != 0:
    num = int(input("Digite um número: "))
    if num != 0:
        soma += num
        cont += 1
print(f"A média dos números digitados é: {soma / cont}")
