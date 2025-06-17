#Leia um nome completo e mostre nome por nome

nome_sep = ''
cont = 0
nome = str(input("Digite seu nome completo: "))
nome = nome + ' '

while cont < len(nome):
    if nome[cont] == ' ':
        print(nome_sep)
        nome_sep = ''
    else:
        nome_sep = nome_sep + nome[cont]
    cont += 1
           
