#Escreva um programa que receba uma lista de números e retorne uma nova lista contendo apenas os números pares.

numeros = []
numeros_pares = []

while True:
    numeros.append(int(input("Digite um número: ")))
    resp = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if resp == "N":
        break

for n in numeros:
    if n % 2 == 0:
        numeros_pares.append(n)

print(f"Números digitados: {numeros}")
print(f"Números pares: {numeros_pares}")
