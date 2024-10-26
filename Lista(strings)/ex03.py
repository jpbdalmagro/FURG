# Escreva um programa que recebe uma string do usuário e imprime a string com todas as letras maiúsculas convertidas 
# para minúsculas e vice-versa

string = input("Digite uma string: ")

for letra in string:
    if str.islower(letra):
        print(letra.upper(), end='')
    else:
        print(letra.lower(), end='')
print('')
