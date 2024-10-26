# Escreva um programa que mostre a tabuada (0 a 10) de um número fornecido pelo usuário

cont = 1

num = int(input("Digite um  número para ver a tabuada: "))

while cont <= 10:
    linha = f"{num} x {cont:2} = {num * cont:2}"
    print(f'{linha:^20}')
    cont += 1
