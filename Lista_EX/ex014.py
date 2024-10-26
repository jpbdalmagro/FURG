# Escreva um programa que mostre a seguinte sequência de números para um valor N informado pelo usuário

cont = 1

num = int(input("Digite um número: "))

while cont <= num:
    print(f"{cont}" * cont)
    cont += 1
