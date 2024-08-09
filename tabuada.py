cont = 1

num = int(input("Digite um  número para ver a tabuada: "))

while cont <= 10:
    linha = f"{num} x {cont:2} = {num * cont:2}"
    print(f'{linha:^20}')
    cont += 1
