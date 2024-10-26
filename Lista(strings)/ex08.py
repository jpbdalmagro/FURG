''' Escreva um programa em python que leia uma string, e substitua cada segmento de dois ou mais espaços em branco por um só caractere de espaço.
    Não deve ser utilizada qualquer função no python que trabalhe com strings.'''
    
frase = input("Digite uma frase: ")
nova_frase = ''
espaco = False

for letra in frase:
    if letra == ' ':
        if not espaco:
            nova_frase += ' '
            espaco = True
    else:
        nova_frase += letra
        espaco = False
        
print(nova_frase)
