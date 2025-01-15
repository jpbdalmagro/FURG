# 1)Escreva uma função recursivapara contar quantas vezes o caractere cocorre na strings, onde o caractere e a stringsão fornecidos como parâmetro.

def conta_caractere(s, c):  
    if len(s) == 0:
        return 0
    if s[0] == c:
        return 1 + conta_caractere(s[1:], c)
    else:
        return conta_caractere(s[1:], c)
    

string = input("Digite uma palavra: ")
caractere = input("Digite um caractere: ")

print(conta_caractere(string, caractere))
