# Escreva um programa que recebe uma string do usuário e imprime a string invertida.

palavra = input("Digite uma palavra: ")
cont = len(palavra)

while cont > 0:
    print(palavra.upper()[cont - 1], end='')
    cont -= 1
print('')
