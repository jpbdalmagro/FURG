#Escreva um programa que receba duas listas do usuário e retorne uma nova lista contendo apenas os elementos comuns entre as duas listas.

lista1 = []
lista2 = []
comuns = []

while True:
    lista1.append(int(input("Digite um número para a primeira lista: ")))
    resp = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if resp == "N":
        break

while True:
    lista2.append(int(input("Digite um número para a segunda lista: ")))
    resp = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if resp == "N":
        break

for n in lista1:
    if n in lista2:
        comuns.append(n)

print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Elementos comuns: {comuns}")
