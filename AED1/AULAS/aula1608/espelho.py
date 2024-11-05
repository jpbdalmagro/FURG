#Leia uma palavra e mostre seu espelho

palavra = input("Digite uma palavra: ")
cont = len(palavra)

while cont > 0:
    print(palavra.upper()[cont - 1], end='')
    cont -= 1
print('')
