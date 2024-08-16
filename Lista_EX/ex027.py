#Faça um programa em python que desenhe uma pirâmide conforme 2 dados informados pelo usuário. O primeiro dado indica o "tijolo" e o segundo a quantidade de andares.

cont = 1

tijolo = input("Digite um caractere: ")
andares = int(input("Digite um número: "))

while cont <= andares:
    espacos = ' ' * (andares - cont)
    tijolos = tijolo * (2 * cont - 1)
    print(espacos + tijolos)
    cont += 1
