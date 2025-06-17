# Faça um programa em python que receba uma lista de números inteiros como entrada e retorne a maior soma dos números ímpares
# consecutivos da lista. Caso não haja números ímpares na lista, o programa deve retornar 0.

numeros = []
n1 = n2 = 0


while True:
    
    numeros.append(int(input("Digite um número: ")))
    if input("Deseja continuar? [S/N]: ").upper() == 'N':
        break

for i in range(len(numeros)):
    if numeros[i] % 2 != 0:
        if numeros[i] > n1:
            n2 = n1
            n1 = numeros[i]
        elif numeros[i] > n2:
            n2 = numeros[i]

soma = n1 + n2

print(f"A maior soma dos números ímpares consecutivos é: {soma}")
