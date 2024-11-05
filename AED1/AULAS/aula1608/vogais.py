#Leia um nome e 1. Escreva apenas as vogais do nome, 2. Diga quantas vogais tem
cont = 0
vogais = 0
nome = input("Digite um nome: ")

while cont < len(nome):
    if nome.lower()[cont] in 'aeiou':
        print(nome[cont])
        vogais += 1
    cont += 1
print(vogais)
