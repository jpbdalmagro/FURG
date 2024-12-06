#Leia um nome e deixe ele capitalizado

cont = 0
nome_cap = nome_sep = ''
nome = str(input("Digite seu nome completo em letras minusculas: "))
nome += ' '

while cont < len(nome):
    char = nome[cont]
    if not char == ' ':
        nome_sep += char
    else:
        i = 0
        capilizado = ''
        if nome_sep == 'de' or nome_sep == 'da' or nome_sep == 'do' or nome_sep == 'das' or nome_sep == 'dos':
            nome_cap += nome_sep + ' '
        else:
            while i < len(nome_sep):
                if i == 0:
                    encode = ord(nome_sep[i]) - 32
                    capilizado += chr(encode)
                else:
                    capilizado += nome_sep[i]
                i += 1
            nome_cap += capilizado + ' '
        nome_sep = ''
    cont += 1

print(nome_cap)
