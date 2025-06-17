#Leia um string e escreva letra por letra

cont = 0
string = input("Digite uma palavra: ")

while cont < len(string):
    print(string[cont])
    cont += 1
