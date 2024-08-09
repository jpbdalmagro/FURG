fat = num = int(input("Digite um número: "))
cont = num - 1

while cont > 1:
    fat *= cont
    cont -= 1

print(f"O fatorial do número {num} é {fat}.")