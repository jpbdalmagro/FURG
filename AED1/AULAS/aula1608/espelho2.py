#Leia um nome e faça o espelho dele

nome = input("Digite o nome: ")
nome = nome + " "
nome_sep = nome_invertido = ''
cont = 0

while cont < len(nome):
    char = nome[cont]
    if char == ' ':
        contrario = len(nome_sep)
        espelho = ''
        while contrario > 0:
            espelho = espelho + nome_sep[contrario - 1]
            contrario -= 1
        if not nome_invertido:    
            nome_invertido = espelho
        else:
            nome_invertido = nome_invertido + " " + espelho
        nome_sep = ''    
    else:
        nome_sep = nome_sep + char
    cont += 1
    
print(nome_invertido)
